---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
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
  scored_at: '2026-08-03'
api_count: 4
apis:
- description: Partner API for generating and retrieving Trupanion pet insurance quotes (species, breed, age, location, and coverage inputs) so partners can surface a monthly premium in their own enrollment flow. Na
  name: Trupanion Quotes API
  slug: trupanion-quotes-api
- description: 'Partner API for converting a quote into an active Trupanion policy - submitting pet, owner, and payment details to enroll a member and bind coverage. Named as a partner product on Trupanion''s sandbox '
  name: Trupanion Enrollments API
  slug: trupanion-enrollments-api
- description: Partner API for retrieving Trupanion offers and promotional coverage programs (for example, breeder, shelter, and retail partner offers) that a partner can present to a pet owner. Named as a partner p
  name: Trupanion Offers API
  slug: trupanion-offers-api
- description: Software integration behind Trupanion's VetDirectPay - the patented ability to submit a treatment invoice and pay the veterinary hospital directly at checkout, often before the pet owner leaves the ex
  name: Trupanion Vet Portal / VetDirectPay Integration
  slug: trupanion-vet-portal-directpay-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trupanion-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trupanion
- group: company
  title: ''
  type: Website
  url: https://www.trupanion.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-documentation.trupanion.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://sandbox-trupanionapi.developer.azure-api.net/getting-started
- group: company
  title: ''
  type: PartnerProgram
  url: https://www.trupanion.com/about/partner-with-trupanion
- group: start
  title: ''
  type: SignUp
  url: https://sandbox-trupanionapi.developer.azure-api.net/signin
created: '2026-07-03'
description: Trupanion is a pet medical insurance provider for cats and dogs, best known for its patented software that pays participating veterinary hospitals directly at checkout (VetDirectPay) rather than reimbursing pet owners after the fact. Trupanion operates a partner developer portal (Azure API Management) that exposes Partner APIs for Quotes, Enrollments, and Offers, plus a Vet Portal / VetDirectPay integration used by veterinary practice management systems such as ezyVet, IDEXX, and DaySmart Vet. API access is gated - partners must be approved through Trupanion's Partner Program and are issued OAuth client credentials (client ID and client secret) plus a subscription key; the endpoint reference is not publicly published. The APIs listed here are modeled from Trupanion's public partner and portal materials, not from an openly documented API reference.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trupanion.png
layout: provider
modified: '2026-07-03'
name: Trupanion
nav: Providers
network: true
overview: 'Trupanion publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Pet Insurance, Insurance, Veterinary, InsurTech, and Direct Pay.


  Trupanion''s developer surface includes documentation, getting-started guide, signup flow, and 4 more developer resources.'
random_paper: 42
score:
  band: minimal
  composite: 12.4
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: domain-security
  name: Trupanion Domain Security
  slug: trupanion-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: trupanion
tags:
- Pet Insurance
- Insurance
- Veterinary
- InsurTech
- Direct Pay
- Partner API
website: https://www.trupanion.com/
---
