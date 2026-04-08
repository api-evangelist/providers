---
aid: google-firebase
url: https://raw.githubusercontent.com/api-evangelist/google-firebase/refs/heads/main/apis.yml
apis:
- name: Firebase Realtime Database API
  description: The Firebase Realtime Database API provides RESTful access to Firebase's cloud-hosted NoSQL database. It enables developers to store and sync data in real time across all connected clients using JSON. The API supports reading, writing, updating, and deleting data, along with server-sent events for real-time streaming and query filtering.
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://firebase.google.com/docs/database
  baseURL: https://firebaseio.com
  tags:
  - Database
  - JSON
  - NoSQL
  - Real-Time
  properties:
  - type: Documentation
    url: https://firebase.google.com/docs/reference/rest/database
  - type: OpenAPI
    url: openapi/firebase-realtime-database-openapi.yml
  - type: JSONSchema
    url: json-schema/google-firebase-database-node-schema.json
- name: Firebase Cloud Messaging API (FCM)
  description: The Firebase Cloud Messaging API enables developers to send notifications and data messages to client apps on Android, iOS, and the web. The HTTP v1 API provides per-platform message customization, topic messaging, device group messaging, and delivery tracking. It uses OAuth 2.0 for authentication and supports both notification and data payloads.
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://firebase.google.com/docs/cloud-messaging
  baseURL: https://fcm.googleapis.com
  tags:
  - Messaging
  - Mobile
  - Push Notifications
  properties:
  - type: Documentation
    url: https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages
  - type: OpenAPI
    url: openapi/firebase-cloud-messaging-openapi.yml
  - type: JSONSchema
    url: json-schema/google-firebase-fcm-message-schema.json
- name: Firebase Authentication REST API
  description: The Firebase Authentication REST API enables developers to manage user authentication using email/password, phone, and federated identity providers such as Google, Facebook, and Apple. The API supports creating and signing in users, verifying tokens, managing user accounts, sending verification emails, and password resets through the Identity Toolkit endpoints.
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://firebase.google.com/docs/auth
  baseURL: https://identitytoolkit.googleapis.com
  tags:
  - Authentication
  - Identity
  - Users
  properties:
  - type: Documentation
    url: https://firebase.google.com/docs/reference/rest/auth
- name: Firebase Hosting REST API
  description: The Firebase Hosting REST API allows developers to programmatically manage web hosting deployments on Firebase. It supports creating new releases, managing site versions, uploading files, configuring custom domains, and managing release channels for preview deployments.
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://firebase.google.com/docs/hosting
  baseURL: https://firebasehosting.googleapis.com
  tags:
  - Deployment
  - Hosting
  - Web
  properties:
  - type: Documentation
    url: https://firebase.google.com/docs/reference/hosting/rest
- name: Firebase Remote Config API
  description: The Firebase Remote Config API enables developers to change the behavior and appearance of their apps without requiring users to download an update. The API allows publishing new Remote Config templates, managing conditions and parameters, and rolling back to previous configurations.
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://firebase.google.com/docs/remote-config
  baseURL: https://firebaseremoteconfig.googleapis.com
  tags:
  - Configuration
  - Feature Flags
  - Remote Config
  properties:
  - type: Documentation
    url: https://firebase.google.com/docs/reference/remote-config/rest
name: Google Firebase
tags:
- Analytics
- Authentication
- Backend as a Service
- Cloud Messaging
- Google Cloud
- Hosting
- Mobile
- Real-Time Database
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google Firebase is a comprehensive app development platform that provides backend services, SDKs, and APIs for building and scaling mobile and web applications, including authentication, real-time databases, cloud messaging, hosting, and analytics.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

