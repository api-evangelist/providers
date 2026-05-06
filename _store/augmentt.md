---
aid: augmentt
name: Augmentt
description: |
  Augmentt is a multi-tenant SaaS management platform built for managed service providers (MSPs). It provides SaaS discovery (Shadow IT), license optimization, usage tracking, spend management, and SaaS security policy enforcement across Microsoft 365 and cloud applications. Augmentt integrates with major PSA and RMM platforms including ConnectWise and N-able.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - MSP
  - Microsoft 365
  - SaaS Management
  - SaaS Security
  - Shadow IT
url: https://raw.githubusercontent.com/api-evangelist/augmentt/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: augmentt:augmentt-discover
    name: Augmentt Discover
    description: |
      Augmentt Discover provides SaaS discovery and Shadow IT detection capabilities for MSPs, identifying all cloud applications used across managed client environments.
    humanURL: https://www.augmentt.com/the-tools-you-need-to-offer-saas-admin-services/
    baseURL: https://www.augmentt.com
    tags:
      - Discovery
      - MSP
      - SaaS
      - Shadow IT
    properties:
      - type: Documentation
        url: https://www.augmentt.com/the-tools-you-need-to-offer-saas-admin-services/
  - aid: augmentt:augmentt-optimize
    name: Augmentt Optimize
    description: |
      Augmentt Optimize tracks SaaS usage and spend across client environments to identify unused licenses, redundant applications, and cost savings opportunities for MSPs.
    humanURL: https://www.augmentt.com/the-tools-you-need-to-offer-saas-admin-services/
    baseURL: https://www.augmentt.com
    tags:
      - License Management
      - MSP
      - SaaS
      - Spend Management
    properties:
      - type: Documentation
        url: https://www.augmentt.com/the-tools-you-need-to-offer-saas-admin-services/
  - aid: augmentt:augmentt-engage
    name: Augmentt Engage
    description: |
      Augmentt Engage provides SaaS administration, management, and automation capabilities allowing MSPs to centralize SaaS security policy enforcement and user lifecycle management across Microsoft 365 and cloud apps.
    humanURL: https://www.augmentt.com/user-management/
    baseURL: https://www.augmentt.com
    tags:
      - Automation
      - MSP
      - SaaS Security
      - User Management
    properties:
      - type: Documentation
        url: https://www.augmentt.com/user-management/
common:
  - type: Website
    url: https://www.augmentt.com
  - type: Documentation
    url: https://www.augmentt.com/resources
  - type: Integrations
    data:
      - name: ConnectWise
        description: Native integration with ConnectWise PSA for automated ticketing and billing based on SaaS discovery and license data.
      - name: N-able
        description: Integration with N-able RMM for combined endpoint and SaaS management visibility for MSPs.
      - name: Microsoft 365
        description: Deep integration with Microsoft 365 tenant data for SaaS license, usage, and security policy management.
      - name: CloudRadial
        description: Augmentt data surfaced in CloudRadial customer portal for self-service SaaS app visibility.
  - type: Features
    data:
      - name: Multi-Tenant Management
        description: Manage SaaS applications across multiple client tenants from a single MSP dashboard with hierarchical access control.
      - name: SaaS Discovery
        description: Automatically discover all cloud applications in use across client environments including Shadow IT not approved by IT.
      - name: License Optimization
        description: Track license utilization, identify unused seats, and generate recommendations to reduce SaaS spend across clients.
      - name: SaaS Security Policies
        description: Enforce security policies across SaaS applications including MFA requirements, conditional access, and app permissions.
      - name: User Lifecycle Management
        description: Automate user onboarding and offboarding across SaaS applications when employees join or leave client organizations.
      - name: PSA Integration
        description: Integrate discovery and optimization data with PSA platforms for automated billing and service delivery.
  - type: UseCases
    data:
      - name: SaaS Spend Management
        description: Identify and eliminate wasted SaaS spend by discovering unused licenses and redundant applications across client portfolios.
      - name: Shadow IT Control
        description: Detect and manage unsanctioned cloud applications to reduce security risk and enforce acceptable use policies.
      - name: Microsoft 365 Management
        description: Manage M365 licenses, security settings, and user access across all client tenants from a unified MSP console.
      - name: Employee Offboarding
        description: Automate secure offboarding of departing employees by revoking access to all SaaS applications simultaneously.
  - type: Solutions
    data:
      - name: MSP SaaS Management Service
        description: Package and deliver SaaS management as a managed service offering including discovery, optimization, and security monitoring.
      - name: Microsoft 365 Security
        description: Extend M365 security posture management with SaaS-specific controls, policy enforcement, and compliance reporting.
  - type: PrivacyPolicy
    url: https://www.augmentt.com/privacy-policy/
  - type: TermsOfService
    url: https://www.augmentt.com/terms-of-service/
  - type: Contact
    url: https://www.augmentt.com/contact/
  - type: Blog
    url: https://www.augmentt.com/blog/
  - type: SignUp
    url: https://www.augmentt.com/free-trial/
  - type: Pricing
    url: https://www.augmentt.com/pricing/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
