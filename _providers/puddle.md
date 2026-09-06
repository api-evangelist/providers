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
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/puddle-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/puddle-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://usepuddle.com
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/puddle-security.txt
- group: auth
  title: ''
  type: Security
  url: well-known/puddle-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/puddle-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/puddle-well-known.yml
- group: start
  title: ''
  type: Login
  url: https://usepuddle.com/login
created: '2026-07-17'
description: Puddle is a technical-interview platform for evaluating software-engineering candidates in real-world, AI-enabled conditions. Candidates work through live coding assessments inside a sandboxed environment with an integrated IDE and terminal, and are free to use modern AI tools (such as Claude Code) during the session. Puddle captures detailed signals about how a candidate approaches a problem across structured phases (problem discussion, architecture, implementation, and debrief) and produces an outcome report with confidence scores, focus and iteration-pace metrics, and hiring recommendations. It is sold as a B2B SaaS recruitment-assessment tool via demo and early-access waitlist. Puddle was surfaced as an a16z portfolio company and added to the API Evangelist network. As of this pass Puddle publishes no public API, developer documentation, SDK, or OpenAPI surface; the profile below captures its verifiable public web and security presence.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/puddle.png
layout: provider
modified: '2026-07-20'
name: Puddle
nav: Providers
network: true
overview: Puddle is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technical Interviews, Hiring, Developer Assessment, and Recruiting.
random_paper: 8
score:
  band: minimal
  composite: 8.4
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 8.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/puddle/refs/heads/main/screenshots/puddle-2026-09-02T152315.png
security:
- kind: domain-security
  name: Puddle Domain Security
  slug: puddle-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Puddle Vulnerability Disclosure
  slug: puddle-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: puddle
tags:
- Company
- Technical Interviews
- Hiring
- Developer Assessment
- Recruiting
- Artificial Intelligence
- Coding Assessment
website: https://usepuddle.com
---
