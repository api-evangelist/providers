---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.9
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 14
  human_in_the_loop: 1
  name: Cognition Labs Agentic Access
  operation_count: 26
  slug: cognition-labs-agentic-access
  summary_line: 26 operations · 14 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.devin.ai/v1
  baseurl_source: declared
  description: Upload and download files for Devin to work with.
  name: Cognition Labs Attachments API
  slug: cognition-labs-attachments-api
- baseURL: https://api.devin.ai/v1
  baseurl_source: declared
  description: Agent Compute Unit (ACU) usage and billing metrics.
  name: Cognition Labs Consumption API
  slug: cognition-labs-consumption-api
- baseURL: https://api.devin.ai/v1
  baseurl_source: declared
  description: Cross-organization administration.
  name: Cognition Labs Enterprise (v3) API
  slug: cognition-labs-enterprise-v3-api
- baseURL: https://api.devin.ai/v1
  baseurl_source: declared
  description: Organization knowledge entries and folders.
  name: Cognition Labs Knowledge API
  slug: cognition-labs-knowledge-api
- baseURL: https://api.devin.ai/v1
  baseurl_source: declared
  description: Send and read messages within a running session.
  name: Cognition Labs Messages API
  slug: cognition-labs-messages-api
- baseURL: https://api.devin.ai/v1
  baseurl_source: declared
  description: Current org-scoped session and user management.
  name: Cognition Labs Organizations (v3) API
  slug: cognition-labs-organizations-v3-api
- baseURL: https://api.devin.ai/v1
  baseurl_source: declared
  description: Reusable team playbooks that seed new sessions.
  name: Cognition Labs Playbooks API
  slug: cognition-labs-playbooks-api
- baseURL: https://api.devin.ai/v1
  baseurl_source: declared
  description: Encrypted credentials Devin can use inside sessions.
  name: Cognition Labs Secrets API
  slug: cognition-labs-secrets-api
- baseURL: https://api.devin.ai/v1
  baseurl_source: declared
  description: Create and manage Devin sessions (v1 legacy surface).
  name: Cognition Labs Sessions API
  slug: cognition-labs-sessions-api
- baseURL: https://api.devin.ai/v1
  baseurl_source: declared
  description: Operations for enterprise-specific features and reporting
  name: Cognition Labs Enterprise API
  slug: cognition-labs-enterprise-api
- baseURL: https://api.devin.ai/v1
  baseurl_source: declared
  description: Operations for managing audit logs
  name: Cognition Labs Audit Logs API
  slug: cognition-labs-audit-logs-api
artifact_total: 43
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Devin API (Cognition Labs) Attachments API
  slug: open-cognition-labs-attachments-api
- collection_type: open
  name: Devin API (Cognition Labs) Attachments Consumption API
  slug: open-cognition-labs-consumption-api
- collection_type: open
  name: Devin API (Cognition Labs) Attachments Enterprise (v3) API
  slug: open-cognition-labs-enterprise-v3-api
- collection_type: open
  name: Devin API (Cognition Labs) Attachments Knowledge API
  slug: open-cognition-labs-knowledge-api
- collection_type: open
  name: Devin API (Cognition Labs) Attachments Messages API
  slug: open-cognition-labs-messages-api
- collection_type: open
  name: Devin API (Cognition Labs) Attachments Organizations (v3) API
  slug: open-cognition-labs-organizations-v3-api
- collection_type: open
  name: Devin API (Cognition Labs) Attachments Playbooks API
  slug: open-cognition-labs-playbooks-api
- collection_type: open
  name: Devin API (Cognition Labs) Attachments Secrets API
  slug: open-cognition-labs-secrets-api
- collection_type: open
  name: Devin API (Cognition Labs) Attachments Sessions API
  slug: open-cognition-labs-sessions-api
- collection_type: open
  name: Devin API (Cognition Labs)
  slug: open-cognition-labs
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cognition-labs/refs/heads/main/rules/cognition-labs-rules.yml
  title: ''
  type: Spectral
  url: rules/cognition-labs-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cognition-labs/refs/heads/main/json-ld/cognition-labs-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cognition-labs-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cognition-labs/refs/heads/main/vocabulary/cognition-labs-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cognition-labs-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cognition-labs/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cognition-labs/refs/heads/main/data-model/cognition-labs-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cognition-labs-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cognition-labs/refs/heads/main/cli/cognition-labs-cli.yml
  title: ''
  type: CLI
  url: cli/cognition-labs-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cognition-labs/refs/heads/main/changelog/cognition-labs-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cognition-labs-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.cognition.ai/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cognition-labs/refs/heads/main/errors/cognition-labs-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cognition-labs-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cognition-labs/refs/heads/main/conformance/cognition-labs-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cognition-labs-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cognition-labs/refs/heads/main/llms/cognition-labs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cognition-labs-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cognition-labs/refs/heads/main/a2a/cognition-labs-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/cognition-labs-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cognition-labs/refs/heads/main/well-known/cognition-labs-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cognition-labs-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cognition-labs/refs/heads/main/hosts/cognition-labs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cognition-labs-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cognition-labs/refs/heads/main/vendors/cognition-labs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cognition-labs-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://cognition.com/legal/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cognition.com/legal/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.devin.ai/tutorial-library/repo-setup
- group: docs
  title: ''
  type: APIReference
  url: https://docs.devin.ai/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cognition-labs/refs/heads/main/agentic-access/cognition-labs-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cognition-labs-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cognition-labs/refs/heads/main/security/cognition-labs-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cognition-labs-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cognition-labs/refs/heads/main/security/cognition-labs-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cognition-labs-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cognition-labs/refs/heads/main/security/cognition-labs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cognition-labs-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cognition-labs/refs/heads/main/authentication/cognition-labs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cognition-labs-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CognitionAI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cognition-ai-labs
- group: company
  title: ''
  type: Website
  url: https://cognition.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.devin.ai
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cognition-labs/refs/heads/main/plans/cognition-labs-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cognition-labs-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cognition-labs/refs/heads/main/rate-limits/cognition-labs-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cognition-labs-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cognition-labs/refs/heads/main/finops/cognition-labs-finops.yml
  title: ''
  type: FinOps
  url: finops/cognition-labs-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://cognition.com/blog
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cognition-labs/refs/heads/main/capabilities/cognition-labs-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cognition-labs-capability-edges.yml
created: '2026-07-02'
description: Cognition Labs is the applied AI lab behind Devin, the autonomous AI software engineer that plans, writes, tests, and ships code inside its own shell, code editor, and browser. The Devin API lets teams create and drive Devin sessions programmatically - sending prompts and follow-up messages, attaching files, storing organizational knowledge and reusable playbooks, injecting secrets, and tracking Agent Compute Unit (ACU) consumption - across a legacy v1 surface, a v2 enterprise surface, and a current v3 organizations/enterprise surface built around service-user and personal access tokens.
finops:
- name: Cognition Labs Finops
  service_category: AI and Machine Learning
  slug: cognition-labs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cognition-labs.png
json_schemas:
- name: CreateSessionInput
  property_count: 12
  slug: cognition-labs-create-session-input
- name: CreateSessionResponse
  property_count: 3
  slug: cognition-labs-create-session-response
- name: KnowledgeEntry
  property_count: 0
  slug: cognition-labs-knowledge-entry
- name: KnowledgeFolder
  property_count: 4
  slug: cognition-labs-knowledge-folder
- name: KnowledgeInput
  property_count: 6
  slug: cognition-labs-knowledge-input
- name: PlaybookInput
  property_count: 4
  slug: cognition-labs-playbook-input
- name: Playbook
  property_count: 0
  slug: cognition-labs-playbook
- name: SecretInput
  property_count: 5
  slug: cognition-labs-secret-input
- name: SecretMetadata
  property_count: 4
  slug: cognition-labs-secret-metadata
- name: SessionDetail
  property_count: 0
  slug: cognition-labs-session-detail
- name: SessionSummary
  property_count: 12
  slug: cognition-labs-session-summary
jsonld:
- class_count: 26
  name: Cognition Labs Context
  property_count: 68
  slug: cognition-labs-context
layout: provider
modified: '2026-07-02'
name: Cognition Labs
nav: Providers
network: true
overview: 'Cognition Labs publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Attachments API, Consumption API, Enterprise (v3) API, and 8 more. Tagged areas include Artificial Intelligence, AI Agents, Autonomous Coding, Software Engineering, and LLM.


  The Cognition Labs catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cognition Labs'' developer surface includes CLI, changelog, getting-started guide, API reference, authentication, documentation, engineering blog, and 26 more developer resources.'
plans:
- name: Cognition Labs Plans Pricing
  plan_count: 6
  slug: cognition-labs-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 6
  name: Cognition Labs Rate Limits
  slug: cognition-labs-rate-limits
rules:
- effective_rule_count: 55
  extends:
  - spectral:oas
  name: Cognition Labs API Rules
  rule_count: 14
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 3
  slug: cognition-labs-rules
score:
  band: strong
  composite: 60.6
  coverage:
    artifact_dirs: 27
    catalog_earned: 87.4
    catalog_earned_first_party: 0.0
    catalog_gap: 27.7
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 19.8
  facets:
    access_clarity: 62.6
    contract_governance: 35.6
    contract_quality: 68.3
    developer_ergonomics: 53.0
    discoverability: 73.2
    operational_transparency: 57.4
  previous_composite: 40.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.1
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/cognition-labs/refs/heads/main/screenshots/cognition-labs-2026-07-25T210009.png
security:
- kind: authentication
  name: Cognition Labs Authentication
  slug: cognition-labs-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cognition Labs Domain Security
  slug: cognition-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cognition Labs Vulnerability Disclosure
  slug: cognition-labs-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Cognition Labs Trust Center
  slug: cognition-labs-trust-center
  summary_line: SOC 2, ISO 27001
slug: cognition-labs
tags:
- Artificial Intelligence
- AI Agents
- Autonomous Coding
- Software Engineering
- LLM
- Devin
website: https://cognition.ai/
---
