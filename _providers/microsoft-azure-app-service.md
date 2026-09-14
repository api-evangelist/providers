---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Microsoft Azure App Service Agentic Access
  operation_count: 7
  slug: microsoft-azure-app-service-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 2
apis:
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Operations operations
  name: Microsoft Azure App Service Operations API
  slug: microsoft-azure-app-service-operations-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Web Apps operations
  name: Microsoft Azure App Service Web Apps API
  slug: microsoft-azure-app-service-web-apps-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure App Service REST Operations API
  slug: open-microsoft-azure-app-service-operations-api
- collection_type: open
  name: Azure App Service REST Operations Web Apps API
  slug: open-microsoft-azure-app-service-web-apps-api
- collection_type: open
  name: Azure App Service REST API
  slug: open-microsoft-azure-app-service
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-app-service-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-app-service-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-app-service-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-app-service-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/app-service/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: agent
  title: ''
  type: LlmsText
  url: https://portal.azure.com/llms.txt
created: '2026-03-13'
description: Microsoft Azure App Service is a fully managed platform-as-a-service (PaaS) for building, deploying, and scaling web apps, REST APIs, and mobile backends. It supports multiple languages and frameworks, offers built-in auto-scaling and load balancing, and includes integrated authentication, continuous deployment, custom domain, and SSL certificate management.
finops:
- name: Microsoft Azure App Service Finops
  service_category: API
  slug: microsoft-azure-app-service-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-app-service.png
layout: provider
modified: '2026-05-19'
name: Microsoft Azure App Service
nav: Providers
network: true
overview: 'Microsoft Azure App Service publishes 2 APIs on the [APIs.io](https://apis.io/) network: Operations API and Web Apps API. Tagged areas include App Service, Hosting, Microsoft Azure, Platform-as-a-Service, and Web App.


  Microsoft Azure App Service''s developer surface includes authentication, developer portal, documentation, pricing, support, and 8 more developer resources.'
plans:
- name: Microsoft Azure App Service Plans Pricing
  plan_count: 3
  slug: microsoft-azure-app-service-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Microsoft Azure App Service Rate Limits
  slug: microsoft-azure-app-service-rate-limits
scopes:
- name: Microsoft Azure App Service Scopes
  scope_count: 1
  slug: microsoft-azure-app-service-scopes
  summary_line: 1 scope · implicit
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-app-service/refs/heads/main/screenshots/microsoft-azure-app-service-2026-06-20T185356.png
security:
- kind: authentication
  name: Microsoft Azure App Service Authentication
  slug: microsoft-azure-app-service-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure App Service Domain Security
  slug: microsoft-azure-app-service-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-app-service
tags:
- App Service
- Hosting
- Microsoft Azure
- Platform-as-a-Service
- Web App
website: https://portal.azure.com/
---
