---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 16.9
  scored_at: '2026-08-12'
api_count: 4
apis:
- description: 'Market API for electronic placement in the London subscription market — create submissions and submission versions, upload Market Reform Contract and quote documents, add carriers and underwriters to '
  name: Lloyd's Placing API - Submission and Quote v1
  slug: lloyds-placing-api-submission-and-quote
- description: Second Placing API listed in the Lloyd's API catalogue, described by Lloyd's as "Finalise Placings, Bind Risks, Sign Transactions" — the BIND verb of the insurance lifecycle for the London subscriptio
  name: Lloyd's Placing API - Firm Order
  slug: lloyds-placing-api-firm-order
- description: Third API listed in the Lloyd's API catalogue, described by Lloyd's as "Submit Risk, Premium and Claims details for Delegated Authority Placements" — the delegated authority reporting path that carrie
  name: Lloyd's RPAC API (Risk, Premium and Claims)
  slug: lloyds-rpac-api
- description: 'Lloyd''s catastrophe event reference data served from the London Market API Gateway — the market''s canonical codes for aggregating losses to a named catastrophe (e.g. 17E "Typhoon Hato, 20 August 2017 '
  name: Lloyd's Catastrophe Codes API v1
  slug: lloyds-catastrophe-codes-api
artifact_total: 30
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lloyds-of-london-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.lloyds.com/security-reports
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/lloyds-of-london-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lloyds-of-london-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lloyds-of-london-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lloyds-of-london-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lloyds-of-london-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lloyds-of-london-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lloyds-of-london-error-codes.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lloyds-of-london-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lloyds-of-london-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/lloyds-of-london-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lloyds-of-london-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/lloyds-of-london-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lloyds-of-london-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.lloyds.com/
- group: operate
  title: ''
  type: Support
  url: https://www.lloyds.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.lloyds.com/news-and-insights
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lloyds.com/help/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lloyds.com/help/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://www.lloyds.com/market-resources/requirements-and-standards
- group: docs
  title: ''
  type: Documentation
  url: https://www.lloyds.com/market-resources/requirements-and-standards/core-data-record
- group: docs
  title: ''
  type: Documentation
  url: https://www.lloyds.com/market-resources/delegated-authorities/market-knowledge/reporting-standards
- group: docs
  title: ''
  type: Documentation
  url: https://www.lloyds.com/insights/news/lloyds-provides-acord-membership-for-all-coverholders
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lloydsdigital
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LloydsOfLondon
created: '2026-07-25'
description: 'Lloyd''s of London is the world''s specialist insurance and reinsurance market, operating as a regulated marketplace rather than as a carrier: the Corporation of Lloyd''s oversees syndicates, managing agents, brokers and coverholders who underwrite property, casualty, marine, aviation, energy, cyber, political risk and reinsurance business on a subscription basis from its home market in the United Kingdom. Its API posture reflects that role. Lloyd''s is a standards and market-infrastructure publisher first — the Core Data Record (CDR), the Market Reform Contract (MRC), coverholder and delegated claims reporting standards, and Blueprint Two digital processing requirements — and its technical surface is aimed at brokers, syndicates and market vendors, not at outside developers. Lloyd''s ran a public API Development Portal at developer.lloyds.com (the "API Factory", BETA from June 2020) that published a Base API Standard and a catalogue of three market APIs: Placing — Submission
  and Quote, Placing — Firm Order, and RPAC for delegated authority risk, premium and claims. That portal now redirects to www.lloyds.com and no replacement self-serve developer portal is published. Production access to the underlying London Market API gateway (https://api.londonmarketgroup.co.uk) has always been partner-gated: an organisation must be onboarded to LIMOSS Common Services, registered in the Common Services Azure Active Directory tenant, and register an X.509 certificate before it can call anything. There is no public, self-serve Lloyd''s API, no public sandbox and no public downloadable specification reachable today — the honest record for this market body is documentation-and-standards-first. What Lloyd''s does still operate, verified by live probe, is a genuine gated API estate: three isolated gateway environments (Sandbox, PreProd, Production), an OpenID Connect discovery document and JWKS published on each, and a routed Catastrophe Codes v1 endpoint whose unauthenticated
  /health meta resource answers 200 while its data resources return 401 "Client certificate is missing". Its most reusable public artifact is the Lloyd''s Base API Standard — a normative RFC 2119 document fixing the resource model, query grammar, collection and error envelopes, versioning compatibility rules and the dual mutual-TLS + JWT security model for every API published to the market.'
examples:
- key_count: 3
  name: Lloyds Of London Catastrophecodes Collection
  slug: lloyds-of-london-catastrophecodes-collection
- key_count: 6
  name: Lloyds Of London Catastrophecodes Singleton
  slug: lloyds-of-london-catastrophecodes-singleton
- key_count: 2
  name: Lloyds Of London Error Document
  slug: lloyds-of-london-error-document
- key_count: 1
  name: Lloyds Of London Identity Document
  slug: lloyds-of-london-identity-document
- key_count: 3
  name: Lloyds Of London Placing Brokerdepartment Collection
  slug: lloyds-of-london-placing-brokerdepartment-collection
- key_count: 3
  name: Lloyds Of London Placing Submission Collection
  slug: lloyds-of-london-placing-submission-collection
- key_count: 22
  name: Lloyds Of London Placing Submission Get
  slug: lloyds-of-london-placing-submission-get
- key_count: 18
  name: Lloyds Of London Placing Submission Post Request
  slug: lloyds-of-london-placing-submission-post-request
- key_count: 21
  name: Lloyds Of London Placing Submission Post Response
  slug: lloyds-of-london-placing-submission-post-response
- key_count: 16
  name: Lloyds Of London Placing Submission Put Request
  slug: lloyds-of-london-placing-submission-put-request
- key_count: 21
  name: Lloyds Of London Placing Submission Put Response
  slug: lloyds-of-london-placing-submission-put-response
- key_count: 9
  name: Lloyds Of London Placing Submissiondialogue Quote Request
  slug: lloyds-of-london-placing-submissiondialogue-quote-request
- key_count: 18
  name: Lloyds Of London Placing Submissiondialogue Quote Response
  slug: lloyds-of-london-placing-submissiondialogue-quote-response
- key_count: 7
  name: Lloyds Of London Placing Submissiondialogue Rfq Request
  slug: lloyds-of-london-placing-submissiondialogue-rfq-request
- key_count: 16
  name: Lloyds Of London Placing Submissiondialogue Rfq Response
  slug: lloyds-of-london-placing-submissiondialogue-rfq-response
- key_count: 3
  name: Lloyds Of London Placing Submissiondocument Collection
  slug: lloyds-of-london-placing-submissiondocument-collection
- key_count: 9
  name: Lloyds Of London Placing Submissiondocument Post Request
  slug: lloyds-of-london-placing-submissiondocument-post-request
- key_count: 14
  name: Lloyds Of London Placing Submissiondocument Post Response
  slug: lloyds-of-london-placing-submissiondocument-post-response
- key_count: 5
  name: Lloyds Of London Placing Submissionunderwriter Post Request
  slug: lloyds-of-london-placing-submissionunderwriter-post-request
- key_count: 29
  name: Lloyds Of London Placing Submissionunderwriter Post Response
  slug: lloyds-of-london-placing-submissionunderwriter-post-response
- key_count: 3
  name: Lloyds Of London Placing Underwriterorganisation Collection
  slug: lloyds-of-london-placing-underwriterorganisation-collection
- key_count: 2
  name: Lloyds Of London Version Document
  slug: lloyds-of-london-version-document
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Lloyd's of London
nav: Providers
network: true
overview: 'Lloyd''s of London publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, United Kingdom, Reinsurance, Specialty Insurance, and London Market.


  Lloyd''s of London''s developer surface includes authentication, code examples, changelog, sandbox, support, engineering blog, documentation, and 20 more developer resources.'
random_paper: 56
scopes:
- name: Lloyds Of London Scopes
  scope_count: 1
  slug: lloyds-of-london-scopes
  summary_line: 1 scope · authorizationCode/on-behalf-of
score:
  band: thin
  composite: 30.9
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 32.6
    discoverability: 72.2
    governance: 12.5
    operational_transparency: 31.6
  previous_composite: 30.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 72.7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lloyds-of-london/refs/heads/main/screenshots/lloyds-of-london-2026-07-25T225413.png
security:
- kind: authentication
  name: Lloyds Of London Authentication
  slug: lloyds-of-london-authentication
  summary_line: mutualTLS/oauth2/openIdConnect/http · 4 schemes
- kind: domain-security
  name: Lloyds Of London Domain Security
  slug: lloyds-of-london-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lloyds Of London Vulnerability Disclosure
  slug: lloyds-of-london-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: lloyds-of-london
tags:
- Insurance
- United Kingdom
- Reinsurance
- Specialty Insurance
- London Market
- Underwriting
- Claims
- Delegated Authority
- Broker
- Market Infrastructure
- Standards
- ACORD
website: https://www.lloyds.com/
---
