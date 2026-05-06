---
aid: google-android
name: Google Android
description: Android is a mobile operating system developed by Google, based on a modified version of the Linux kernel and other open-source software. It powers billions of devices worldwide including smartphones, tablets, TVs, and wearables.
type: Index
image: https://www.android.com/static/images/logos/android-logo.png
url: https://raw.githubusercontent.com/api-evangelist/google-android/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-18'
access: 3rd-Party
specificationVersion: '0.19'
tags:
  - Android
  - Google
  - Mobile Development
  - Mobile Operating System
  - Open Source
apis:
  - aid: google-android:android-management-api
    name: Android Management API
    description: The Android Management API provides remote enterprise management of Android devices by creating and managing policies that control device behavior and apps.
    image: https://www.gstatic.com/devrel-devsite/prod/v2ff77c87c709f3e5e323c03865ecedf5b4afc4446d0e0e2904abf9d5/android/images/touchicon-180.png
    humanURL: https://developers.google.com/android/management
    baseURL: https://androidmanagement.googleapis.com
    tags:
      - Device Management
      - Enterprise
      - MDM
      - Policies
    properties:
      - type: Documentation
        url: https://developers.google.com/android/management/reference/rest
      - type: OpenAPI
        url: https://androidmanagement.googleapis.com/$discovery/rest?version=v1
      - type: Authentication
        url: https://developers.google.com/android/management/authentication
  - aid: google-android:google-play-developer-api
    name: Google Play Developer API
    description: The Google Play Developer API allows you to perform a number of publishing and app-management tasks including managing in-app purchases and subscriptions.
    image: https://play-lh.googleusercontent.com/BJIR7aQ3sMO0JlxdVcX_Wy8mMv-Inh8J9t3i-ARE6M9aKqBKPDxQMr1JkEALvMECEXRM
    humanURL: https://developers.google.com/android-publisher
    baseURL: https://androidpublisher.googleapis.com
    tags:
      - In-App Purchases
      - Play Store
      - Publishing
      - Subscriptions
    properties:
      - type: Documentation
        url: https://developers.google.com/android-publisher/api-ref/rest
      - type: OpenAPI
        url: https://androidpublisher.googleapis.com/$discovery/rest?version=v3
      - type: Getting Started
        url: https://developers.google.com/android-publisher/getting_started
  - aid: google-android:firebase-cloud-messaging-api
    name: Firebase Cloud Messaging API
    description: Firebase Cloud Messaging (FCM) is a cross-platform messaging solution that lets you reliably send messages to Android devices at no cost.
    image: https://firebase.google.com/images/social.png
    humanURL: https://firebase.google.com/docs/cloud-messaging
    baseURL: https://fcm.googleapis.com
    tags:
      - Cloud Messaging
      - Firebase
      - Messaging
      - Push Notifications
    properties:
      - type: Documentation
        url: https://firebase.google.com/docs/cloud-messaging/server
      - type: OpenAPI
        url: https://fcm.googleapis.com/$discovery/rest?version=v1
      - type: SDK
        url: https://firebase.google.com/docs/cloud-messaging/android/client
  - aid: google-android:google-play-games-services-api
    name: Google Play Games Services API
    description: The Google Play Games Services API enables games to integrate with features like achievements, leaderboards, and multiplayer gaming.
    image: https://play-lh.googleusercontent.com/BJIR7aQ3sMO0JlxdVcX_Wy8mMv-Inh8J9t3i-ARE6M9aKqBKPDxQMr1JkEALvMECEXRM
    humanURL: https://developers.google.com/games/services
    baseURL: https://www.googleapis.com/games/v1
    tags:
      - Achievements
      - Gaming
      - Leaderboards
      - Multiplayer
    properties:
      - type: Documentation
        url: https://developers.google.com/games/services/web/api/rest
      - type: OpenAPI
        url: https://www.googleapis.com/discovery/v1/apis/games/v1/rest
      - type: SDK
        url: https://developers.google.com/games/services/android/quickstart
  - aid: google-android:android-device-provisioning-partner-api
    name: Android Device Provisioning Partner API
    description: The Android Device Provisioning Partner API allows device resellers and enterprise mobility management providers to programmatically manage zero-touch enrollment for enterprise Android devices, including creating customers, claiming devices, and managing device metadata.
    image: https://www.gstatic.com/devrel-devsite/prod/v2ff77c87c709f3e5e323c03865ecedf5b4afc4446d0e0e2904abf9d5/android/images/touchicon-180.png
    humanURL: https://developers.google.com/zero-touch
    baseURL: https://androiddeviceprovisioning.googleapis.com
    tags:
      - Device Provisioning
      - Enterprise
      - Reseller
      - Zero-Touch Enrollment
    properties:
      - type: Documentation
        url: https://developers.google.com/zero-touch/reference/reseller/rest
      - type: Getting Started
        url: https://developers.google.com/zero-touch/guides/overview
  - aid: google-android:android-over-the-air-api
    name: Android Over the Air API
    description: The Android Over the Air API provides the infrastructure used by the Android partner portal for managing device system updates, including deployments, configurations, groups, and packages.
    image: https://www.gstatic.com/devrel-devsite/prod/v2ff77c87c709f3e5e323c03865ecedf5b4afc4446d0e0e2904abf9d5/android/images/touchicon-180.png
    humanURL: https://developers.google.com/android/over-the-air/reference/rest
    baseURL: https://androidovertheair.googleapis.com
    tags:
      - Device Updates
      - Firmware
      - OTA Updates
      - System Updates
    properties:
      - type: Documentation
        url: https://developers.google.com/android/over-the-air/reference/rest
      - type: OpenAPI
        url: https://androidovertheair.googleapis.com/$discovery/rest?version=v1
      - type: Authentication
        url: https://developers.google.com/android/over-the-air/v1/how-tos/authorizing
  - aid: google-android:google-play-emm-api
    name: Google Play EMM API
    description: The Google Play EMM API enables enterprise mobility management providers to manage the distribution of Android apps and configurations to enterprise users and devices. This API is no longer accepting new registrations but remains available for existing integrations.
    image: https://www.gstatic.com/devrel-devsite/prod/v2ff77c87c709f3e5e323c03865ecedf5b4afc4446d0e0e2904abf9d5/android/images/touchicon-180.png
    humanURL: https://developers.google.com/android/work/play/emm-api/
    baseURL: https://androidenterprise.googleapis.com
    tags:
      - App Management
      - EMM
      - Enterprise
      - Enterprise Mobility
    properties:
      - type: Documentation
        url: https://developers.google.com/android/work/play/emm-api/v1
      - type: Getting Started
        url: https://developers.google.com/android/work/play/emm-api/getstarted
  - aid: google-android:play-integrity-api
    name: Play Integrity API
    description: The Play Integrity API helps protect your apps and games from potentially risky and fraudulent interactions by checking that interactions and server requests are coming from your genuine app binary running on a genuine Android device.
    image: https://www.gstatic.com/devrel-devsite/prod/v2ff77c87c709f3e5e323c03865ecedf5b4afc4446d0e0e2904abf9d5/android/images/touchicon-180.png
    humanURL: https://developer.android.com/google/play/integrity
    baseURL: https://playintegrity.googleapis.com
    tags:
      - App Verification
      - Fraud Prevention
      - Integrity
      - Security
    properties:
      - type: Documentation
        url: https://developer.android.com/google/play/integrity/overview
      - type: Getting Started
        url: https://developer.android.com/google/play/integrity/standard
  - aid: google-android:cloud-testing-api
    name: Cloud Testing API
    description: The Cloud Testing API powers Firebase Test Lab, enabling developers to test Android and iOS apps on real and virtual devices hosted in Google data centers, including instrumentation tests and robo tests.
    image: https://firebase.google.com/images/social.png
    humanURL: https://firebase.google.com/docs/test-lab
    baseURL: https://testing.googleapis.com
    tags:
      - Firebase
      - Quality Assurance
      - Test Lab
      - Testing
    properties:
      - type: Documentation
        url: https://firebase.google.com/docs/test-lab/reference/testing/rest/
      - type: Getting Started
        url: https://firebase.google.com/docs/test-lab/android/get-started
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: Portal
    url: https://developers.android.com/
  - type: Blog
    url: https://android-developers.googleblog.com/
  - type: GitHubOrganization
    url: https://github.com/android
  - type: TermsOfService
    url: https://developers.google.com/terms
  - type: PrivacyPolicy
    url: https://policies.google.com/privacy
  - type: Support
    url: https://developer.android.com/support
  - type: Newsletter
    url: https://developer.android.com/newsletter
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/android
  - type: YouTube
    url: https://www.youtube.com/user/androiddevelopers
  - type: Support
    url: https://issuetracker.google.com/issues?q=componentid:192735
  - type: Training
    url: https://developer.android.com/courses
  - type: StatusPage
    url: https://status.cloud.google.com/
  - type: Features
    data:
      - name: Enterprise Device Management
        description: Remotely manage and configure Android devices with policies for enterprise mobility.
      - name: App Publishing and Distribution
        description: Publish and manage Android apps on Google Play including in-app purchases and subscriptions.
      - name: Push Notifications
        description: Send cross-platform push notifications to Android devices via Firebase Cloud Messaging.
      - name: Play Integrity
        description: Verify that interactions come from genuine app binaries running on genuine Android devices.
      - name: Zero-Touch Enrollment
        description: Automate enterprise device provisioning and enrollment at scale.
      - name: Cloud Testing
        description: Test Android apps on real and virtual devices in Google data centers via Firebase Test Lab.
      - name: Game Services
        description: Integrate achievements, leaderboards, and multiplayer features into Android games.
      - name: Over-the-Air Updates
        description: Manage system updates and firmware deployments for Android device fleets.
  - type: UseCases
    data:
      - name: Enterprise Mobility Management
        description: Deploy and manage corporate Android devices with security policies and app distribution.
      - name: App Store Management
        description: Automate app publishing, pricing, and subscription management on Google Play.
      - name: User Engagement
        description: Drive user engagement with push notifications, in-app messages, and game achievements.
      - name: Device Fleet Management
        description: Manage large fleets of Android devices for retail, logistics, or field operations.
      - name: App Quality Assurance
        description: Automate testing of Android apps across device configurations using Cloud Testing.
  - type: Integrations
    data:
      - name: Firebase
        description: Integrate with Firebase for analytics, crashlytics, authentication, and cloud messaging.
      - name: Google Cloud
        description: Connect Android apps to Google Cloud services for storage, ML, and compute.
      - name: Google Play Console
        description: Manage app releases, testing tracks, and performance metrics through the Play Console.
      - name: Android Studio
        description: Develop and debug Android apps with the official IDE and its integrated tools.
      - name: Jetpack Libraries
        description: Use Android Jetpack libraries for architecture, UI, and behavior best practices.
---
