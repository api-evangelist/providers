---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 1
  name: Microsoft Azure Site Recovery Agentic Access
  operation_count: 15
  slug: microsoft-azure-site-recovery-agentic-access
  summary_line: 15 operations · 10 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Manage replication protected items in a Recovery Services vault
  name: Azure Site Recovery ReplicationProtectedItems API
  slug: microsoft-azure-site-recovery-replicationprotecteditems-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ClusterRecoveryPoint API from Azure Site Recovery — 1 operation(s) for clusterrecoverypoint.
  name: Azure Site Recovery Cluster Recovery Point API
  slug: microsoft-azure-site-recovery-clusterrecoverypoint-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ClusterRecoveryPoints API from Azure Site Recovery — 1 operation(s) for clusterrecoverypoints.
  name: Azure Site Recovery Cluster Recovery Points API
  slug: microsoft-azure-site-recovery-clusterrecoverypoints-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The MigrationRecoveryPoints API from Azure Site Recovery — 2 operation(s) for migrationrecoverypoints.
  name: Azure Site Recovery Migration Recovery Points API
  slug: microsoft-azure-site-recovery-migrationrecoverypoints-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Operations API from Azure Site Recovery — 1 operation(s) for operations.
  name: Azure Site Recovery Operations API
  slug: microsoft-azure-site-recovery-operations-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ReplicationAlertSettings API from Azure Site Recovery — 2 operation(s) for replicationalertsettings.
  name: Azure Site Recovery Replication Alert Settings API
  slug: microsoft-azure-site-recovery-replicationalertsettings-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ReplicationAppliances API from Azure Site Recovery — 1 operation(s) for replicationappliances.
  name: Azure Site Recovery Replication Appliances API
  slug: microsoft-azure-site-recovery-replicationappliances-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ReplicationEligibilityResults API from Azure Site Recovery — 2 operation(s) for replicationeligibilityresults.
  name: Azure Site Recovery Replication Eligibility Results API
  slug: microsoft-azure-site-recovery-replicationeligibilityresults-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ReplicationEvents API from Azure Site Recovery — 2 operation(s) for replicationevents.
  name: Azure Site Recovery Replication Events API
  slug: microsoft-azure-site-recovery-replicationevents-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ReplicationFabrics API from Azure Site Recovery — 8 operation(s) for replicationfabrics.
  name: Azure Site Recovery Replication Fabrics API
  slug: microsoft-azure-site-recovery-replicationfabrics-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ReplicationJobs API from Azure Site Recovery — 6 operation(s) for replicationjobs.
  name: Azure Site Recovery Replication Jobs API
  slug: microsoft-azure-site-recovery-replicationjobs-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ReplicationLogicalNetworks API from Azure Site Recovery — 2 operation(s) for replicationlogicalnetworks.
  name: Azure Site Recovery Replication Logical Networks API
  slug: microsoft-azure-site-recovery-replicationlogicalnetworks-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ReplicationMigrationItems API from Azure Site Recovery — 9 operation(s) for replicationmigrationitems.
  name: Azure Site Recovery Replication Migration Items API
  slug: microsoft-azure-site-recovery-replicationmigrationitems-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ReplicationNetworkMappings API from Azure Site Recovery — 3 operation(s) for replicationnetworkmappings.
  name: Azure Site Recovery Replication Network Mappings API
  slug: microsoft-azure-site-recovery-replicationnetworkmappings-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ReplicationNetworks API from Azure Site Recovery — 3 operation(s) for replicationnetworks.
  name: Azure Site Recovery Replication Networks API
  slug: microsoft-azure-site-recovery-replicationnetworks-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ReplicationProtectableItems API from Azure Site Recovery — 2 operation(s) for replicationprotectableitems.
  name: Azure Site Recovery Replication Protectable Items API
  slug: microsoft-azure-site-recovery-replicationprotectableitems-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ReplicationProtectionClusters API from Azure Site Recovery — 10 operation(s) for replicationprotectionclusters.
  name: Azure Site Recovery Replication Protection Clusters API
  slug: microsoft-azure-site-recovery-replicationprotectionclusters-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ReplicationProtectionContainerMappings API from Azure Site Recovery — 4 operation(s) for replicationprotectioncontainermappings.
  name: Azure Site Recovery Replication Protection Container Mappings API
  slug: microsoft-azure-site-recovery-replicationprotectioncontainermappings-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ReplicationProtectionContainers API from Azure Site Recovery — 7 operation(s) for replicationprotectioncontainers.
  name: Azure Site Recovery Replication Protection Containers API
  slug: microsoft-azure-site-recovery-replicationprotectioncontainers-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ReplicationProtectionIntents API from Azure Site Recovery — 2 operation(s) for replicationprotectionintents.
  name: Azure Site Recovery Replication Protection Intents API
  slug: microsoft-azure-site-recovery-replicationprotectionintents-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ReplicationRecoveryPlans API from Azure Site Recovery — 9 operation(s) for replicationrecoveryplans.
  name: Azure Site Recovery Replication Recovery Plans API
  slug: microsoft-azure-site-recovery-replicationrecoveryplans-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ReplicationRecoveryServicesProviders API from Azure Site Recovery — 5 operation(s) for replicationrecoveryservicesproviders.
  name: Azure Site Recovery Replication Recovery Services Providers API
  slug: microsoft-azure-site-recovery-replicationrecoveryservicesproviders-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ReplicationStorageClassificationMappings API from Azure Site Recovery — 3 operation(s) for replicationstorageclassificationmappings.
  name: Azure Site Recovery Replication Storage Classification Mappings API
  slug: microsoft-azure-site-recovery-replicationstorageclassificationmappings-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ReplicationStorageClassifications API from Azure Site Recovery — 3 operation(s) for replicationstorageclassifications.
  name: Azure Site Recovery Replication Storage Classifications API
  slug: microsoft-azure-site-recovery-replicationstorageclassifications-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ReplicationVaultHealth API from Azure Site Recovery — 2 operation(s) for replicationvaulthealth.
  name: Azure Site Recovery Replication Vault Health API
  slug: microsoft-azure-site-recovery-replicationvaulthealth-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ReplicationVaultSetting API from Azure Site Recovery — 2 operation(s) for replicationvaultsetting.
  name: Azure Site Recovery Replication Vault Setting API
  slug: microsoft-azure-site-recovery-replicationvaultsetting-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ReplicationvCenters API from Azure Site Recovery — 3 operation(s) for replicationvcenters.
  name: Azure Site Recovery Replicationv Centers API
  slug: microsoft-azure-site-recovery-replicationvcenters-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The SupportedOperatingSystems API from Azure Site Recovery — 1 operation(s) for supportedoperatingsystems.
  name: Azure Site Recovery Supported Operating Systems API
  slug: microsoft-azure-site-recovery-supportedoperatingsystems-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The TargetComputeSizes API from Azure Site Recovery — 1 operation(s) for targetcomputesizes.
  name: Azure Site Recovery Target Compute Sizes API
  slug: microsoft-azure-site-recovery-targetcomputesizes-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Recovery Points API from Azure Site Recovery — 2 operation(s) for recovery points.
  name: Azure Site Recovery Recovery Points API
  slug: microsoft-azure-site-recovery-recovery-points-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Replication Policies API from Azure Site Recovery — 2 operation(s) for replication policies.
  name: Azure Site Recovery Replication Policies API
  slug: microsoft-azure-site-recovery-replication-policies-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: Manage recovery plans for orchestrated failover
  name: Azure Site Recovery Recovery Plans API
  slug: microsoft-azure-site-recovery-recoveryplans-api
artifact_total: 51
collections:
- collection_type: open
  name: Azure Site Recovery REST RecoveryPlans API
  slug: open-microsoft-azure-site-recovery-recoveryplans-api
- collection_type: open
  name: Azure Site Recovery REST RecoveryPlans ReplicationProtectedItems API
  slug: open-microsoft-azure-site-recovery-replicationprotecteditems-api
- collection_type: open
  name: Azure Site Recovery REST API
  slug: open-microsoft-azure-site-recovery
common:
- group: design
  href: https://artifacts.apis.io/microsoft-azure-site-recovery/rules/microsoft-azure-site-recovery-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-azure-site-recovery-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-site-recovery/json-ld/microsoft-azure-site-recovery-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microsoft-azure-site-recovery-context.jsonld
- group: design
  href: https://artifacts.apis.io/microsoft-azure-site-recovery/vocabulary/microsoft-azure-site-recovery-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-azure-site-recovery-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-site-recovery/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-site-recovery/data-model/microsoft-azure-site-recovery-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-azure-site-recovery-data-model.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-site-recovery/cli/microsoft-azure-site-recovery-cli.yml
  title: ''
  type: CLI
  url: cli/microsoft-azure-site-recovery-cli.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-azure-site-recovery/changelog/microsoft-azure-site-recovery-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/microsoft-azure-site-recovery-changelog.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-site-recovery/conventions/microsoft-azure-site-recovery-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-azure-site-recovery-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.microsoft.com/en-us/trust-center
- group: design
  href: https://artifacts.apis.io/microsoft-azure-site-recovery/lifecycle/microsoft-azure-site-recovery-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-azure-site-recovery-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-site-recovery/errors/microsoft-azure-site-recovery-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-azure-site-recovery-problem-types.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-site-recovery/conformance/microsoft-azure-site-recovery-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-azure-site-recovery-conformance.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-site-recovery/llms/microsoft-azure-site-recovery-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-azure-site-recovery-llms.txt
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-site-recovery/well-known/microsoft-azure-site-recovery-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-azure-site-recovery-security.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-site-recovery/well-known/microsoft-azure-site-recovery-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-azure-site-recovery-well-known.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-site-recovery/hosts/microsoft-azure-site-recovery-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-azure-site-recovery-hosts.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-site-recovery/vendors/microsoft-azure-site-recovery-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-azure-site-recovery-vendors.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-site-recovery/packages/microsoft-azure-site-recovery-packages.yml
  title: ''
  type: SDKs
  url: packages/microsoft-azure-site-recovery-packages.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-site-recovery/packages/microsoft-azure-site-recovery-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-azure-site-recovery-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://techcommunity.microsoft.com/tag/security
- group: other
  title: ''
  type: Leadership
  url: https://news.microsoft.com/leadership
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.microsoft.com/en-us/changelog
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/category/windows/blog/windows-itpro-blog
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-site-recovery/security/microsoft-azure-site-recovery-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/microsoft-azure-site-recovery-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-site-recovery/security/microsoft-azure-site-recovery-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-azure-site-recovery-vulnerability-disclosure.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-site-recovery/plans/microsoft-azure-site-recovery-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-azure-site-recovery-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-azure-site-recovery/rate-limits/microsoft-azure-site-recovery-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-azure-site-recovery-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-site-recovery/finops/microsoft-azure-site-recovery-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-azure-site-recovery-finops.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-site-recovery/capabilities/microsoft-azure-site-recovery-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/microsoft-azure-site-recovery-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://microsoft.com
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-site-recovery/agentic-access/microsoft-azure-site-recovery-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-site-recovery-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-site-recovery/security/microsoft-azure-site-recovery-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-site-recovery-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-site-recovery/authentication/microsoft-azure-site-recovery-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-site-recovery-authentication.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-site-recovery/scopes/microsoft-azure-site-recovery-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-site-recovery-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/site-recovery/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/site-recovery/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-quickstart
- group: operate
  title: ''
  type: StatusPage
  url: https://azure.status.microsoft/en-us/status
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/azure-site-recovery
- group: agent
  title: ''
  type: LlmsText
  url: https://portal.azure.com/llms.txt
created: '2026-03-13'
description: Azure Site Recovery REST API provides management of disaster recovery for Azure VMs, on-premises VMs, and physical servers. It supports configuring replication, running test failovers, executing planned and unplanned failovers, and managing recovery plans.
finops:
- has_sources: true
  method: derived
  name: Microsoft Azure Site Recovery Finops
  primary_unit: ''
  service_category: ''
  slug: microsoft-azure-site-recovery-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-site-recovery.png
json_schemas:
- name: EnableProtectionInput
  property_count: 1
  slug: microsoft-azure-site-recovery-enable-protection-input
- name: ReplicationProtectedItemCollection
  property_count: 2
  slug: microsoft-azure-site-recovery-replication-protected-item-collection
- name: ReplicationProtectedItem
  property_count: 5
  slug: microsoft-azure-site-recovery-replication-protected-item
jsonld:
- class_count: 3
  name: Microsoft Azure Site Recovery Context
  property_count: 7
  slug: microsoft-azure-site-recovery-context
layout: provider
modified: '2026-09-16'
name: Azure Site Recovery
nav: Providers
network: true
overview: 'Azure Site Recovery publishes 32 API contracts indexed on the [APIs.io](https://apis.io/) network, including ReplicationProtectedItems API, Cluster Recovery Point API, Cluster Recovery Points API, and 29 more. Tagged areas include Disaster Recovery, Replication, Business Continuity, Failover, and Microsoft Azure.


  The Azure Site Recovery catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Azure Site Recovery''s developer surface includes CLI, changelog, engineering blog, authentication, developer portal, pricing, documentation, and 38 more developer resources.'
plans:
- name: Microsoft Azure Site Recovery Plans Pricing
  plan_count: 2
  slug: microsoft-azure-site-recovery-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 2
  name: Microsoft Azure Site Recovery Rate Limits
  slug: microsoft-azure-site-recovery-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: Azure Site Recovery API Rules
  rule_count: 54
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 8
  slug: microsoft-azure-site-recovery-rules
scopes:
- name: Microsoft Azure Site Recovery Scopes
  scope_count: 1
  slug: microsoft-azure-site-recovery-scopes
  summary_line: 1 scope · implicit
score:
  band: strong
  composite: 64.8
  coverage:
    artifact_dirs: 34
    catalog_earned: 72.8
    catalog_earned_first_party: 16.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 18.2
  facets:
    access_clarity: 68.4
    contract_governance: 22.0
    contract_quality: 51.7
    developer_ergonomics: 63.7
    discoverability: 82.1
    operational_transparency: 65.8
  previous_composite: 46.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 36
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/microsoft-azure-site-recovery/microsoft-azure-site-recovery-2026-06-20T185437.png
security:
- kind: authentication
  name: Microsoft Azure Site Recovery Authentication
  slug: microsoft-azure-site-recovery-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Site Recovery Domain Security
  slug: microsoft-azure-site-recovery-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Azure Site Recovery Vulnerability Disclosure
  slug: microsoft-azure-site-recovery-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Azure Site Recovery Trust Center
  slug: microsoft-azure-site-recovery-trust-center
  summary_line: GDPR
skill_count: 2
skills:
- name: planned-failover-and-reprotect
  slug: microsoft-azure-site-recovery-planned-failover-and-reprotect
- name: test-failover-drill
  slug: microsoft-azure-site-recovery-test-failover-drill
slug: microsoft-azure-site-recovery
tags:
- Disaster Recovery
- Replication
- Business Continuity
- Failover
- Microsoft Azure
- Azure Resource Manager
website: https://microsoft.com
---
