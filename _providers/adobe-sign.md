---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Adobe Sign Agentic Access
  operation_count: 2
  slug: adobe-sign-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- description: Discovery of the correct regional api_access_point
  name: Adobe Acrobat Sign Base URIs API
  slug: adobe-sign-base-uris-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Adobe Acrobat Sign REST Base URIs API
  slug: open-adobe-sign-base-uris-api
- collection_type: open
  name: Adobe Acrobat Sign REST API
  slug: open-adobe-sign
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/adobe-sign-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/adobe-sign-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adobe-sign-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/adobe-sign-authentication.yml
- group: auth
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
graphqls:
- description: This directory contains a conceptual GraphQL schema for the Adobe Acrobat Sign REST API v6. Adobe Acrobat Sign (formerly Adobe Sign and EchoSign) is a cloud-based electronic signature and digital docu
  name: Adobe Sign (Acrobat Sign) GraphQL Schema
  slug: adobe-sign-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/adobe-sign.png
layout: provider
modified: '2026-05-11'
name: Adobe Acrobat Sign
nav: Providers
network: true
overview: 'Adobe Acrobat Sign publishes 1 API on the [APIs.io](https://apis.io/) network: Base URIs API. Tagged areas include Electronic Signature, E-Signature, Document Workflow, Digital Signature, and Adobe.


  Adobe Acrobat Sign''s developer surface includes authentication, documentation, signup flow, pricing, support, FAQ, and 8 more developer resources.'
random_paper: 19
scopes:
- name: Adobe Sign Scopes
  scope_count: 12
  slug: adobe-sign-scopes
  summary_line: 12 scopes · authorizationCode
score:
  band: thin
  composite: 30.8
  coverage:
    artifact_dirs: 8
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 48.2
    developer_ergonomics: 40.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 30.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adobe-sign/refs/heads/main/screenshots/adobe-sign-2026-06-20T165020.png
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
- Electronic Signature
- E-Signature
- Document Workflow
- Digital Signature
- Adobe
- Agreements
website: https://www.adobe.com/sign.html
---
