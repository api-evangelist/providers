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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Branch's Quote to Bind GraphQL API exposes everything an affinity partner needs to go from initial quote to final purchase of Branch home + auto (and optional umbrella) insurance without leaving their
  name: Branch Quote to Bind API
  slug: branch-quote-to-bind-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/branch-insurance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ourbranch.com/
- group: start
  title: ''
  type: Portal
  url: https://docs.v2.api.ourbranch.com/
- group: start
  title: ''
  type: Signup
  url: https://www.ourbranch.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.v2.api.ourbranch.com/
- group: start
  title: ''
  type: Sandbox
  url: https://studio.apollographql.com/public/Branch-Quote-to-Bind-Staging/explorer?variant=current
- group: company
  title: ''
  type: About
  url: https://www.ourbranch.com/s/about
- group: company
  title: ''
  type: Press
  url: https://www.ourbranch.com/s/press
- group: company
  title: ''
  type: Blog
  url: https://www.ourbranch.com/s/blog
- group: company
  title: ''
  type: Careers
  url: https://www.ourbranch.com/s/careers
- group: other
  title: ''
  type: Claims
  url: https://www.ourbranch.com/s/claims
- group: other
  title: ''
  type: AvailableStates
  url: https://www.ourbranch.com/s/available-states
- group: operate
  title: ''
  type: CommunityPledge
  url: https://www.ourbranch.com/s/community-pledge
- group: operate
  title: ''
  type: CommunityDiscount
  url: https://www.ourbranch.com/s/my-community-discount
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ourbranch.com/s/blog/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ourbranch.com/s/blog/terms-of-use
- group: company
  title: ''
  type: Partner
  url: https://www.ourbranch.com/s/blog/partner_with_branch
- group: docs
  title: ''
  type: Documentation
  url: https://www.ourbranch.com/s/blog/branch_insurance_exchange
- group: operate
  title: ''
  type: Support
  url: mailto:api@ourbranch.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ourbranch
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/ourbranch
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OurBranch
created: '2026-05-25'
description: Branch is a Columbus, Ohio insurtech that bundles home and auto insurance (with optional umbrella coverage) and issues policies in seconds from just a name and address. The company operates as Branch Insurance Exchange, a reciprocal insurer, plus the managing General Branch Agency / Branch Financial, Inc. holding company, and originally targeted direct-to-consumer customers with a quote-and-bind flow that prefills rating data from public sources. Branch raised a $147M Series C at a $1.05B valuation in 2022 (Weatherford Capital, Acrew Capital, Anthemis, Cherry Creek Holdings, Greycroft, HSCM Bermuda, AmFam Ventures, others), partnered with SimpliSafe (home security bundle) and ADT, and runs an embedded "Quote to Bind" GraphQL API used by affinity partners (mortgage originators, lenders, aggregators) to embed home + auto quotes inside their own apps. The Quote to Bind v2 GraphQL API (https://docs.v2.api.ourbranch.com) exposes requestQuoteV2, recalculateQuoteV2, addCar, addDriver,
  requestBind, getOffer, enhancedGetOffer, getBoundPoliciesByOfferId, getPolicyDocuments, and getOfferPDF, plus optional webhook / SFTP / S3 postbacks for bind and document-signed events. Partners authenticate with an API key in the Authorization header and an x-affinity-code header when responsible for multiple agencies, and may either run the whole flow via the API or hand customers off to ourbranch.com / staff.ourbranch.com for customize / review / checkout / sign-documents steps. A staging endpoint at https://staging.v2.api.ourbranch.com mirrors production with shared test users and payment methods. Branch operates in roughly two dozen US states including Ohio, Texas, Illinois, Arizona, Missouri, and others, and emphasises community-discount pricing, a community pledge / giveback program, and B Corp certification (2023). There is no public OpenAPI specification — the API is GraphQL-only and the schema is browsable on Apollo Studio (studio.apollographql.com/public/Branch-Quote-to-Bind-Staging)
  with an API key.
graphqls:
- description: Branch's Quote to Bind GraphQL API exposes everything an affinity partner needs to go from initial quote to final purchase of Branch home + auto (and optional umbrella) insurance without leaving their
  name: Branch GraphQL API
  slug: branch-insurance-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/branch-insurance.png
layout: provider
modified: '2026-05-25'
name: Branch
nav: Providers
network: true
overview: 'Branch publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Home Insurance, Auto Insurance, Umbrella Insurance, and Bundled Insurance.


  Branch''s developer surface includes developer portal, signup flow, getting-started guide, sandbox, engineering blog, documentation, support, and 15 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 20.2
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 41.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 20.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.2
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/branch-insurance/refs/heads/main/screenshots/branch-insurance-2026-06-20T173630.png
security:
- kind: domain-security
  name: Branch Insurance Domain Security
  slug: branch-insurance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: branch-insurance
tags:
- Insurance
- Home Insurance
- Auto Insurance
- Umbrella Insurance
- Bundled Insurance
- Insurtech
- Reciprocal Exchange
- Embedded Insurance
- Quote to Bind
- GraphQL
- Partner API
- Affinity
- Mortgage
- Columbus Ohio
website: https://www.ourbranch.com/
---
