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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-24'
api_count: 3
apis:
- description: The Clearview AI facial recognition platform provides image-based identity matching backed by an indexed corpus of publicly available imagery. Access is restricted to vetted government, law enforcemen
  name: Clearview AI Facial Recognition Platform
  slug: facial-recognition
- description: 'Clearview AI offers investigation tooling for vetted law enforcement and public-safety users that surfaces matching imagery and source links for an uploaded probe image. Workflow tooling is delivered '
  name: Clearview AI Investigation Tools
  slug: investigation-tools
- description: Clearview AI markets identity-verification capabilities to regulated financial-services customers for fraud prevention, KYC enrichment, and investigative review. Integration is delivered as a vendor-m
  name: Clearview AI Financial Services
  slug: financial-services
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clearview-ai-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clearviewai
- group: company
  title: ''
  type: Website
  url: https://www.clearview.ai/
- group: company
  title: ''
  type: About
  url: https://www.clearview.ai/about-us
- group: other
  title: ''
  type: Transparency
  url: https://www.clearview.ai/post/transparency-report
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clearview.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clearview.ai/terms-of-service
- group: operate
  title: ''
  type: Contact
  url: https://www.clearview.ai/contact
- group: company
  title: ''
  type: News
  url: https://www.clearview.ai/news
- group: design
  title: ''
  type: JSONLD
  url: json-ld/clearview-ai-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/clearview-ai-rules.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://clearview.ai/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.clearview.ai/blog-feed.xml
created: '2024-01-01'
description: Clearview AI is a U.S.-based facial recognition company providing identity verification, investigative search, and biometric matching services primarily to law enforcement, government agencies, and approved financial sector customers. The platform indexes publicly available images and exposes proprietary facial recognition technology through a controlled, customer-vetted developer surface. Public technical documentation of the API is intentionally limited; access is gated, and integrations are scoped through customer agreements with strict use-case, audit, and transparency requirements.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clearview-ai.png
jsonld:
- class_count: 0
  name: Clearview Ai Context
  property_count: 4
  slug: clearview-ai-context
layout: provider
modified: '2026-04-23'
name: Clearview AI
nav: Providers
network: true
overview: 'Clearview AI publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Biometrics, Facial Recognition, Identity, Investigations, and Law Enforcement.


  The Clearview AI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Clearview AI''s developer surface includes product news, engineering blog, and 11 more developer resources.'
random_paper: 12
rules:
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Clearview AI API Rules
  rule_count: 8
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 4
  slug: clearview-ai-rules
score:
  band: emerging
  composite: 19.1
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 45.5
    contract_quality: 7.0
    developer_ergonomics: 2.4
    discoverability: 72.2
    governance: 45.5
    operational_transparency: 0.0
  previous_composite: 19.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clearview-ai/refs/heads/main/screenshots/clearview-ai-2026-06-20T174501.png
security:
- kind: domain-security
  name: Clearview Ai Domain Security
  slug: clearview-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: clearview-ai
tags:
- Biometrics
- Facial Recognition
- Identity
- Investigations
- Law Enforcement
- Surveillance
website: https://www.clearview.ai/
---
