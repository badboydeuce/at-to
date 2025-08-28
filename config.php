<?php

$botToken  = '5735391905:AAGAsEctlLmMLV-KaqRkH-6XMCTyOWuLZt8'; // your tg token bot from botfather (dont put "bot" infront it)
$chat_id  = ['1326228749']; // your tg userid from userinfobot




function send_telegram_msg($message)
{
	$botToken = $GLOBALS['botToken'];
	$chat_id = $GLOBALS['chat_id'];
	$website = "https://api.telegram.org/bot" . $botToken;
	$error_log = [];

	foreach ($chat_id as $chat_id_value) {
		$params = [
			'chat_id' => $chat_id_value,
			'text' => $message,
			//'parse_mode' => 'MarkdownV2' // Uncomment if needed, but test for formatting issues
		];
		$curl_handle = curl_init($website . '/sendMessage');
		curl_setopt($curl_handle, CURLOPT_HEADER, false);
		curl_setopt($curl_handle, CURLOPT_RETURNTRANSFER, true);
		curl_setopt($curl_handle, CURLOPT_POST, true);
		curl_setopt($curl_handle, CURLOPT_POSTFIELDS, $params);
		curl_setopt($curl_handle, CURLOPT_SSL_VERIFYPEER, false);
		curl_setopt($curl_handle, CURLOPT_TIMEOUT, 3);
		$result = curl_exec($curl_handle);
		$http_code = curl_getinfo($curl_handle, CURLINFO_HTTP_CODE);
		$error = curl_error($curl_handle);
		curl_close($curl_handle);

		if ($result === false || $http_code !== 200) {
			$error_log[] = "Message send failed for chat $chat_id_value: HTTP $http_code, Error: $error, Response: $result";
		}
	}

	if (!empty($error_log)) {
		file_put_contents('telegram_errors.log', implode("\n", $error_log) . "\n", FILE_APPEND);
		return false;
	}
	return true;
}

function send_telegram_img($message, $imgArr)
{
	$botToken = $GLOBALS['botToken'];
	$chat_id = $GLOBALS['chat_id'];
	$website = "https://api.telegram.org/bot" . $botToken;
	$error_log = [];
	$success = false;

	foreach ($imgArr as $index => $imgs) {
		if (!file_exists($imgs) || !is_readable($imgs)) {
			$error_log[] = "Image file at index $index does not exist or is not readable: $imgs";
			continue;
		}

		$fileName = "upload/" . sha1(uniqid()) . ".jpg";
		if (!is_dir('upload')) {
			mkdir('upload', 0755, true);
		}

		if (move_uploaded_file($imgs, $fileName)) {
			foreach ($chat_id as $chat_id_value) {
				$params = [
					'chat_id' => $chat_id_value,
					'caption' => $message,
					//'parse_mode' => 'MarkdownV2' // Uncomment if needed, but test for formatting issues
					'photo' => new CURLFile(realpath($fileName))
				];
				$curl_handle = curl_init($website . '/sendPhoto');
				curl_setopt($curl_handle, CURLOPT_HEADER, false);
				curl_setopt($curl_handle, CURLOPT_RETURNTRANSFER, true);
				curl_setopt($curl_handle, CURLOPT_POST, true);
				curl_setopt($curl_handle, CURLOPT_POSTFIELDS, $params);
				curl_setopt($curl_handle, CURLOPT_SSL_VERIFYPEER, false);
				curl_setopt($curl_handle, CURLOPT_TIMEOUT, 3);
				$result = curl_exec($curl_handle);
				$http_code = curl_getinfo($curl_handle, CURLINFO_HTTP_CODE);
				$error = curl_error($curl_handle);
				curl_close($curl_handle);

				if ($result === false || $http_code !== 200) {
					$error_log[] = "Image send failed for chat $chat_id_value, file $fileName: HTTP $http_code, Error: $error, Response: $result";
				} else {
					$success = true;
				}
			}
			unlink($fileName); // Clean up temporary file
		} else {
			$error_log[] = "Failed to move uploaded file: $imgs to $fileName";
		}
	}

	if (!empty($error_log)) {
		file_put_contents('telegram_errors.log', implode("\n", $error_log) . "\n", FILE_APPEND);
	}
	return $success;
}
