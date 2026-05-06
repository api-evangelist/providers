---
aid: apiable
name: Apiable
description: Apiable is an API portal platform that enables businesses to create single-tenant, white-label developer portals with custom domains, branding, and API product management. It supports API monetization, developer self-service onboarding, usage metrics, subscription lifecycle management, and integrates with API gateways including Amazon API Gateway and Kong.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Amazon API Gateway
  - API Gateway
  - API Monetization
  - API Portal
  - Developer Experience
  - Developer Portal
  - Kong
  - Platform
  - Self-Service
url: https://raw.githubusercontent.com/api-evangelist/apiable/refs/heads/main/apis.yml
created: '2025-01-08'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: apiable:api-portal-platform
    name: Apiable API Portal Platform
    description: Apiable provides a self-service API portal platform for API product managers and developers. It offers single-tenant dedicated portals with custom domains, automated API documentation with try-out functionality, developer onboarding, subscription management, usage dashboards, and role-based access control integrated with existing API gateways.
    humanURL: https://www.apiable.io/platform/api-portal
    tags:
      - API Gateway
      - API Portal
      - Developer Experience
      - Developer Portal
      - Monetization
    properties:
      - type: Documentation
        url: https://www.apiable.io/platform/api-portal
      - type: Pricing
        url: https://www.apiable.io/pricing
common:
  - type: Website
    url: https://www.apiable.io/
  - type: Pricing
    url: https://www.apiable.io/pricing
  - type: Blog
    url: https://www.apiable.io/resources
  - type: Features
    data:
      - name: API Portal Generation
        description: Single-tenant dedicated portals with custom domains, branding, logos, and CSS whitelabeling.
      - name: API Product Management
        description: Bundle APIs into products and plans with monetization options and subscription lifecycle management.
      - name: Auto-Generated API Documentation
        description: Automatically generate API documentation from specs with interactive try-out functionality and code samples.
      - name: Developer Self-Service Onboarding
        description: Self-service account creation, API subscription, and credential generation for developers.
      - name: Usage Metrics and Dashboards
        description: Real-time API consumption tracking and usage dashboards for developers and administrators.
      - name: Role-Based Access Control
        description: Team access control with role-based permissions and shared API credential management.
      - name: Google Tag Manager Integration
        description: Deploy analytics and tracking tags via Google Tag Manager integration in developer portals.
  - type: UseCases
    data:
      - name: Partner API Onboarding
        description: Streamline partner API access with self-service portals and automated credential provisioning.
      - name: API Product Monetization
        description: Implement usage-based billing and subscription plans for API product revenue generation.
      - name: Developer Self-Service Portals
        description: Create branded developer portals where consumers can discover, subscribe to, and manage API access independently.
      - name: API Adoption Scaling
        description: Scale API adoption by reducing onboarding friction through self-service workflows and automated access management.
  - type: Integrations
    data:
      - name: Amazon API Gateway
        description: Native integration with Amazon API Gateway for managing API products and subscriptions.
      - name: Kong
        description: Integration with Kong API Gateway for portal-driven API access management.
      - name: Google Tag Manager
        description: Deploy analytics, tracking, and marketing tags into developer portals via Google Tag Manager.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
