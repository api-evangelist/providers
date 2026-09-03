---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nebula-security-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nebusec.ai
- group: company
  title: ''
  type: About
  url: https://nebusec.ai/about
- group: company
  title: ''
  type: Blog
  url: https://nebusec.ai/research
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/NebuSec/vega-skill/blob/main/README.md
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/NebuSec/vega-skill/blob/main/skills/vega-cli/SKILL.md
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/NebuSec/vega-skill#getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NebuSec
- group: operate
  title: ''
  type: Support
  url: mailto:info@nebusec.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nebusec.ai/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nebusec.ai/privacy/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/nebusecurity
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/125323912/
- group: agent
  title: ''
  type: AgentSkill
  url: skills/nebula-security-vega-cli.md
- group: build
  title: ''
  type: CLI
  url: cli/nebula-security-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/nebula-security-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nebula-security-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nebula-security-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nebula-security-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nebula-security-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nebula-security-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nebula-security-llms.txt
created: '2026-07-17'
description: Nebula Security is an AI-native cybersecurity company backed by Y Combinator (S26) and founded by world-class hackers — members of a top CTF team, DEF CON winners, Black Hat speakers, and cybersecurity PhDs. Its product, Vega, is an AI security agent that audits codebases for vulnerabilities on the Vega backend, alongside human-led product security auditing. Vega runs from the terminal via the Vega CLI (`vega`), which is distributed as an installable Agent Skill and an npm/global binary, authenticates with an API key or OAuth login, and exposes a project → repository → scan → finding drill-down. The team publishes vulnerability research (e.g. an nginx RCE, CVE-2026-42530) and positions "Audited by Nebula Security" as a product credibility marker.
image: https://nebusec.ai/nebusec-social.png
layout: provider
modified: '2026-07-20'
name: Nebula Security
nav: Providers
network: true
overview: 'Nebula Security is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cybersecurity, Vulnerability Management, and Application Security.


  Nebula Security''s developer surface includes engineering blog, documentation, API reference, getting-started guide, support, CLI, authentication, and 15 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 22.7
  coverage:
    artifact_dirs: 12
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 61.9
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 22.7
  provenance:
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nebula-security/refs/heads/main/screenshots/nebula-security-2026-08-07T184807.png
security:
- kind: authentication
  name: Nebula Security Authentication
  slug: nebula-security-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Nebula Security Domain Security
  slug: nebula-security-domain-security
  summary_line: TLSv1.3 · DMARC
slug: nebula-security
tags:
- Company
- Security
- Cybersecurity
- Vulnerability Management
- Application Security
- Code Scanning
- Artificial Intelligence
- Developer Tools
- CLI
website: https://nebusec.ai
---
