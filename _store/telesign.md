---
aid: telesign
name: Telesign
description: Telesign provides a comprehensive suite of communications and security APIs enabling businesses to verify phone numbers, send SMS and voice messages, and assess fraud risk. Core offerings include SMS messaging, voice calls, multi-channel verification (OTP/MFA), phone number intelligence (PhoneID), reputation scoring, and silent verification. Telesign serves thousands of enterprises globally for account security, fraud prevention, and customer communications.
url: https://raw.githubusercontent.com/api-evangelist/telesign/refs/heads/main/apis.yml
modified: '2026-05-03'
specificationVersion: '0.19'
tags:
  - Authentication
  - Communications
  - Fraud Prevention
  - Phone Intelligence
  - SMS
  - Verification
apis:
  - aid: telesign:sms-api
    name: Telesign SMS API
    description: Send SMS messages including alerts, notifications, reminders, marketing messages, and one-time passwords to phone numbers worldwide. Messages are classified by type (OTP, ARN, MKT) and provide delivery status tracking via reference IDs.
    humanURL: https://developer.telesign.com/enterprise/docs/sms-get-started
    baseURL: https://rest-ww.telesign.com/v1
    tags:
      - Alerts
      - Messaging
      - Notifications
      - OTP
      - SMS
    properties:
      - type: Documentation
        url: https://developer.telesign.com/enterprise/docs/sms-get-started
      - type: OpenAPI
        url: openapi/telesign-sms-openapi.yml
  - aid: telesign:phoneid-api
    name: Telesign PhoneID API
    description: Retrieve global phone number intelligence including carrier information, geographic location, phone type (mobile, landline, VoIP), and subscriber data. Used for fraud prevention, identity verification, and risk assessment during account creation and transactions.
    humanURL: https://developer.telesign.com/enterprise/docs/phoneid-api-overview
    baseURL: https://rest-ww.telesign.com/v1
    tags:
      - Carrier Data
      - Fraud Prevention
      - Identity Verification
      - Phone Intelligence
      - Risk Assessment
    properties:
      - type: Documentation
        url: https://developer.telesign.com/enterprise/docs/phoneid-api-overview
      - type: OpenAPI
        url: openapi/telesign-phoneid-openapi.yml
  - aid: telesign:verify-api
    name: Telesign Verify API
    description: Multi-channel phone-based verification and MFA. Send one-time passcodes via SMS, voice, WhatsApp, Viber, RCS, or email, and verify codes submitted by end users. Supports password reset, account creation verification, and login MFA flows.
    humanURL: https://developer.telesign.com/enterprise/docs/verify-api-overview
    baseURL: https://rest-ww.telesign.com/v1
    tags:
      - Authentication
      - MFA
      - OTP
      - Two-Factor Authentication
      - Verification
    properties:
      - type: Documentation
        url: https://developer.telesign.com/enterprise/docs/verify-api-overview
      - type: OpenAPI
        url: openapi/telesign-verify-openapi.yml
  - aid: telesign:score-api
    name: Telesign Score API
    description: Assess fraud risk for phone numbers using reputation scoring based on intelligence, traffic patterns, machine learning, and a global data consortium. Returns a risk level and numeric score with a recommended action (allow, flag, block).
    humanURL: https://developer.telesign.com/enterprise/docs/score-api-overview
    baseURL: https://rest-ww.telesign.com/v1
    tags:
      - Fraud Detection
      - Phone Intelligence
      - Risk Scoring
    properties:
      - type: Documentation
        url: https://developer.telesign.com/enterprise/docs/score-api-overview
      - type: OpenAPI
        url: openapi/telesign-score-openapi.yml
  - aid: telesign:voice-api
    name: Telesign Voice API
    description: Send voice messages including OTPs, alerts, and notifications to phone numbers worldwide. Supports text-to-speech message delivery and call status tracking.
    humanURL: https://developer.telesign.com/enterprise/docs/voice-get-started
    baseURL: https://rest-ww.telesign.com/v1
    tags:
      - OTP
      - Telecommunications
      - Voice
    properties:
      - type: Documentation
        url: https://developer.telesign.com/enterprise/docs/voice-get-started
common:
  - type: Website
    url: https://www.telesign.com/
  - type: Developer Portal
    url: https://developer.telesign.com/enterprise
  - type: Authentication
    url: https://developer.telesign.com/enterprise/docs/authentication
  - type: Status Page
    url: https://status.telesign.com/
  - type: Pricing
    url: https://www.telesign.com/pricing/
  - type: Terms of Service
    url: https://www.telesign.com/terms-conditions/
  - type: GitHub Organization
    url: https://github.com/TeleSign
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
