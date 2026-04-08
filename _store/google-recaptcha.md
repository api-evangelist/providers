---
aid: google-recaptcha
url: https://raw.githubusercontent.com/api-evangelist/google-recaptcha/refs/heads/main/apis.yml
apis:
- name: reCAPTCHA Enterprise API
  description: The reCAPTCHA Enterprise API provides advanced bot detection and fraud prevention capabilities for websites and applications. It returns risk scores and reason codes for user interactions, supports creating and managing site keys, assessments, and related resources. The API enables creating assessments for tokens, annotating assessments with feedback, and managing firewall policies for automated protection.
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://cloud.google.com/recaptcha-enterprise/docs
  baseURL: https://recaptchaenterprise.googleapis.com
  tags:
  - Bot Detection
  - Enterprise
  - Risk Assessment
  properties:
  - type: Documentation
    url: https://cloud.google.com/recaptcha-enterprise/docs/reference/rest
  - type: OpenAPI
    url: openapi/recaptcha-enterprise-openapi.yml
  - type: JSONSchema
    url: json-schema/google-recaptcha-assessment-schema.json
- name: reCAPTCHA Site Verify API
  description: The reCAPTCHA Site Verify API is the standard verification endpoint for reCAPTCHA v2 and v3 tokens. After a user completes a reCAPTCHA challenge on the frontend, the backend sends the response token to this API to verify the interaction. The API returns whether the verification succeeded, a score (for v3), the action name, and the hostname.
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://developers.google.com/recaptcha/docs/verify
  baseURL: https://www.google.com/recaptcha/api
  tags:
  - reCAPTCHA V3
  - Token Validation
  - Verification
  properties:
  - type: Documentation
    url: https://developers.google.com/recaptcha/docs/verify
name: Google reCAPTCHA
tags:
- Abuse Prevention
- Bot Detection
- CAPTCHA
- Fraud Prevention
- Google Cloud
- Security
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google reCAPTCHA is a security service that protects websites and applications from spam and abuse by verifying that interactions are from real humans rather than bots, offering Enterprise and standard APIs for site verification and risk assessment.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

