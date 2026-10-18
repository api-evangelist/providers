---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.6
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 119
  human_in_the_loop: 0
  name: Cloudtruth Agentic Access
  operation_count: 211
  slug: cloudtruth-agentic-access
  summary_line: 211 operations · 119 acting
api_count: 1
apis:
- baseURL: https://api.cloudtruth.io
  baseurl_source: declared
  description: The audit API from CloudTruth — 3 operation(s) for audit.
  name: CloudTruth Audit API
  slug: cloudtruth-audit-api
- baseURL: https://api.cloudtruth.io
  baseurl_source: declared
  description: The backup API from CloudTruth — 1 operation(s) for backup.
  name: CloudTruth Backup API
  slug: cloudtruth-backup-api
- baseURL: https://api.cloudtruth.io
  baseurl_source: declared
  description: The environments API from CloudTruth — 6 operation(s) for environments.
  name: CloudTruth Environments API
  slug: cloudtruth-environments-api
- baseURL: https://api.cloudtruth.io
  baseurl_source: declared
  description: The features API from CloudTruth — 1 operation(s) for features.
  name: CloudTruth Features API
  slug: cloudtruth-features-api
- baseURL: https://api.cloudtruth.io
  baseurl_source: declared
  description: The grants API from CloudTruth — 3 operation(s) for grants.
  name: CloudTruth Grants API
  slug: cloudtruth-grants-api
- baseURL: https://api.cloudtruth.io
  baseurl_source: declared
  description: The groups API from CloudTruth — 4 operation(s) for groups.
  name: CloudTruth Groups API
  slug: cloudtruth-groups-api
- baseURL: https://api.cloudtruth.io
  baseurl_source: declared
  description: The import API from CloudTruth — 1 operation(s) for import.
  name: CloudTruth Import API
  slug: cloudtruth-import-api
- baseURL: https://api.cloudtruth.io
  baseurl_source: declared
  description: The integrations API from CloudTruth — 44 operation(s) for integrations.
  name: CloudTruth Integrations API
  slug: cloudtruth-integrations-api
- baseURL: https://api.cloudtruth.io
  baseurl_source: declared
  description: The _internal API from CloudTruth — 1 operation(s) for _internal.
  name: CloudTruth Internal API
  slug: cloudtruth-internal-api
- baseURL: https://api.cloudtruth.io
  baseurl_source: declared
  description: The invitations API from CloudTruth — 5 operation(s) for invitations.
  name: CloudTruth Invitations API
  slug: cloudtruth-invitations-api
- baseURL: https://api.cloudtruth.io
  baseurl_source: declared
  description: The log-destinations API from CloudTruth — 3 operation(s) for log-destinations.
  name: CloudTruth Log Destinations API
  slug: cloudtruth-log-destinations-api
- baseURL: https://api.cloudtruth.io
  baseurl_source: declared
  description: The memberships API from CloudTruth — 2 operation(s) for memberships.
  name: CloudTruth Memberships API
  slug: cloudtruth-memberships-api
- baseURL: https://api.cloudtruth.io
  baseurl_source: declared
  description: The organizations API from CloudTruth — 2 operation(s) for organizations.
  name: CloudTruth Organizations API
  slug: cloudtruth-organizations-api
- baseURL: https://api.cloudtruth.io
  baseurl_source: declared
  description: The projects API from CloudTruth — 20 operation(s) for projects.
  name: CloudTruth Projects API
  slug: cloudtruth-projects-api
- baseURL: https://api.cloudtruth.io
  baseurl_source: declared
  description: The reports API from CloudTruth — 2 operation(s) for reports.
  name: CloudTruth Reports API
  slug: cloudtruth-reports-api
- baseURL: https://api.cloudtruth.io
  baseurl_source: declared
  description: The Schema API from CloudTruth — 1 operation(s) for schema.
  name: CloudTruth Schema API
  slug: cloudtruth-schema-api
- baseURL: https://api.cloudtruth.io
  baseurl_source: declared
  description: The types API from CloudTruth — 4 operation(s) for types.
  name: CloudTruth Types API
  slug: cloudtruth-types-api
- baseURL: https://api.cloudtruth.io
  baseurl_source: declared
  description: The users API from CloudTruth — 3 operation(s) for users.
  name: CloudTruth Users API
  slug: cloudtruth-users-api
- baseURL: https://api.cloudtruth.io
  baseurl_source: declared
  description: The utils API from CloudTruth — 1 operation(s) for utils.
  name: CloudTruth Utils API
  slug: cloudtruth-utils-api
- baseURL: https://api.cloudtruth.io
  baseurl_source: declared
  description: The webhooks API from CloudTruth — 2 operation(s) for webhooks.
  name: CloudTruth Webhooks API
  slug: cloudtruth-webhooks-api
- baseURL: https://api.cloudtruth.io
  baseurl_source: declared
  description: The Service Accounts API from CloudTruth — 3 operation(s) for service accounts.
  name: CloudTruth Service Accounts API
  slug: cloudtruth-service-accounts-api
artifact_total: 33
asyncapis:
- description: ''
  name: Cloudtruth Webhooks
  slug: cloudtruth-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudtruth/refs/heads/main/agentic-access/cloudtruth-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudtruth-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudtruth/refs/heads/main/rules/cloudtruth-rules.yml
  title: ''
  type: Spectral
  url: rules/cloudtruth-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudtruth/refs/heads/main/json-ld/cloudtruth-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cloudtruth-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudtruth/refs/heads/main/vocabulary/cloudtruth-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cloudtruth-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudtruth/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudtruth/refs/heads/main/asyncapi/cloudtruth-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/cloudtruth-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudtruth/refs/heads/main/data-model/cloudtruth-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cloudtruth-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudtruth/refs/heads/main/errors/cloudtruth-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cloudtruth-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudtruth/refs/heads/main/conformance/cloudtruth-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cloudtruth-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudtruth/refs/heads/main/llms/cloudtruth-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloudtruth-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudtruth/refs/heads/main/well-known/cloudtruth-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cloudtruth-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudtruth/refs/heads/main/hosts/cloudtruth-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloudtruth-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudtruth/refs/heads/main/vendors/cloudtruth-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cloudtruth-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloudtruth.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cloudtruth.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://cloudtruth.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cloudtruth
- group: company
  title: ''
  type: Blog
  url: https://cloudtruth.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cloudtruth.com/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cloudtruth.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.cloudtruth.io/api/schema/redoc/
- group: docs
  title: ''
  type: APIReference
  url: https://api.cloudtruth.io/api/schema/redoc/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudtruth/refs/heads/main/authentication/cloudtruth-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cloudtruth-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudtruth/refs/heads/main/security/cloudtruth-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudtruth-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cloudtruth.com/
created: '2026-10-09'
description: CloudTruth provides a Config Data Platform that helps enterprises eliminate misconfigurations across cloud, IaC, and application settings. The platform enables teams to centrally manage configuration data, enforce policies, and integrate with CI/CD pipelines, Kubernetes, Terraform, and other tools. CloudTruth offers secure storage, versioning, and audit trails for configuration values, supporting compliance and reducing risk of configuration drift. It serves developers, DevOps, and security engineers seeking reliable configuration management at scale.
image: https://cloudtruth.com/wp-content/uploads/2025/06/drift-logo-1.svg
json_schemas:
- name: AwsPull
  property_count: 15
  slug: cloudtruth-aws-pull
- name: AwsPush
  property_count: 19
  slug: cloudtruth-aws-push
- name: AzureKeyVaultPush
  property_count: 17
  slug: cloudtruth-azure-key-vault-push
- name: Parameter
  property_count: 20
  slug: cloudtruth-parameter
- name: PatchedAwsPull
  property_count: 15
  slug: cloudtruth-patched-aws-pull
- name: Value
  property_count: 27
  slug: cloudtruth-value
jsonld:
- class_count: 120
  name: Cloudtruth Context
  property_count: 174
  slug: cloudtruth-context
layout: provider
modified: '2026-10-09'
name: CloudTruth
nav: Providers
network: true
overview: 'CloudTruth publishes 21 API contracts indexed on the [APIs.io](https://apis.io/) network, including Audit API, Backup API, Environments API, and 18 more. Tagged areas include Company, ConfigManagement, DevOps, Cloud, and Security.


  The CloudTruth catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  CloudTruth''s developer surface includes pricing, engineering blog, getting-started guide, documentation, API reference, authentication, and 19 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: CloudTruth API Rules
  rule_count: 11
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 5
  slug: cloudtruth-rules
score:
  band: developing
  composite: 46.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 67.3
    developer_ergonomics: 54.2
    discoverability: 73.2
    operational_transparency: 13.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Cloudtruth Authentication
  slug: cloudtruth-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Cloudtruth Domain Security
  slug: cloudtruth-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cloudtruth
tags:
- Company
- ConfigManagement
- DevOps
- Cloud
- Security
website: https://cloudtruth.com/
---
