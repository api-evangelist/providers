---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.6
  scored_at: '2026-09-23'
api_count: 1
apis:
- baseURL: https://discountedtokens.com/v1
  baseurl_source: declared
  description: OpenAI/Anthropic-compatible REST API for LLM inference with prepaid Bearer-key authentication. Documents /chat/completions, /responses, /messages, and /models via a public OpenAPI 3.1.0 contract.
  name: DiscountedTokens API
  slug: discountedtokens-api
artifact_total: 6
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/discountedtokens-api/refs/heads/main/security/discountedtokens-api-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/discountedtokens-api-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/discountedtokens-api/refs/heads/main/security/discountedtokens-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/discountedtokens-api-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/discountedtokens-api/refs/heads/main/authentication/discountedtokens-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/discountedtokens-api-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/discountedtokens-api/refs/heads/main/security/discountedtokens-api-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/discountedtokens-api-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/discountedtokens-api/refs/heads/main/well-known/discountedtokens-api-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/discountedtokens-api-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/discountedtokens-api/refs/heads/main/well-known/discountedtokens-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/discountedtokens-api-security.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/discountedtokens-api/refs/heads/main/conformance/discountedtokens-api-conformance.yml
  title: ''
  type: Conformance
  url: conformance/discountedtokens-api-conformance.yml
- group: company
  title: ''
  type: Website
  url: https://discountedtokens.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://discountedtokens.com/status
- group: commercial
  title: ''
  type: Pricing
  url: https://discountedtokens.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://discountedtokens.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://discountedtokens.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://discountedtokens.com/contact
- group: start
  title: ''
  type: SignUp
  url: https://discountedtokens.com/guest
- group: company
  title: ''
  type: Blog
  url: https://discountedtokens.com/updates
created: '2026-09-17'
description: An independent, third-party prepaid API reseller providing OpenAI/Anthropic-compatible access to frontier GPT-family models via a single Bearer key. Exposes OpenAI Chat, OpenAI Responses, and Anthropic Messages compatible endpoints with usage-based prepaid billing (no subscription, no free trial).
image: https://discountedtokens.com/og-image.png
layout: provider
modified: '2026-09-17'
name: DiscountedTokens API
nav: Providers
network: true
overview: 'DiscountedTokens API publishes 1 API on the [APIs.io](https://apis.io/) network: DiscountedTokens API. Tagged areas include Artificial Intelligence, LLM, Generative AI Inference, OpenAI-Compatible, and Anthropic Compatible.


  DiscountedTokens API''s developer surface includes authentication, pricing, support, signup flow, engineering blog, and 10 more developer resources.'
plans:
- name: Discountedtokens Api Plans Pricing
  plan_count: 0
  slug: discountedtokens-api-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Discountedtokens Api Rate Limits
  slug: discountedtokens-api-rate-limits
score:
  band: developing
  composite: 43.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 47.6
    developer_ergonomics: 42.3
    discoverability: 75.9
    operational_transparency: 42.1
  previous_composite: 43.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Discountedtokens Api Authentication
  slug: discountedtokens-api-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Discountedtokens Api Domain Security
  slug: discountedtokens-api-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Discountedtokens Api Vulnerability Disclosure
  slug: discountedtokens-api-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: discountedtokens-api
tags:
- Artificial Intelligence
- LLM
- Generative AI Inference
- OpenAI-Compatible
- Anthropic Compatible
- API Reseller
- Aggregator
- Prepaid
- Usage-Based
- Developer Tools
- AI Infrastructure
website: https://discountedtokens.com/
---
