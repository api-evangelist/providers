---
aid: banuba
url: https://raw.githubusercontent.com/api-evangelist/banuba/refs/heads/main/apis.yml
name: Banuba
tags:
  - AR
  - Augmented Reality
  - Beauty
  - Face Recognition
  - Facial
  - SDK
  - Video
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-16'
modified: '2026-04-21'
position: Consuming
description: Banuba is an AR and AI technology company providing the Face AR SDK for augmented reality face effects, beauty filters, and virtual try-on experiences. The SDK supports iOS, Android, Web (HTML5), Windows, macOS, Unity, Flutter, and React Native. Use cases include live streaming beauty filters, video conferencing face effects, selfie editing, virtual makeup try-on, and face tracking for interactive applications.
apis:
  - aid: banuba:face-ar-sdk
    name: Banuba Face AR SDK
    tags:
      - AR
      - Augmented Reality
      - Beauty Filters
      - Face Effects
      - Face Tracking
      - Virtual Try-On
    humanURL: https://docs.banuba.com/far-sdk/
    properties:
      - url: https://docs.banuba.com/far-sdk/
        type: Documentation
      - url: https://www.banuba.com/augmented-reality-sdk
        type: Website
      - url: https://github.com/Banuba
        type: GitHub
    description: The Banuba Face AR SDK provides AR face effects, beauty filters, and face tracking for mobile (iOS/Android), web, and desktop applications. The SDK includes real-time face detection, 3D face tracking, background segmentation, and a library of customizable AR effects and beauty filters. Integration is via native SDK rather than REST API. Tracks up to 9 faces simultaneously.
  - aid: banuba:video-editor-sdk
    name: Banuba Video Editor SDK
    tags:
      - Video Editing
      - AI
      - White-Label
      - SDK
    humanURL: https://www.banuba.com/video-editor-sdk
    properties:
      - url: https://docs.banuba.com/ve-sdk/
        type: Documentation
      - url: https://www.banuba.com/video-editor-sdk
        type: Website
    description: Banuba Video Editor SDK is a complete white-label video and photo editing solution for iOS and Android with AI features including auto-clipping, captions, beauty filters, AR effects, and music integration.
  - aid: banuba:face-liveness-sdk
    name: Banuba Face Liveness SDK
    tags:
      - Liveness Detection
      - Biometrics
      - Security
      - Identity Verification
    humanURL: https://www.banuba.com/face-liveness
    properties:
      - url: https://docs.banuba.com/face-liveness/
        type: Documentation
      - url: https://www.banuba.com/face-liveness
        type: Website
    description: Banuba Face Liveness SDK provides anti-spoofing technology that verifies a face is real and present in real time, used for identity verification and access control.
common:
  - type: Website
    url: https://www.banuba.com/
    name: Banuba
  - type: Documentation
    url: https://docs.banuba.com/
    name: Banuba SDK Documentation
  - type: Documentation
    url: https://docs.banuba.com/far-sdk/
    name: Face AR SDK Docs
  - type: GitHub
    url: https://github.com/Banuba
    name: Banuba GitHub
  - type: Blog
    url: https://www.banuba.com/blog
    name: Banuba Blog
  - type: PrivacyPolicy
    url: https://www.banuba.com/privacy-policy
    name: Privacy Policy
  - type: SpectralRules
    url: rules/banuba-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/banuba-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/face-ar.yaml
  - type: JSON-LD
    url: json-ld/banuba-context.jsonld
  - name: Features
    type: Features
    data:
      - name: Face AR Effects
        description: Real-time AR face masks, filters, and accessories for live and recorded video.
      - name: Beauty Filters
        description: Skin smoothing, face reshaping, eye enlargement, and makeup filters.
      - name: 3D Face Tracking
        description: Precise 3D face landmark tracking for accurate AR effect placement.
      - name: Background Segmentation
        description: Real-time background removal and replacement for video calls.
      - name: Virtual Try-On
        description: Virtual makeup, glasses, hair color, and accessory try-on experiences.
      - name: AI Face Detection
        description: ML-powered face detection with age, gender, and emotion analysis.
      - name: Cross-Platform SDK
        description: Native SDKs for iOS, Android, Web, Windows, macOS, Unity, Flutter, and React Native.
      - name: Custom Effects Builder
        description: Banuba Effect Player for creating custom AR effects without coding.
  - name: Use Cases
    type: UseCases
    data:
      - name: Live Streaming Beauty Filters
        description: Real-time beauty and AR filters for live streaming platforms.
      - name: Video Conferencing
        description: Face effects and background segmentation for video call applications.
      - name: Selfie and Photo Editing
        description: Beauty retouching and AR effects for mobile photo editing apps.
      - name: Virtual Makeup Try-On
        description: AI-powered virtual makeup try-on for beauty e-commerce.
      - name: Face Authentication
        description: Face-based liveness detection and verification for security applications.
      - name: Gaming and Entertainment
        description: Face-tracked AR avatars and character animation for games.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
