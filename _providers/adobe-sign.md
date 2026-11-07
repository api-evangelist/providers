---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Adobe Sign Agentic Access
  operation_count: 2
  slug: adobe-sign-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.na4.adobesign.com/api/rest/v6
  baseurl_source: declared
  description: Discovery of the correct regional api_access_point
  name: Adobe Acrobat Sign Base URIs API
  slug: adobe-sign-base-uris-api
artifact_total: 9
collections:
- collection_type: open
  name: Adobe Acrobat Sign REST Base URIs API
  slug: open-adobe-sign-base-uris-api
- collection_type: open
  name: Adobe Acrobat Sign REST API
  slug: open-adobe-sign
common:
- group: agent
  href: https://artifacts.apis.io/adobe-sign/agentic-access/adobe-sign-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/adobe-sign-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/adobe-sign/security/adobe-sign-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/adobe-sign-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/adobe-sign/security/adobe-sign-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adobe-sign-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/adobe-sign/authentication/adobe-sign-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adobe-sign-authentication.yml
- group: auth
  href: https://artifacts.apis.io/adobe-sign/scopes/adobe-sign-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/adobe-sign-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adobe-sign
- group: company
  title: ''
  type: Website
  url: https://www.adobe.com/sign.html
- group: docs
  title: ''
  type: Documentation
  url: https://opensource.adobe.com/acrobat-sign/developer_guide/index.html
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.adobe.com/document-services/homepage/
- group: start
  title: ''
  type: Signup
  url: https://www.adobe.com/sign/free-trial-global.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.adobe.com/sign/pricing/plans.html
- group: start
  title: ''
  type: Login
  url: https://secure.adobesign.com/public/login
- group: operate
  title: ''
  type: Support
  url: https://helpx.adobe.com/support/sign.html
- group: operate
  title: ''
  type: FAQ
  url: https://helpx.adobe.com/sign/faq/api.html
created: '2026-05-11'
description: Adobe Acrobat Sign (formerly Adobe Sign and EchoSign) is a cloud-based electronic signature and digital document workflow service that lets organizations send, sign, track, and manage legally binding agreements. The Acrobat Sign REST API v6 provides programmatic access to agreements, templates, transient documents, workflows, users, groups, and webhooks using OAuth 2.0 authentication against a region-specific API access point.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/adobe-sign.png
layout: provider
modified: '2026-05-11'
name: Adobe Acrobat Sign
nav: Providers
network: true
overview: 'Adobe Acrobat Sign publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Base URIs API. Tagged areas include E-Signature, Document Workflow, Digital Signature, Adobe, and Agreements.


  The Adobe Acrobat Sign catalog on APIs.io includes 1 Spectral governance ruleset.


  Adobe Acrobat Sign''s developer surface includes authentication, documentation, signup flow, pricing, support, FAQ, and 8 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: Adobe Acrobat Sign API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: adobe-sign-rules
scopes:
- name: Adobe Sign Scopes
  scope_count: 12
  slug: adobe-sign-scopes
  summary_line: 12 scopes · authorizationCode
score:
  band: thin
  composite: 33.2
  coverage:
    artifact_dirs: 12
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 17.1
    contract_governance: 13.6
    contract_quality: 42.2
    developer_ergonomics: 40.5
    discoverability: 66.1
    operational_transparency: 13.2
  previous_composite: 33.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/adobe-sign/adobe-sign-2026-06-20T165020.png
security:
- kind: authentication
  name: Adobe Sign Authentication
  slug: adobe-sign-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Adobe Sign Domain Security
  slug: adobe-sign-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Adobe Sign Vulnerability Disclosure
  slug: adobe-sign-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: adobe-sign
tags:
- E-Signature
- Document Workflow
- Digital Signature
- Adobe
- Agreements
website: https://www.adobe.com/sign.html
---
