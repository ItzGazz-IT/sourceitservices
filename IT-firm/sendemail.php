<?php

define("RECIPIENT_NAME", "Source IT Services");
define("RECIPIENT_EMAIL", "support@itserv.co.za");

function clean_input($value)
{
  $value = trim((string)$value);
  return preg_replace('/[\r\n]+/', ' ', $value);
}

$userName = clean_input($_POST['username'] ?? '');
$senderEmail = filter_var(clean_input($_POST['email'] ?? ''), FILTER_VALIDATE_EMAIL);
$senderPhone = clean_input($_POST['phone'] ?? '');
$company = clean_input($_POST['company'] ?? '');
$service = clean_input($_POST['service'] ?? '');
$userSubject = clean_input($_POST['subject'] ?? '');
$consent = clean_input($_POST['consent'] ?? '');
$message = trim((string)($_POST['message'] ?? ''));
$honeypot = trim((string)($_POST['website'] ?? ''));

// Honeypot anti-spam field should stay empty.
if ($honeypot !== '') {
  header('Location: contact.html?message=failed');
  exit;
}

$requiredIsValid =
  $userName !== '' &&
  $senderEmail &&
  $company !== '' &&
  $service !== '' &&
  $userSubject !== '' &&
  $message !== '' &&
  strtolower($consent) === 'yes';

if ($requiredIsValid) {
  $recipient = RECIPIENT_NAME . ' <' . RECIPIENT_EMAIL . '>';
  $emailSubject = '[Website Enquiry] ' . $userSubject;

  $body = "New website enquiry\n\n";
  $body .= "Name: {$userName}\n";
  $body .= "Email: {$senderEmail}\n";
  $body .= "Phone: {$senderPhone}\n";
  $body .= "Company: {$company}\n";
  $body .= "Service: {$service}\n";
  $body .= "Subject: {$userSubject}\n\n";
  $body .= "Message:\n{$message}\n";

  $headers = "From: Source IT Services Website <no-reply@itserv.co.za>\r\n";
  $headers .= "Reply-To: {$senderEmail}\r\n";
  $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

  $success = mail($recipient, $emailSubject, $body, $headers);
  header('Location: contact.html?message=' . ($success ? 'success' : 'failed'));
  exit;
}

header('Location: contact.html?message=failed');
exit;

?>