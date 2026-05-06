---
aid: acquia
url: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/apis.yml
apis:
  - aid: acquia:acquia-cloud-api
    name: Acquia Cloud API
    tags:
      - Applications
      - Cloud
      - Drupal
      - Environments
      - Hosting
    humanURL: https://cloudapi-docs.acquia.com/
    properties:
      - type: Documentation
        url: https://cloudapi-docs.acquia.com/
      - type: OpenAPI
        url: openapi/acquia-cloud-openapi.yml
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/openapi/acquia-cloud-applications.yml
        title: Acquia Applications API
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/openapi/acquia-cloud-environments.yml
        title: Acquia Environments API
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/openapi/acquia-cloud-organizations.yml
        title: Acquia Organizations API
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/openapi/acquia-cloud-account.yml
        title: Acquia Account API
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/openapi/acquia-cloud-subscriptions.yml
        title: Acquia Subscriptions API
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/openapi/acquia-cloud-teams-and-permissions.yml
        title: Acquia Teams And Permissions API
      - type: NaftikoCapability
        url: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/capabilities/shared/acquia-cloud-applications.yaml
    description: The Acquia Cloud API is a powerful tool that allows developers to programmatically interact with Acquia's cloud hosting platform. This API enables users to automate tasks, manage infrastructure, and deploy applications with ease. With the Acquia Cloud API, developers can create custom scripts and applications to streamline workflows, monitor performance, and scale resources as needed.
  - aid: acquia:acquia-cloud-site-factory-api
    name: Acquia Cloud Site Factory API
    tags:
      - Cloud
      - Drupal
      - Multisite
      - Site Factory
    humanURL: https://dev.acquia.com/api-documentation/acquia-cloud-site-factory-api
    properties:
      - type: Documentation
        url: https://docs.acquia.com/site-factory/extend/api
    description: Acquia Cloud Site Factory API is a powerful tool that allows developers to manage, customize, and automate various aspects of their websites and digital experiences. With this API, users can programmatically create and modify websites, manage content, and streamline deployment processes. By providing a flexible and scalable interface, Acquia Cloud Site Factory API enables developers to efficiently build and maintain multiple websites in a centralized platform.
  - aid: acquia:acquia-content-hub-api
    name: Acquia Content Hub API
    tags:
      - Content
      - Content Hub
      - Drupal
      - Syndication
    humanURL: https://dev.acquia.com/api-documentation/acquia-content-hub-api
    properties:
      - type: Documentation
        url: https://docs.acquia.com/drupal-starter-kits/add-ons/content-hub/api
    description: The Acquia Content Hub API is a powerful tool that allows users to easily distribute and share content across multiple websites and digital channels. By leveraging this API, content managers can automate the process of importing, exporting, and synchronizing content between various platforms, saving time and effort. Additionally, the API enables users to gain valuable insights into content performance and engagement metrics, helping to optimize content strategy and drive better results.
name: Acquia
tags:
  - Content
  - Experience
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://www.acquia.com/partners
    name: Work with a Partner | Acquia
    type: Partners
    description: 'null'
  - url: https://www.acquia.com/blog
    name: The Acquia Blog | Acquia
    type: Blog
    description: 'null'
  - url: https://www.acquia.com/events/online
    name: Register for Upcoming and Recorded Webinars | Acquia
    type: Webinars
    description: 'null'
  - url: https://www.acquia.com/support/acquia-training-certification
    name: Acquia Training & Certification | Acquia
    type: Certifications
    description: 'null'
  - url: https://dev.acquia.com/
    name: Acquia Developer Portal Homepage
    type: Portal
    description: 'null'
  - url: https://dev.acquia.com/tutorial
    name: Acquia Developer Portal Tutorials
    type: Tutorials
    description: 'null'
  - url: https://docs.acquia.com/service-offerings/support/support-users-guide#contacting-acquia-support
    name: Support Users Guide | Service Offerings | Acquia Product Documentation
    type: Support
    description: 'null'
  - url: https://status.acquia.com/
    name: Acquia, Inc. Status
    type: StatusPage
    description: 'null'
  - type: GitHubOrganization
    url: https://github.com/acquia
  - type: CLI
    url: https://github.com/acquia/cli
    title: Acquia CLI
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/rules/acquia-spectral-rules.yml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/capabilities/drupal-application-management.yaml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/vocabulary/acquia-vocabulary.yaml
  - type: TermsOfService
    url: https://www.acquia.com/about-us/legal
  - type: SignUp
    url: https://accounts.acquia.com/register
  - type: Features
    data:
      - name: Cloud Hosting
        description: Managed Drupal hosting on Acquia Cloud with auto-scaling, CDN, and DDoS protection.
      - name: Application Management
        description: Programmatic management of Drupal applications, environments, and deployments via Cloud API.
      - name: Multi-Site Factory
        description: Acquia Cloud Site Factory for managing hundreds of Drupal sites from a centralized platform.
      - name: Content Syndication
        description: Acquia Content Hub for distributing and synchronizing Drupal content across multiple sites.
      - name: Cloud IDE
        description: Browser-based Cloud IDE for remote Drupal development with pre-configured environments.
      - name: OAuth2 Authentication
        description: Secure API access via OAuth2 authorization code flow with scoped tokens.
  - type: UseCases
    data:
      - name: Automated Deployment Pipelines
        description: Integrate Acquia Cloud API into CI/CD pipelines for automated code deployment and cache clearing.
      - name: Multi-Environment Management
        description: Manage dev, staging, and production Drupal environments programmatically.
      - name: Platform Administration
        description: Automate team provisioning, SSH key management, and organizational access control.
      - name: Content Distribution
        description: Use Content Hub API to distribute content across a network of Drupal sites.
      - name: Headless Drupal
        description: Manage decoupled Drupal applications with Next.js or other frontend frameworks via Acquia APIs.
  - type: Integrations
    data:
      - name: Drupal CMS
        description: Native Drupal module integrations for Acquia Cloud, Content Hub, and Site Studio.
      - name: GitHub Actions
        description: GitHub Actions workflows for Acquia Cloud deployment automation using Acquia CLI.
      - name: Next.js
        description: Headless Drupal with Next.js using Acquia CMS headless starter kit.
      - name: Acquia DAM
        description: Digital Asset Management integration via Widen Collective for media management in Drupal.
created: '2025-02-17'
modified: '2026-04-19'
position: Consumer
description: Acquia is a leading provider of digital experience management solutions for organizations looking to enhance their online presence. They offer a range of services, including cloud hosting, digital asset management, and content management, to help businesses create, manage, and optimize their websites and digital experiences.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
