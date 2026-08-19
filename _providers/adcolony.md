---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.5
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 4
asyncapis:
- description: ''
  name: Adcolony V4Vc Webhooks
  slug: adcolony-v4vc-webhooks
common:
- group: operate
  title: ''
  type: Releases
  url: https://github.com/AdColony/AdColony-iOS-SDK/releases
- group: company
  title: ''
  type: Website
  url: https://www.adcolony.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AdColony
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/AdColony/AdColony-iOS-SDK
- group: build
  title: ''
  type: Packages
  url: packages/adcolony-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/adcolony-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/adcolony-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/adcolony-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adcolony-domain-security.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/adcolony-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/adcolony-v4vc-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/adcolony-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/adcolony-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/adcolony-conventions.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/adcolony-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/adcolony-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adcolony-llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/AdColony/AdColony-Android-SDK/wiki
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/AdColony/AdColony-Android-SDK/wiki/Project-Setup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.digitalturbine.com/legal/privacy-policy
coverage:
  checked: '2026-08-12'
  detail: AdColony was absorbed into Digital Turbine's DT Exchange, so every path on adcolony.com now 308-redirects to digitalturbine.com and the one HTTP API it shipped — the Publisher Reporting API v2.3 — survives only as a PDF link on a support host that no longer accepts connections.
  evidence:
  - status: 308
    url: https://www.adcolony.com/
  - status: 0
    url: https://support.adcolony.com/wp-content/uploads/2019/07/AdColony-Publisher-Reporting-API-v2.3_Nov222016.pdf
  - status: 200
    url: https://github.com/AdColony/AdColony-Android-SDK/wiki/Publisher-Reporting-API
  - status: 403
    url: https://adcolony-www-common.s3.amazonaws.com/Javadoc/4.8.0/index.html
  reason: defunct
  state: none
created: '2026-07-17'
description: AdColony was a mobile advertising and app-monetization company known for its high-definition video and interactive (Aurora HD) mobile ad SDKs and its Publisher and Advertiser reporting APIs. AdColony was acquired by Digital Turbine in 2021; adcolony.com and its developer support/docs hosts now 308-redirect to digitalturbine.com, so the historical reporting-API and helpdesk documentation is no longer served. The first-party AdColony mobile ads SDKs for iOS (CocoaPods) and Android (Maven Central) remain published, and the iOS SDK source remains archived on GitHub.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/adcolony.png
layout: provider
modified: '2026-08-12'
name: AdColony
nav: Providers
network: true
overview: 'AdColony is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Mobile Advertising, AdTech, and SDK.


  The AdColony catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AdColony''s developer surface includes changelog, documentation, getting-started guide, and 17 more developer resources.'
plans:
- name: Adcolony Plans Pricing
  plan_count: 0
  slug: adcolony-plans-pricing
random_paper: 112
rate_limits:
- limit_count: 0
  name: Adcolony Rate Limits
  slug: adcolony-rate-limits
score:
  band: thin
  composite: 33.0
  delta: -0.8
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 28.6
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 33.8
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adcolony/refs/heads/main/screenshots/adcolony-2026-07-25T181608.png
security:
- kind: domain-security
  name: Adcolony Domain Security
  slug: adcolony-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adcolony
tags:
- Company
- Advertising
- Mobile Advertising
- AdTech
- SDK
- Monetization
- Mobile
website: https://www.adcolony.com/
---
