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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Formspree Agentic Access
  operation_count: 1
  slug: formspree-agentic-access
  summary_line: 1 operation
api_count: 3
apis:
- description: 'Public POST endpoint per form. Accepts standard HTML form posts and cross-origin AJAX (Accept: application/json) and returns JSON. No auth for the submission itself; per-form spam controls.'
  name: Formspree Form Submission Endpoint
  slug: submission
- description: REST API for retrieving submissions and managing forms. Endpoints under /api/0/forms/<hashid>/. Bearer auth using a public read-only API key or a Master API key (paid plans only). Supports since/limit
  name: Formspree Forms API
  slug: forms-api
- description: The Forms API from Formspree — 1 operation(s) for forms.
  name: Formspree Forms API
  slug: formspree-forms-api
artifact_total: 12
collections:
- collection_type: open
  name: Formspree Form Submissions API
  slug: open-formspree
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/formspree-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/formspree-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/formspree-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/formspree-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/formspree-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/formspree
- group: company
  title: ''
  type: Website
  url: https://formspree.io/
- group: docs
  title: ''
  type: Documentation
  url: https://help.formspree.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://formspree.io/plans
- group: build
  title: ''
  type: GitHub
  url: https://github.com/formspree
- group: operate
  title: ''
  type: StatusPage
  url: https://www.formspreestatus.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/formspree-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/formspree-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/formspree-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://formspree.io/llms.txt
created: '2026-05-08'
description: 'Formspree is a form backend for static and Jamstack sites. Two API surfaces matter: (1) the public form-submission endpoint (formspree.io/f/{hashid}) that accepts POST submissions and returns JSON when the Accept header is set, and (2) the Forms API (formspree.io/api/0/...) for programmatic submission retrieval, export and form management. Plugins and the Formspree CLI extend the surface.'
finops:
- name: Formspree Finops
  service_category: Forms / Backend
  slug: formspree-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/formspree.png
layout: provider
modified: '2026-05-08'
name: Formspree
nav: Providers
network: true
overview: 'Formspree publishes 1 API on the [APIs.io](https://apis.io/) network: Forms API. Tagged areas include Forms, Backend, Static Sites, Email, and Webhooks.


  Formspree''s developer surface includes authentication, documentation, pricing, GitHub presence, and 11 more developer resources.'
plans:
- name: Formspree Plans Pricing
  plan_count: 4
  slug: formspree-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 3
  name: Formspree Rate Limits
  slug: formspree-rate-limits
score:
  band: thin
  composite: 38.3
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 62.7
    developer_ergonomics: 19.6
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 38.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/formspree/refs/heads/main/screenshots/formspree-2026-06-20T181435.png
security:
- kind: authentication
  name: Formspree Authentication
  slug: formspree-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Formspree Domain Security
  slug: formspree-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Formspree Vulnerability Disclosure
  slug: formspree-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Formspree Trust Center
  slug: formspree-trust-center
  summary_line: SOC 2, GDPR
slug: formspree
tags:
- Forms
- Backend
- Static Sites
- Email
- Webhooks
- JAMstack
- CLI
website: https://formspree.io/
---
