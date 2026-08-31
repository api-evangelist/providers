---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Proctorio Agentic Access
  operation_count: 3
  slug: proctorio-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 1
apis:
- description: After an exam attempt is submitted, Proctorio POSTs an HMAC-signed JSON webhook to the integrating platform's endpoint carrying the attempt id, user id, an overall suspicion score, submission metadata
  name: Proctorio Result Webhooks (v2/v3)
  slug: proctorio-webhooks
- description: Generate signed launch URLs for proctored exam sessions.
  name: Proctorio Launch API
  slug: proctorio-launch-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Proctorio API (v2) Launch API
  slug: open-proctorio-launch-api
- collection_type: open
  name: Proctorio Launch API (v2)
  slug: open-proctorio
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/proctorio/API/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/proctorio/API/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/proctorio-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/proctorio-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/proctorio-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/proctorio-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/proctorio-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/proctorio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/proctorio-incorporated
- group: company
  title: ''
  type: Website
  url: https://proctorio.com
- group: docs
  title: ''
  type: Documentation
  url: https://proctorio.com/about/integration
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/proctorio/API
- group: commercial
  title: ''
  type: Plans
  url: plans/proctorio-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/proctorio-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/proctorio-finops.yml
- group: operate
  title: ''
  type: Changelog
  url: https://changes.proctorio.com/
created: '2026-07-05'
description: Proctorio is a remote proctoring and learning-integrity platform that secures online exams with automated recording (video, audio, screen, web traffic), identity verification, lockdown-browser behavior controls, and post-exam suspicion scoring with behavioral flags. Proctorio is delivered primarily as an LMS-embedded integration - LTI 1.1 and LTI 1.3 for Canvas, Blackboard, Brightspace (D2L), Moodle, and ILIAS - so most institutions never touch a REST API directly. For assessment platforms that are not LMS-native, Proctorio also exposes a partner/integration REST API (v2) that generates signed exam launch URLs for candidates, reviewers, and live proctors, plus HMAC-signed result webhooks (v2/v3) that deliver the exam suspicion score and behavioral flags back to the integrating platform. API access is gated - the consumer key, secret key, and region-specific API endpoint are provisioned by a Proctorio representative per institution or partner - but the endpoint paths, request
  bodies, and webhook payloads are documented publicly in Proctorio's official Apache-2.0 .NET client (github.com/proctorio/API).
finops:
- name: Proctorio Finops
  service_category: Education and Assessment
  slug: proctorio-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/proctorio.png
layout: provider
modified: '2026-07-05'
name: Proctorio
nav: Providers
network: true
overview: 'Proctorio publishes 1 API on the [APIs.io](https://apis.io/) network: Launch API. Tagged areas include Online Proctoring, Remote Proctoring, Exam Integrity, Assessment, and EdTech.


  Proctorio''s developer surface includes authentication, documentation, changelog, and 13 more developer resources.'
plans:
- name: Proctorio Plans Pricing
  plan_count: 3
  slug: proctorio-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 4
  name: Proctorio Rate Limits
  slug: proctorio-rate-limits
score:
  band: thin
  composite: 28.7
  coverage:
    artifact_dirs: 8
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 13.6
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  open_source:
    applies: true
    score: 0.0
  previous_composite: 28.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 42.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Proctorio Authentication
  slug: proctorio-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Proctorio Domain Security
  slug: proctorio-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Proctorio Vulnerability Disclosure
  slug: proctorio-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Proctorio Trust Center
  slug: proctorio-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27018, PCI DSS
slug: proctorio
tags:
- Online Proctoring
- Remote Proctoring
- Exam Integrity
- Assessment
- EdTech
- LTI
- LMS Integration
- Learning Integrity
website: https://proctorio.com
---
