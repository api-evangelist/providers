---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- baseURL: https://raw.githubusercontent.com
  baseurl_source: declared
  description: The Databricks Industry Solutions API from Cleaninglab — 1 operation(s) for databricks industry solutions.
  name: Cleaninglab Databricks Industry Solutions API
  slug: cleaninglab-databricks-industry-solutions-api
artifact_total: 5
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cleaninglab/refs/heads/main/rules/cleaninglab-rules.yml
  title: ''
  type: Spectral
  url: rules/cleaninglab-rules.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cleaninglab/refs/heads/main/cli/cleaninglab-cli.yml
  title: ''
  type: CLI
  url: cli/cleaninglab-cli.yml
- group: auth
  title: ''
  type: Compliance
  url: https://cleanlab.ai/trust/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cleaninglab/refs/heads/main/conformance/cleaninglab-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cleaninglab-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cleaninglab/refs/heads/main/llms/cleaninglab-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cleaninglab-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cleaninglab/refs/heads/main/well-known/cleaninglab-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cleaninglab-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cleaninglab/refs/heads/main/well-known/cleaninglab-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cleaninglab-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cleaninglab/refs/heads/main/hosts/cleaninglab-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cleaninglab-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cleaninglab/refs/heads/main/vendors/cleaninglab-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cleaninglab-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cleaninglab/refs/heads/main/packages/cleaninglab-packages.yml
  title: ''
  type: SDKs
  url: packages/cleaninglab-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cleaninglab/refs/heads/main/packages/cleaninglab-packages.yml
  title: ''
  type: Packages
  url: packages/cleaninglab-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cleanlab.ai/terms/
- group: operate
  title: ''
  type: Support
  url: https://help.cleanlab.ai/
- group: auth
  title: ''
  type: Security
  url: https://cleanlab.ai/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cleanlab.ai/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://cleanlab.ai/news/
- group: other
  title: ''
  type: Leadership
  url: https://cleanlab.ai/team/
- group: company
  title: ''
  type: Blog
  url: https://cleanlab.ai/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.cleanlab.ai/studio/quickstart/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cleanlab.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cleanlab
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cleaninglab/refs/heads/main/security/cleaninglab-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cleaninglab-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cleaninglab/refs/heads/main/security/cleaninglab-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cleaninglab-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cleaninglab/refs/heads/main/security/cleaninglab-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cleaninglab-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cleanlab.ai
coverage:
  checked: '2026-10-09'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on the provider's hosts.
  evidence:
  - status: 404
    url: https://cleanlab.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: Cleanlab provides AI safety tools to detect and remediate hallucinations, retrieval errors, and policy violations in AI agents. The platform offers guardrails, monitoring, and automated evaluation for LLM outputs, helping enterprises deploy trustworthy AI. Acquired by Handshake AI, Cleanlab serves developers with APIs, SDKs, and a web UI for real‑time error correction and compliance.
image: https://cleanlab.ai/_next/static/media/social-share-card-homepage.71fc9f90.png
layout: provider
modified: '2026-10-08'
name: Cleaninglab
nav: Providers
network: true
overview: 'Cleaninglab is listed with 1 API on the [APIs.io](https://apis.io/) network: Databricks Industry Solutions API. Tagged areas include Company, Artificial Intelligence, Safety, Monitoring, and Hallucination.


  The Cleaninglab catalog on APIs.io includes 1 Spectral governance ruleset.


  Cleaninglab''s developer surface includes CLI, support, engineering blog, getting-started guide, documentation, and 20 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Cleaninglab API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: cleaninglab-rules
score:
  band: developing
  composite: 45.0
  coverage:
    artifact_dirs: 12
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 58.5
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 10.7
    developer_ergonomics: 42.9
    discoverability: 76.8
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Cleaninglab Domain Security
  slug: cleaninglab-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cleaninglab Vulnerability Disclosure
  slug: cleaninglab-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Cleaninglab Trust Center
  slug: cleaninglab-trust-center
  summary_line: SOC 2
slug: cleaninglab
tags:
- Company
- Artificial Intelligence
- Safety
- Monitoring
- Hallucination
website: https://cleanlab.ai
---
