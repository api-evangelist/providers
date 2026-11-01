---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 40
  human_in_the_loop: 0
  name: Namirial Agentic Access
  operation_count: 81
  slug: namirial-agentic-access
  summary_line: 81 operations · 40 acting
api_count: 3
apis:
- baseURL: https://saas.esignanywhere.net/api
  baseurl_source: declared
  description: Access to authentication endpoints
  name: Namirial Auth API
  slug: namirial-auth-api
- baseURL: https://saas.esignanywhere.net/api
  baseurl_source: declared
  description: The Authorization API from Namirial — 2 operation(s) for authorization.
  name: Namirial Authorization API
  slug: namirial-authorization-api
- baseURL: https://saas.esignanywhere.net/api
  baseurl_source: declared
  description: The AutomaticProfile API from Namirial — 1 operation(s) for automaticprofile.
  name: Namirial Automatic Profile API
  slug: namirial-automaticprofile-api
- baseURL: https://saas.esignanywhere.net/api
  baseurl_source: declared
  description: Manage clients
  name: Namirial Clients API
  slug: namirial-clients-api
- baseURL: https://saas.esignanywhere.net/api
  baseurl_source: declared
  description: Manage association between clients and instances
  name: Namirial Clients Instances API
  slug: namirial-clientsinstances-api
- baseURL: https://saas.esignanywhere.net/api
  baseurl_source: declared
  description: Manage documents
  name: Namirial Documents API
  slug: namirial-documents-api
- baseURL: https://saas.esignanywhere.net/api
  baseurl_source: declared
  description: The Draft API from Namirial — 10 operation(s) for draft.
  name: Namirial Draft API
  slug: namirial-draft-api
- baseURL: https://saas.esignanywhere.net/api
  baseurl_source: declared
  description: The DraftActivity API from Namirial — 1 operation(s) for draftactivity.
  name: Namirial Draft Activity API
  slug: namirial-draftactivity-api
- baseURL: https://saas.esignanywhere.net/api
  baseurl_source: declared
  description: The Envelope API from Namirial — 13 operation(s) for envelope.
  name: Namirial Envelope API
  slug: namirial-envelope-api
- baseURL: https://saas.esignanywhere.net/api
  baseurl_source: declared
  description: The EnvelopeActivity API from Namirial — 2 operation(s) for envelopeactivity.
  name: Namirial Envelope Activity API
  slug: namirial-envelopeactivity-api
- baseURL: https://saas.esignanywhere.net/api
  baseurl_source: declared
  description: The EnvelopeBulk API from Namirial — 7 operation(s) for envelopebulk.
  name: Namirial Envelope Bulk API
  slug: namirial-envelopebulk-api
- baseURL: https://saas.esignanywhere.net/api
  baseurl_source: declared
  description: Manage eSignAnyWhere envelope
  name: Namirial Envelopes API
  slug: namirial-envelopes-api
- baseURL: https://saas.esignanywhere.net/api
  baseurl_source: declared
  description: The File API from Namirial — 4 operation(s) for file.
  name: Namirial File API
  slug: namirial-file-api
- baseURL: https://saas.esignanywhere.net/api
  baseurl_source: declared
  description: Manage instances
  name: Namirial Instances API
  slug: namirial-instances-api
- baseURL: https://saas.esignanywhere.net/api
  baseurl_source: declared
  description: The License API from Namirial — 1 operation(s) for license.
  name: Namirial License API
  slug: namirial-license-api
- baseURL: https://saas.esignanywhere.net/api
  baseurl_source: declared
  description: Manage connector organizations
  name: Namirial Organizations API
  slug: namirial-organizations-api
- baseURL: https://saas.esignanywhere.net/api
  baseurl_source: declared
  description: Manage association between organizations and instances
  name: Namirial Organizations Instances API
  slug: namirial-organizationsinstances-api
- baseURL: https://saas.esignanywhere.net/api
  baseurl_source: declared
  description: Manage process signature
  name: Namirial Processes API
  slug: namirial-processes-api
- baseURL: https://saas.esignanywhere.net/api
  baseurl_source: declared
  description: The SealingCertificate API from Namirial — 1 operation(s) for sealingcertificate.
  name: Namirial Sealing Certificate API
  slug: namirial-sealingcertificate-api
- baseURL: https://saas.esignanywhere.net/api
  baseurl_source: declared
  description: The System API from Namirial — 1 operation(s) for system.
  name: Namirial System API
  slug: namirial-system-api
- baseURL: https://saas.esignanywhere.net/api
  baseurl_source: declared
  description: The Team API from Namirial — 2 operation(s) for team.
  name: Namirial Team API
  slug: namirial-team-api
- baseURL: https://saas.esignanywhere.net/api
  baseurl_source: declared
  description: The Template API from Namirial — 6 operation(s) for template.
  name: Namirial Template API
  slug: namirial-template-api
artifact_total: 46
common:
- group: agent
  href: https://artifacts.apis.io/namirial/agentic-access/namirial-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/namirial-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/namirial/plans/namirial-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/namirial-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/namirial/rules/namirial-rules.yml
  title: ''
  type: Spectral
  url: rules/namirial-rules.yml
- group: design
  href: https://artifacts.apis.io/namirial/json-ld/namirial-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/namirial-context.jsonld
- group: design
  href: https://artifacts.apis.io/namirial/vocabulary/namirial-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/namirial-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/namirial/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/namirial/data-model/namirial-data-model.yml
  title: ''
  type: DataModel
  url: data-model/namirial-data-model.yml
- group: design
  href: https://artifacts.apis.io/namirial/components/namirial-components.yml
  title: ''
  type: Components
  url: components/namirial-components.yml
- group: operate
  href: https://artifacts.apis.io/namirial/changelog/namirial-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/namirial-changelog.yml
- group: design
  href: https://artifacts.apis.io/namirial/conventions/namirial-conventions.yml
  title: ''
  type: Conventions
  url: conventions/namirial-conventions.yml
- group: start
  href: https://artifacts.apis.io/namirial/sandbox/namirial-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/namirial-sandbox.yml
- group: operate
  href: https://artifacts.apis.io/namirial/lifecycle/namirial-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/namirial-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/namirial/lifecycle/namirial-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/namirial-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/namirial/errors/namirial-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/namirial-problem-types.yml
- group: design
  href: https://artifacts.apis.io/namirial/conformance/namirial-conformance.yml
  title: ''
  type: Conformance
  url: conformance/namirial-conformance.yml
- group: other
  href: https://artifacts.apis.io/namirial/overlays/namirial-connectors-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/namirial-connectors-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/namirial/llms/namirial-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/namirial-llms.txt
- group: other
  href: https://artifacts.apis.io/namirial/a2a/namirial-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/namirial-a2a.yml
- group: agent
  href: https://artifacts.apis.io/namirial/well-known/namirial-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/namirial-well-known.yml
- group: other
  href: https://artifacts.apis.io/namirial/hosts/namirial-hosts.yml
  title: ''
  type: Hosts
  url: hosts/namirial-hosts.yml
- group: build
  href: https://artifacts.apis.io/namirial/integrations/namirial-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/namirial-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/namirial/vendors/namirial-vendors.yml
  title: ''
  type: Vendors
  url: vendors/namirial-vendors.yml
- group: build
  href: https://artifacts.apis.io/namirial/packages/namirial-packages.yml
  title: ''
  type: SDKs
  url: packages/namirial-packages.yml
- group: build
  href: https://artifacts.apis.io/namirial/packages/namirial-packages.yml
  title: ''
  type: Packages
  url: packages/namirial-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.namirial.com/en/blog/trust/
- group: start
  title: ''
  type: GettingStarted
  url: https://documentation.namirial.com/onboarding
- group: auth
  href: https://artifacts.apis.io/namirial/scopes/namirial-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/namirial-scopes.yml
- group: auth
  href: https://artifacts.apis.io/namirial/authentication/namirial-authentication.yml
  title: ''
  type: Authentication
  url: authentication/namirial-authentication.yml
- group: auth
  href: https://artifacts.apis.io/namirial/security/namirial-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/namirial-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.namirial.com/en/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.namirial.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://doc.namirial.com/
- group: docs
  title: ''
  type: APIReference
  url: https://doc.namirial.com/connectors-apis/latest/
- group: operate
  title: ''
  type: Support
  url: https://servicedesk.namirial.com/hc/en-gb
- group: company
  title: ''
  type: Blog
  url: https://www.namirial.com/en/blog/
- group: company
  title: ''
  type: Newsroom
  url: https://www.namirial.com/en/news/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.namirial.com/
- group: auth
  title: ''
  type: Security
  url: https://www.namirial.com/en/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.namirial.com/en/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/namirial/
created: '2026-10-18'
description: Namirial is a European digital trust services company and qualified trust service provider. Its own site describes products for customer identification and identity verification (Namirial Onboarding), electronic signatures, digital identity wallets (Wallet Gateway, Wallet App), and related trust and compliance services for large enterprises, SMEs and public administration. It publishes product documentation, developer SDK docs (Android, iOS, Windows) and a Connectors APIs reference.
image: https://www.namirial.com/wp-content/uploads/cropped-favicon-namirial-360x360.png
json_schemas:
- name: CreateProcessDraftRequest
  property_count: 6
  slug: namirial-create-process-draft-request
- name: EnvelopeDetailResponse
  property_count: 6
  slug: namirial-envelope-detail-response
- name: GetProcessResponse
  property_count: 5
  slug: namirial-get-process-response
- name: InstanceNoId
  property_count: 5
  slug: namirial-instance-no-id
- name: Instance
  property_count: 6
  slug: namirial-instance
- name: Organization
  property_count: 4
  slug: namirial-organization
jsonld:
- class_count: 28
  name: Namirial Context
  property_count: 66
  slug: namirial-context
layout: provider
modified: '2026-10-18'
name: Namirial
nav: Providers
network: true
overview: 'Namirial publishes 22 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Authorization API, Automatic Profile API, and 19 more. Tagged areas include Company, Digital Trust, Electronic Signature, Identity Verification, and Digital Identity.


  The Namirial catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Namirial''s developer surface includes changelog, sandbox, getting-started guide, authentication, documentation, API reference, support, and 33 more developer resources.'
plans:
- name: Namirial Plans Pricing
  plan_count: 3
  slug: namirial-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Namirial Rate Limits
  slug: namirial-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Namirial API Rules
  rule_count: 12
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 3
  slug: namirial-rules
scopes:
- name: Namirial Scopes
  scope_count: 5
  slug: namirial-scopes
  summary_line: 5 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 59.0
  coverage:
    artifact_dirs: 31
    catalog_earned: 77.8
    catalog_earned_first_party: 12.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.0
    contract_governance: 22.0
    contract_quality: 59.3
    developer_ergonomics: 73.2
    discoverability: 73.2
    operational_transparency: 50.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Namirial Authentication
  slug: namirial-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Namirial Domain Security
  slug: namirial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 10
skills:
- name: bulk-send
  slug: namirial-bulk-send
- name: download-signed-documents
  slug: namirial-download-signed-documents
- name: namirial-draft-lifecycle
  slug: namirial-draft-lifecycle
- name: manage-active-envelope
  slug: namirial-manage-active-envelope
- name: namirial-process-file-workflow
  slug: namirial-process-file-workflow
- name: namirial-retrieve-envelope-details
  slug: namirial-retrieve-envelope-details
- name: namirial-retrieve-template-information
  slug: namirial-retrieve-template-information
- name: send-document-for-signature
  slug: namirial-send-document-for-signature
- name: namirial-send-envelope-bulk
  slug: namirial-send-envelope-bulk
- name: send-from-template
  slug: namirial-send-from-template
slug: namirial
tags:
- Company
- Digital Trust
- Electronic Signature
- Identity Verification
- Digital Identity
- Trust Services
- Compliance
website: https://www.namirial.com/en/
---
