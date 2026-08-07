---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-06'
api_count: 2
apis:
- description: The ad-request surface Doceree publisher partners call to fetch an HCP-targeted advertisement. It is the endpoint behind the Doceree Publisher Tag, the first-party Prebid.js header-bidding adapter (bi
  name: Doceree Bidder / Ad Request API
  slug: bidder
- description: Doceree's measurement and beacon endpoint. The Prebid.js adapter fires GET /v1/hbTimeout and GET /v1/hbBidWon with a base64-encoded, URI-encoded JSON payload on the `data` query parameter and an `adp`
  name: Doceree Tracking API
  slug: tracking
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/doceree-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://doceree.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://doceree.com/publishers
- group: docs
  title: ''
  type: Documentation
  url: https://support.doceree.com/hc/en-us
- group: docs
  title: ''
  type: APIReference
  url: https://docs.prebid.org/dev-docs/bidders/doceree.html
- group: operate
  title: ''
  type: Support
  url: https://support.doceree.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://blog.doceree.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/doceree
- group: start
  title: ''
  type: Login
  url: https://exchange.doceree.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://doceree.com/us-terms-of-service-advertiser
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://doceree.com/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://doceree.com/trust
- group: auth
  title: ''
  type: Compliance
  url: https://doceree.com/trust
- group: operate
  title: ''
  type: Contact
  url: https://doceree.com/contact
- group: build
  title: ''
  type: Packages
  url: packages/doceree-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/doceree-packages.yml
- group: design
  title: ''
  type: Components
  url: components/doceree-components.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/doceree-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/doceree-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/doceree-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/doceree-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/doceree-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/doceree-llms.txt
created: '2026-08-04'
description: 'Doceree Inc. is a US healthcare marketing technology company (Short Hills, New Jersey) operating a global network of physician-only platforms for programmatic messaging and point-of-care advertising to healthcare professionals. Its platform spans HCP programmatic, point-of-care, EHR, email, SMS, co-pay/affordability and account-based messaging channels, backed by a proprietary HCP identity-resolution graph. Doceree''s public, machine-readable surface is an advertising-technology one rather than a general-purpose developer API: a versioned ad-request/bidder endpoint (bidder.doceree.com/v1/adrequest), a tracking/beacon endpoint (tracking.doceree.com), a hosted publisher tag (the Doceree Publisher Tag, servedbydoceree.doceree.com/script/render-header.js), a first-party Prebid.js header-bidding adapter (bidder code "doceree", IAB Europe GVL ID 1063), and first-party mobile ad SDKs for iOS (CocoaPods) and Android (JitPack). Doceree publishes no OpenAPI, AsyncAPI, GraphQL schema,
  MCP server or A2A agent card at any probed host as of August 2026.'
image: https://doceree.com/images/doceree-logo.svg
layout: provider
modified: '2026-08-04'
name: Doceree
nav: Providers
network: true
overview: 'Doceree publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Healthcare, Marketing, AdTech, and Programmatic.


  Doceree''s developer surface includes documentation, API reference, support, engineering blog, authentication, and 18 more developer resources.'
random_paper: 49
score:
  band: thin
  composite: 32.8
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 47.8
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 32.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 46.3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Doceree Authentication
  slug: doceree-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Doceree Domain Security
  slug: doceree-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: trust-center
  name: Doceree Trust Center
  slug: doceree-trust-center
  summary_line: SOC 2
slug: doceree
tags:
- Advertising
- Healthcare
- Marketing
- AdTech
- Programmatic
- Header Bidding
- Life Sciences
- Pharmaceutical
- Point of Care
- Identity Resolution
- Electronic Health Records
- Company
website: https://doceree.com/
---
