---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.8
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 50
  human_in_the_loop: 3
  name: Phala Agentic Access
  operation_count: 102
  slug: phala-agentic-access
  summary_line: 102 operations · 50 acting · 3 human-in-the-loop
api_count: 1
apis:
- description: OpenAI-compatible confidential inference API (chat completions, responses, Anthropic-format messages, completions, embeddings, models) served from GPU TEEs, plus attestation report, signed receipt and
  name: Phala Private AI API
  slug: phala-private-ai-api
- baseURL: https://cloud-api.phala.com
  baseurl_source: declared
  description: App template management and CVM deployment from app blueprints
  name: Phala Network Apps API
  slug: phala-apps-api
- baseURL: https://cloud-api.phala.com
  baseurl_source: declared
  description: The apps-kms-info API from Phala Network — 1 operation(s) for apps-kms-info.
  name: Phala Network Apps Kms Info API
  slug: phala-apps-kms-info-api
- baseURL: https://cloud-api.phala.com
  baseurl_source: declared
  description: The apps-pending-updates API from Phala Network — 2 operation(s) for apps-pending-updates.
  name: Phala Network Apps Pending Updates API
  slug: phala-apps-pending-updates-api
- baseURL: https://cloud-api.phala.com
  baseurl_source: declared
  description: Remote attestation and TEE verification endpoints
  name: Phala Network Attestations API
  slug: phala-attestations-api
- baseURL: https://cloud-api.phala.com
  baseurl_source: declared
  description: Confidential Virtual Machine (CVM) lifecycle management on Phala Network
  name: Phala Network CVMs API
  slug: phala-cvms-api
- baseURL: https://cloud-api.phala.com
  baseurl_source: declared
  description: The cvms-network-config API from Phala Network — 3 operation(s) for cvms-network-config.
  name: Phala Network Cvms Network Config API
  slug: phala-cvms-network-config-api
- baseURL: https://cloud-api.phala.com
  baseurl_source: declared
  description: Available hardware configurations for CVM deployment
  name: Phala Network Instance Types API
  slug: phala-instance-types-api
- baseURL: https://cloud-api.phala.com
  baseurl_source: declared
  description: Key Management Service — key derivation, on-chain anchoring, and inspection
  name: Phala Network KMS API
  slug: phala-kms-api
- baseURL: https://cloud-api.phala.com
  baseurl_source: declared
  description: SSH public key management for CVM access
  name: Phala Network SSH Keys API
  slug: phala-ssh-keys-api
- baseURL: https://cloud-api.phala.com
  baseurl_source: declared
  description: Manage webhook endpoints and monitor delivery history
  name: Phala Network Webhooks API
  slug: phala-webhooks-api
artifact_total: 24
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/phala/refs/heads/main/scopes/phala-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/phala-scopes.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/phala/refs/heads/main/agentic-access/phala-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/phala-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/phala/refs/heads/main/rules/phala-rules.yml
  title: ''
  type: Spectral
  url: rules/phala-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/phala/refs/heads/main/json-ld/phala-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/phala-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/phala/refs/heads/main/vocabulary/phala-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/phala-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/phala/refs/heads/main/data-model/phala-data-model.yml
  title: ''
  type: DataModel
  url: data-model/phala-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://phala.com/trust
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/phala/refs/heads/main/errors/phala-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/phala-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/phala/refs/heads/main/conformance/phala-conformance.yml
  title: ''
  type: Conformance
  url: conformance/phala-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/phala/refs/heads/main/llms/phala-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/phala-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/phala/refs/heads/main/a2a/phala-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/phala-a2a.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/phala/refs/heads/main/well-known/phala-explorer-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/phala-explorer-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/phala/refs/heads/main/well-known/phala-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/phala-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/phala/refs/heads/main/hosts/phala-hosts.yml
  title: ''
  type: Hosts
  url: hosts/phala-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/phala/refs/heads/main/vendors/phala-vendors.yml
  title: ''
  type: Vendors
  url: vendors/phala-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/phala/refs/heads/main/packages/phala-packages.yml
  title: ''
  type: SDKs
  url: packages/phala-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/phala/refs/heads/main/packages/phala-packages.yml
  title: ''
  type: Packages
  url: packages/phala-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://phala.com/learn/tags/Security
- group: company
  title: ''
  type: Newsroom
  url: https://phala.com/tags/News
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/phala/refs/heads/main/authentication/phala-authentication.yml
  title: ''
  type: Authentication
  url: authentication/phala-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/phala/refs/heads/main/security/phala-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/phala-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/phala/refs/heads/main/security/phala-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/phala-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://phala.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.phala.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.phala.com/phala-cloud/phala-cloud-api/overview
- group: start
  title: ''
  type: DeveloperPortal
  url: https://phala.com/tags/Developers
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.phala.com/phala-cloud/getting-started/attestation
- group: company
  title: ''
  type: Blog
  url: https://phala.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Phala-Network
- group: start
  title: ''
  type: Login
  url: https://cloud.phala.com/login
- group: start
  title: ''
  type: SignUp
  url: https://cloud.phala.com/register
- group: commercial
  title: ''
  type: Pricing
  url: https://phala.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://phala.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://phala.com/terms
created: '2026-10-13'
description: Phala Network (Phala Cloud) runs confidential computing infrastructure built on Trusted Execution Environments (Intel TDX, NVIDIA GPU TEE) and the open-source dstack framework. Developers deploy Docker workloads as confidential VMs (CVMs) through the Phala Cloud API, CLI and SDKs, verify them with remote attestation and on-chain KMS, and call attested Private AI models through an OpenAI-compatible inference API at inference.phala.com.
image: https://phala.com/favicon.ico
json_schemas:
- name: CVMInfoDetail
  property_count: 33
  slug: phala-cvminfo-detail
- name: ProvisionComposeFileUpdateRequest
  property_count: 22
  slug: phala-provision-compose-file-update-request
- name: ProvisionDstackAppRequestV2
  property_count: 25
  slug: phala-provision-dstack-app-request-v2
- name: CvmBasicInfo
  property_count: 28
  slug: phala-teehouse-api-routes-cvms-management-cvm-basic-info
- name: CVMInfo
  property_count: 32
  slug: phala-teehouse-api-routes-cvms-v20260121-schemas-cvminfo
- name: UpdateCvmRequest
  property_count: 15
  slug: phala-update-cvm-request
jsonld:
- class_count: 120
  name: Phala Context
  property_count: 355
  slug: phala-context
layout: provider
modified: '2026-10-13'
name: Phala Network
nav: Providers
network: true
overview: 'Phala Network publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Apps API, Apps Kms Info API, Apps Pending Updates API, and 8 more. Tagged areas include Company, Confidential Computing, Trusted Execution Environments, Inference, and Cloud Infrastructure.


  The Phala Network catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Phala Network''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, signup flow, pricing, and 27 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Phala Network API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 1
  slug: phala-rules
scopes:
- name: Phala Scopes
  scope_count: 0
  slug: phala-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 55.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 22.0
    contract_quality: 61.9
    developer_ergonomics: 59.5
    discoverability: 75.0
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 11.1
security:
- kind: authentication
  name: Phala Authentication
  slug: phala-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Phala Domain Security
  slug: phala-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Phala Trust Center
  slug: phala-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: phala
tags:
- Company
- Confidential Computing
- Trusted Execution Environments
- Inference
- Cloud Infrastructure
- Attestation
- LLM Router
website: https://phala.com
---
