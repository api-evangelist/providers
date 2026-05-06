---
aid: beamer
name: Beamer
description: Beamer is a changelog and notification center tool for announcing product updates, new features, and API changes to end users. It provides an embeddable feed widget, push notifications, email digests, and a public changelog page. The Beamer REST API enables programmatic management of posts, users, segments, and notification delivery. Beamer is now part of the Userflow product suite. The API uses API key authentication and supports OpenAPI specifications and Postman collections.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Changelog
  - Deprecation
  - Notifications
  - Product Updates
  - User Engagement
url: https://raw.githubusercontent.com/api-evangelist/beamer/refs/heads/main/apis.yml
created: '2026-03-29'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: beamer:beamer
    name: Beamer API
    description: The Beamer REST API provides programmatic access to changelog posts, user management, segmentation, and notification feeds. Key endpoints include unread count retrieval, post creation and management, user profile updates, and segment management. Authentication uses an API key from Beamer settings.
    humanURL: https://www.getbeamer.com/api
    tags:
      - Changelog
      - Notifications
      - Product Updates
    properties:
      - type: Documentation
        url: https://www.getbeamer.com/api
      - type: APIReference
        url: https://www.getbeamer.com/api
      - type: Authentication
        url: https://www.getbeamer.com/api
common:
  - type: Website
    url: https://www.getbeamer.com/
  - type: Documentation
    url: https://www.getbeamer.com/api
  - type: GettingStarted
    url: https://www.getbeamer.com/help/how-to-install-beamer-using-our-api
  - type: StatusPage
    url: https://status.getbeamer.com
  - type: Integrations
    url: https://apps.make.com/beamer
    title: Make (Integromat) Integration
  - type: Features
    data:
      - name: Changelog Feed Widget
        description: Embeddable changelog widget that displays product updates to users within your application.
      - name: Push Notifications
        description: In-app push notifications to alert users about new features and product updates.
      - name: Email Digests
        description: Automated email digest delivery of changelog posts to user segments.
      - name: User Segmentation
        description: Target changelog announcements and notifications to specific user segments based on attributes.
      - name: Unread Count API
        description: REST API endpoint to retrieve unread notification count for individual users.
      - name: Public Changelog
        description: Hosted public changelog page for external users, prospects, and documentation.
  - type: UseCases
    data:
      - name: Product Update Announcements
        description: Announce new product features, improvements, and bug fixes to end users via in-app notifications.
      - name: API Changelog
        description: Maintain a dedicated API changelog for developers tracking breaking changes, deprecations, and new endpoints.
      - name: User Onboarding
        description: Surface new features to relevant users through targeted notifications and changelog posts.
      - name: Release Notes Automation
        description: Automate release note publishing from CI/CD pipelines using the Beamer API.
  - type: Integrations
    data:
      - name: Zapier
        description: Automation integration connecting Beamer with thousands of apps via Zapier workflows.
      - name: Segment
        description: Customer data platform integration for sending Beamer user events and changelog views to Segment.
      - name: Intercom
        description: Customer messaging platform integration enabling Beamer notifications alongside Intercom conversations.
      - name: ActiveCampaign
        description: Email marketing integration for delivering Beamer changelog digests through ActiveCampaign.
      - name: WordPress
        description: WordPress plugin for embedding Beamer changelog feed in WordPress websites.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
