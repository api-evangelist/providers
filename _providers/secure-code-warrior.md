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
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.2
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Secure Code Warrior Agentic Access
  operation_count: 31
  slug: secure-code-warrior-agentic-access
  summary_line: 31 operations · 10 acting
api_count: 11
apis:
- description: 'The Secure Code Warrior Direct Linking API is a RESTful JSON service that allows partners to retrieve application security training material including links to explainer videos and training exercises '
  name: Secure Code Warrior Direct Linking API
  slug: secure-code-warrior-direct-linking-api
- description: The Assessments API from Secure Code Warrior — 3 operation(s) for assessments.
  name: Secure Code Warrior Assessments API
  slug: secure-code-warrior-assessments-api
- description: The Audit API from Secure Code Warrior — 1 operation(s) for audit.
  name: Secure Code Warrior Audit API
  slug: secure-code-warrior-audit-api
- description: The Courses API from Secure Code Warrior — 2 operation(s) for courses.
  name: Secure Code Warrior Courses API
  slug: secure-code-warrior-courses-api
- description: The Learning API from Secure Code Warrior — 2 operation(s) for learning.
  name: Secure Code Warrior Learning API
  slug: secure-code-warrior-learning-api
- description: The Metrics API from Secure Code Warrior — 3 operation(s) for metrics.
  name: Secure Code Warrior Metrics API
  slug: secure-code-warrior-metrics-api
- description: The Programs API from Secure Code Warrior — 1 operation(s) for programs.
  name: Secure Code Warrior Programs API
  slug: secure-code-warrior-programs-api
- description: The Teams API from Secure Code Warrior — 3 operation(s) for teams.
  name: Secure Code Warrior Teams API
  slug: secure-code-warrior-teams-api
- description: The Tournaments API from Secure Code Warrior — 2 operation(s) for tournaments.
  name: Secure Code Warrior Tournaments API
  slug: secure-code-warrior-tournaments-api
- description: The Training API from Secure Code Warrior — 5 operation(s) for training.
  name: Secure Code Warrior Training API
  slug: secure-code-warrior-training-api
- description: The Users API from Secure Code Warrior — 4 operation(s) for users.
  name: Secure Code Warrior Users API
  slug: secure-code-warrior-users-api
artifact_total: 25
collections:
- collection_type: open
  name: Secure Code Warrior Portal API
  slug: open-secure-code-warrior-portal
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/secure-code-warrior-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/secure-code-warrior-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/secure-code-warrior-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/secure-code-warrior-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.securecodewarrior.com
- group: docs
  title: ''
  type: Documentation
  url: https://portal-api.securecodewarrior.com/api/docs/v2/
- group: docs
  title: ''
  type: Documentation
  url: https://help.securecodewarrior.com/hc/en-us/sections/360006026452-API
- group: docs
  title: ''
  type: Documentation
  url: https://help.securecodewarrior.com/hc/en-us/articles/900005309583-Direct-Linking-API-Documentation
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SecureCodeWarrior
- group: build
  title: ''
  type: GitHubApp
  url: https://github.com/marketplace/secure-code-warrior-for-github
- group: start
  title: ''
  type: GettingStarted
  url: https://help.securecodewarrior.com/hc/en-us/articles/360036036512-How-to-enable-API-access
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/secure-code-warrior-user-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/secure-code-warrior-training-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/secure-code-warrior-context.jsonld
- group: build
  title: ''
  type: Examples
  url: examples/secure-code-warrior-get-leaderboard-example.json
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/secure-code-warrior-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/secure-code-warrior-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://www.securecodewarrior.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.securecodewarrior.com/blog
created: '2026-05-02'
description: Secure Code Warrior is a developer-first security platform that provides security training, coaching, and assessments to help developers write secure code from the start. The platform offers over 50 programming language and framework combinations, covering OWASP Top 10 and CWE vulnerability categories through interactive challenges, assessments, tournaments, and guided learning courses. Secure Code Warrior exposes a REST API supporting user management, training progress reporting, assessment assignment and tracking, tournament management, metrics, and audit logging, with GitHub and CI/CD pipeline integrations for contextual in-workflow security coaching.
examples:
- key_count: 2
  name: Secure Code Warrior Get Leaderboard Example
  slug: secure-code-warrior-get-leaderboard-example
finops:
- name: Secure Code Warrior Finops
  service_category: API
  slug: secure-code-warrior-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/secure-code-warrior.png
json_schemas:
- name: Secure Code Warrior User
  property_count: 9
  slug: secure-code-warrior-user
json_structures:
- name: Secure Code Warrior Training Structure
  property_count: 14
  slug: secure-code-warrior-training-structure
jsonld:
- class_count: 25
  name: Secure Code Warrior Context
  property_count: 2
  slug: secure-code-warrior-context
layout: provider
modified: '2026-05-19'
name: Secure Code Warrior
nav: Providers
network: true
overview: 'Secure Code Warrior publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Assessments API, Audit API, Courses API, and 7 more. Tagged areas include Application Security, Developer Training, Security Education, AppSec, and Secure Coding.


  The Secure Code Warrior catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Secure Code Warrior''s developer surface includes authentication, documentation, getting-started guide, code examples, engineering blog, and 14 more developer resources.'
plans:
- name: Secure Code Warrior Plans Pricing
  plan_count: 3
  slug: secure-code-warrior-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 5
  name: Secure Code Warrior Rate Limits
  slug: secure-code-warrior-rate-limits
rules:
- name: Secure Code Warrior API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: secure-code-warrior-jsonschema-spectral-rules
- name: Secure Code Warrior API Rules
  rule_count: 10
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 6
  slug: secure-code-warrior-rules
score:
  band: developing
  composite: 52.3
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 67.0
    developer_ergonomics: 32.6
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 52.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/secure-code-warrior/refs/heads/main/screenshots/secure-code-warrior-2026-06-20T193625.png
security:
- kind: authentication
  name: Secure Code Warrior Authentication
  slug: secure-code-warrior-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Secure Code Warrior Domain Security
  slug: secure-code-warrior-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Secure Code Warrior Trust Center
  slug: secure-code-warrior-trust-center
  summary_line: SOC 2
slug: secure-code-warrior
tags:
- Application Security
- Developer Training
- Security Education
- AppSec
- Secure Coding
- DevSecOps
website: https://www.securecodewarrior.com
---
