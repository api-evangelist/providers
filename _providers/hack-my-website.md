---
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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-25'
api_count: 1
apis:
- description: 'Automated website security scanner. Only an agent-native surface (llms.txt) is publicly declared; no conventional API contract (OpenAPI/GraphQL/AsyncAPI/gRPC/SOAP) is published. The app''s own backend '
  name: Hack My Website
  slug: hack-my-website
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://hackmywebsite.io
- group: docs
  title: ''
  type: Documentation
  url: https://hackmywebsite.io/how-it-works
- group: start
  title: ''
  type: SignUp
  url: https://hackmywebsite.io/signup
- group: start
  title: ''
  type: Login
  url: https://hackmywebsite.io/login
- group: operate
  title: ''
  type: Support
  url: mailto:support@hackmywebsite.io
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hackmywebsite.io/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hackmywebsite.io/terms-and-conditions
- group: commercial
  title: ''
  type: Pricing
  url: https://hackmywebsite.io
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/hack-my-website/refs/heads/main/plans/hack-my-website-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hack-my-website-plans-pricing.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hack-my-website/refs/heads/main/security/hack-my-website-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hack-my-website-domain-security.yml
coverage:
  checked: '2026-09-18'
  detail: Hack My Website (by Aivi Labs) ships an end-user SaaS security scanner in early-access/waitlist; its only public API path (/api) is a private, robots-disallowed app backend that serves no OpenAPI, and no developer portal, SDK, webhooks or machine-readable contract is published anywhere.
  evidence:
  - status: 404
    url: https://hackmywebsite.io/api/openapi.json
  - status: 404
    url: https://hackmywebsite.io/openapi.json
  - status: 200
    url: https://hackmywebsite.io/robots.txt
  reason: no-developer-program
  state: none
created: '2026-09-18'
description: Automated web-application security scanner that runs 200+ checks across DAST (OWASP ZAP), CVE exploit templates (Nuclei), static analysis (Semgrep/SAST), and SaaS-misconfiguration checks, producing a 0-100 AI Launch Score with go/no-go readiness bands and 1-click AI remediation fix prompts for Cursor, Claude Code, and Windsurf. Built by Aivi Labs for teams shipping sites made with AI coding tools (Lovable, Bolt, v0, Cursor, Claude Code); currently early-access/waitlist with no public developer API.
layout: provider
modified: '2026-09-18'
name: Hack My Website
nav: Providers
network: true
overview: 'Hack My Website publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Application Security, Web Security, Vulnerability Scanning, DAST, and SAST.


  Hack My Website''s developer surface includes documentation, signup flow, support, pricing, and 6 more developer resources.'
plans:
- name: Hack My Website Plans Pricing
  plan_count: 4
  slug: hack-my-website-plans-pricing
random_paper: 8
score:
  band: emerging
  composite: 23.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 60.7
    operational_transparency: 0.0
  previous_composite: 25.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Hack My Website Domain Security
  slug: hack-my-website-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hack-my-website
tags:
- Application Security
- Web Security
- Vulnerability Scanning
- DAST
- SAST
- Cybersecurity
- AppSec
- DevSecOps
- AI Remediation
- Software-as-a-Service
website: https://hackmywebsite.io
---
