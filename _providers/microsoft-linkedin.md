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
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Microsoft Linkedin Agentic Access
  operation_count: 17
  slug: microsoft-linkedin-agentic-access
  summary_line: 17 operations · 8 acting
api_count: 8
apis:
- description: The LinkedIn Marketing API enables programmatic management of LinkedIn advertising campaigns, audience targeting, creative assets, and performance reporting. Developers can create sponsored content, m
  name: LinkedIn Marketing API
  slug: marketing-api
- description: 'The LinkedIn Consumer API provides access to member profiles, sign-in with LinkedIn, and content sharing capabilities. Developers can implement social sign-on, retrieve basic profile information, and '
  name: LinkedIn Consumer API
  slug: consumer-api
- description: The LinkedIn Talent Solutions API provides access to recruiting and talent management capabilities. It enables integration with applicant tracking systems, job posting management, candidate search, an
  name: LinkedIn Talent Solutions API
  slug: talent-solutions-api
- description: Manage ad accounts
  name: Microsoft LinkedIn AdAccounts API
  slug: microsoft-linkedin-adaccounts-api
- description: Manage ad account user permissions
  name: Microsoft LinkedIn AdAccountUsers API
  slug: microsoft-linkedin-adaccountusers-api
- description: Manage campaign groups
  name: Microsoft LinkedIn AdCampaignGroups API
  slug: microsoft-linkedin-adcampaigngroups-api
- description: Manage campaigns
  name: Microsoft LinkedIn AdCampaigns API
  slug: microsoft-linkedin-adcampaigns-api
- description: Manage creatives
  name: Microsoft LinkedIn AdCreatives API
  slug: microsoft-linkedin-adcreatives-api
artifact_total: 17
collections:
- collection_type: open
  name: LinkedIn Marketing API
  slug: open-microsoft-linkedin
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-linkedin-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-linkedin-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-linkedin-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-linkedin-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-linkedin-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/linkedin
- group: start
  title: ''
  type: Portal
  url: https://developer.linkedin.com/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/linkedin/
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/authentication
- group: operate
  title: ''
  type: RateLimits
  url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/rate-limits
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.linkedin.com/legal/l/api-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.linkedin.com/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.linkedin.com/help/linkedin
created: '2024-01-01'
description: LinkedIn, owned by Microsoft, provides APIs for accessing professional networking data, marketing and advertising capabilities, talent solutions, and consumer features including sign-in with LinkedIn.
finops:
- name: Microsoft Linkedin Finops
  service_category: API
  slug: microsoft-linkedin-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-linkedin.png
layout: provider
modified: '2026-04-28'
name: Microsoft LinkedIn
nav: Providers
network: true
overview: 'Microsoft LinkedIn publishes 5 APIs on the [APIs.io](https://apis.io/) network, including AdAccounts API, AdAccountUsers API, AdCampaignGroups API, and 2 more. Tagged areas include Marketing, Microsoft, Professional Networking, Recruiting, and Social Network.


  Microsoft LinkedIn''s developer surface includes authentication, developer portal, documentation, support, and 9 more developer resources.'
plans:
- name: Microsoft Linkedin Plans Pricing
  plan_count: 3
  slug: microsoft-linkedin-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 5
  name: Microsoft Linkedin Rate Limits
  slug: microsoft-linkedin-rate-limits
scopes:
- name: Microsoft Linkedin Scopes
  scope_count: 5
  slug: microsoft-linkedin-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: developing
  composite: 47.1
  delta: 3.2
  facets:
    commercial_clarity: 60.5
    contract_quality: 54.9
    developer_ergonomics: 32.6
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 43.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-linkedin/refs/heads/main/screenshots/microsoft-linkedin-2026-06-20T185506.png
security:
- kind: authentication
  name: Microsoft Linkedin Authentication
  slug: microsoft-linkedin-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Linkedin Domain Security
  slug: microsoft-linkedin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Linkedin Vulnerability Disclosure
  slug: microsoft-linkedin-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-linkedin
tags:
- Marketing
- Microsoft
- Professional Networking
- Recruiting
- Social Network
website: https://developer.linkedin.com/
---
