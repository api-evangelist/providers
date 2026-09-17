---
access_model:
  confidence: high
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.7
  scored_at: '2026-09-16'
api_count: 5
apis:
- description: REST API for the Automation Services Catalog providing a self-service portal where users can order and manage pre-approved automation services with governance controls and approval workflows.
  name: Red Hat Automation Services Catalog API
  slug: services-catalog-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The Access_Policies API from Red Hat Ansible Automation Platform — 3 operation(s) for access_policies.
  name: Red Hat Ansible Automation Platform Access Policies API
  slug: red-hat-ansible-automation-platform-access-policies-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Acs: File API from Red Hat Ansible Automation Platform — 7 operation(s) for acs: file.'
  name: 'Red Hat Ansible Automation Platform Acs: File API'
  slug: red-hat-ansible-automation-platform-acs-file-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The activation-instances API from Red Hat Ansible Automation Platform — 3 operation(s) for activation-instances.
  name: Red Hat Ansible Automation Platform Activation Instances API
  slug: red-hat-ansible-automation-platform-activation-instances-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The activations API from Red Hat Ansible Automation Platform — 7 operation(s) for activations.
  name: Red Hat Ansible Automation Platform Activations API
  slug: red-hat-ansible-automation-platform-activations-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The activity_stream API from Red Hat Ansible Automation Platform — 2 operation(s) for activity_stream.
  name: Red Hat Ansible Automation Platform Activity Stream API
  slug: red-hat-ansible-automation-platform-activity-stream-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The ad_hoc_command_events API from Red Hat Ansible Automation Platform — 1 operation(s) for ad_hoc_command_events.
  name: Red Hat Ansible Automation Platform Ad Hoc Command Events API
  slug: red-hat-ansible-automation-platform-ad-hoc-command-events-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The ad_hoc_commands API from Red Hat Ansible Automation Platform — 8 operation(s) for ad_hoc_commands.
  name: Red Hat Ansible Automation Platform Ad Hoc Commands API
  slug: red-hat-ansible-automation-platform-ad-hoc-commands-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: AI-related operations
  name: Red Hat Ansible Automation Platform AI API
  slug: red-hat-ansible-automation-platform-ai-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The analytics API from Red Hat Ansible Automation Platform — 19 operation(s) for analytics.
  name: Red Hat Ansible Automation Platform Analytics API
  slug: red-hat-ansible-automation-platform-analytics-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Ansible: Collections API from Red Hat Ansible Automation Platform — 7 operation(s) for ansible: collections.'
  name: 'Red Hat Ansible Automation Platform Ansible: Collections API'
  slug: red-hat-ansible-automation-platform-ansible-collections-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Api API from Red Hat Ansible Automation Platform — 1 operation(s) for api: api.'
  name: 'Red Hat Ansible Automation Platform Api: API'
  slug: red-hat-ansible-automation-platform-api-api-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The api API from Red Hat Ansible Automation Platform — 6 operation(s) for api.
  name: Red Hat Ansible Automation Platform API
  slug: red-hat-ansible-automation-platform-api-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Automation-Hub API from Red Hat Ansible Automation Platform — 1 operation(s) for api: automation-hub.'
  name: 'Red Hat Ansible Automation Platform Api: Automation-Hub API'
  slug: red-hat-ansible-automation-platform-api-automation-hub-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Content Api API from Red Hat Ansible Automation Platform — 1 operation(s) for api: content api.'
  name: 'Red Hat Ansible Automation Platform Api: Content API'
  slug: red-hat-ansible-automation-platform-api-content-api-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Content API from Red Hat Ansible Automation Platform — 1 operation(s) for api: content.'
  name: 'Red Hat Ansible Automation Platform Api: Content API'
  slug: red-hat-ansible-automation-platform-api-content-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Content V3 API from Red Hat Ansible Automation Platform — 1 operation(s) for api: content v3.'
  name: 'Red Hat Ansible Automation Platform Api: Content V3 API'
  slug: red-hat-ansible-automation-platform-api-content-v3-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Content V3 Artifacts Collections API from Red Hat Ansible Automation Platform — 1 operation(s) for api: content v3 artifacts collections.'
  name: 'Red Hat Ansible Automation Platform Api: Content V3 Artifacts Collections API'
  slug: red-hat-ansible-automation-platform-api-content-v3-artifacts-collections-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Content V3 Collection_Versions All API from Red Hat Ansible Automation Platform — 1 operation(s) for api: content v3 collection_versions all.'
  name: 'Red Hat Ansible Automation Platform Api: Content V3 Collection_Versions All API'
  slug: red-hat-ansible-automation-platform-api-content-v3-collection-versions-all-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Content V3 Collections All API from Red Hat Ansible Automation Platform — 1 operation(s) for api: content v3 collections all.'
  name: 'Red Hat Ansible Automation Platform Api: Content V3 Collections All API'
  slug: red-hat-ansible-automation-platform-api-content-v3-collections-all-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Content V3 Collections API from Red Hat Ansible Automation Platform — 2 operation(s) for api: content v3 collections.'
  name: 'Red Hat Ansible Automation Platform Api: Content V3 Collections API'
  slug: red-hat-ansible-automation-platform-api-content-v3-collections-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Content V3 Collections Versions API from Red Hat Ansible Automation Platform — 2 operation(s) for api: content v3 collections versions.'
  name: 'Red Hat Ansible Automation Platform Api: Content V3 Collections Versions API'
  slug: red-hat-ansible-automation-platform-api-content-v3-collections-versions-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Content V3 Collections Versions Copy API from Red Hat Ansible Automation Platform — 1 operation(s) for api: content v3 collections versions copy.'
  name: 'Red Hat Ansible Automation Platform Api: Content V3 Collections Versions Copy API'
  slug: red-hat-ansible-automation-platform-api-content-v3-collections-versions-copy-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Content V3 Collections Versions Docs-Blob API from Red Hat Ansible Automation Platform — 1 operation(s) for api: content v3 collections versions docs-blob.'
  name: 'Red Hat Ansible Automation Platform Api: Content V3 Collections Versions Docs-Blob API'
  slug: red-hat-ansible-automation-platform-api-content-v3-collections-versions-docs-blob-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Content V3 Collections Versions Move API from Red Hat Ansible Automation Platform — 1 operation(s) for api: content v3 collections versions move.'
  name: 'Red Hat Ansible Automation Platform Api: Content V3 Collections Versions Move API'
  slug: red-hat-ansible-automation-platform-api-content-v3-collections-versions-move-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Content V3 Excludes API from Red Hat Ansible Automation Platform — 1 operation(s) for api: content v3 excludes.'
  name: 'Red Hat Ansible Automation Platform Api: Content V3 Excludes API'
  slug: red-hat-ansible-automation-platform-api-content-v3-excludes-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Content V3 Imports Collections API from Red Hat Ansible Automation Platform — 1 operation(s) for api: content v3 imports collections.'
  name: 'Red Hat Ansible Automation Platform Api: Content V3 Imports Collections API'
  slug: red-hat-ansible-automation-platform-api-content-v3-imports-collections-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Content V3 Namespaces API from Red Hat Ansible Automation Platform — 2 operation(s) for api: content v3 namespaces.'
  name: 'Red Hat Ansible Automation Platform Api: Content V3 Namespaces API'
  slug: red-hat-ansible-automation-platform-api-content-v3-namespaces-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Content V3 Plugin Ansible Client-Configuration API from Red Hat Ansible Automation Platform — 1 operation(s) for api: content v3 plugin ansible client-configuration.'
  name: 'Red Hat Ansible Automation Platform Api: Content V3 Plugin Ansible Client-Configuration API'
  slug: red-hat-ansible-automation-platform-api-content-v3-plugin-ansible-client-configuration-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Content V3 Plugin Ansible Content Collections All-Collections API from Red Hat Ansible Automation Platform — 1 operation(s) for api: content v3 plugin ansible content collections all-collecti'
  name: 'Red Hat Ansible Automation Platform Api: Content V3 Plugin Ansible Content Collections All-Collections API'
  slug: red-hat-ansible-automation-platform-api-content-v3-plugin-ansible-content-collections-all-collections-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Content V3 Plugin Ansible Content Collections All-Versions API from Red Hat Ansible Automation Platform — 1 operation(s) for api: content v3 plugin ansible content collections all-versions.'
  name: 'Red Hat Ansible Automation Platform Api: Content V3 Plugin Ansible Content Collections All-Versions API'
  slug: red-hat-ansible-automation-platform-api-content-v3-plugin-ansible-content-collections-all-versions-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Content V3 Plugin Ansible Content Collections API from Red Hat Ansible Automation Platform — 1 operation(s) for api: content v3 plugin ansible content collections.'
  name: 'Red Hat Ansible Automation Platform Api: Content V3 Plugin Ansible Content Collections API'
  slug: red-hat-ansible-automation-platform-api-content-v3-plugin-ansible-content-collections-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Content V3 Plugin Ansible Content Collections Artifacts API from Red Hat Ansible Automation Platform — 1 operation(s) for api: content v3 plugin ansible content collections artifacts.'
  name: 'Red Hat Ansible Automation Platform Api: Content V3 Plugin Ansible Content Collections Artifacts API'
  slug: red-hat-ansible-automation-platform-api-content-v3-plugin-ansible-content-collections-artifacts-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Content V3 Plugin Ansible Content Collections Index API from Red Hat Ansible Automation Platform — 2 operation(s) for api: content v3 plugin ansible content collections index.'
  name: 'Red Hat Ansible Automation Platform Api: Content V3 Plugin Ansible Content Collections Index API'
  slug: red-hat-ansible-automation-platform-api-content-v3-plugin-ansible-content-collections-index-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Content V3 Plugin Ansible Content Collections Index Versions API from Red Hat Ansible Automation Platform — 2 operation(s) for api: content v3 plugin ansible content collections index version'
  name: 'Red Hat Ansible Automation Platform Api: Content V3 Plugin Ansible Content Collections Index Versions API'
  slug: red-hat-ansible-automation-platform-api-content-v3-plugin-ansible-content-collections-index-versions-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Content V3 Plugin Ansible Content Collections Index Versions Docs-Blob API from Red Hat Ansible Automation Platform — 1 operation(s) for api: content v3 plugin ansible content collections ind'
  name: 'Red Hat Ansible Automation Platform Api: Content V3 Plugin Ansible Content Collections Index Versions Docs-Blob API'
  slug: red-hat-ansible-automation-platform-api-content-v3-plugin-ansible-content-collections-index-versions-docs-blob-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Content V3 Plugin Ansible Content Namespaces API from Red Hat Ansible Automation Platform — 2 operation(s) for api: content v3 plugin ansible content namespaces.'
  name: 'Red Hat Ansible Automation Platform Api: Content V3 Plugin Ansible Content Namespaces API'
  slug: red-hat-ansible-automation-platform-api-content-v3-plugin-ansible-content-namespaces-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Content V3 Plugin Ansible Imports Collections API from Red Hat Ansible Automation Platform — 1 operation(s) for api: content v3 plugin ansible imports collections.'
  name: 'Red Hat Ansible Automation Platform Api: Content V3 Plugin Ansible Imports Collections API'
  slug: red-hat-ansible-automation-platform-api-content-v3-plugin-ansible-imports-collections-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Content V3 Plugin Ansible Search Collection-Versions API from Red Hat Ansible Automation Platform — 1 operation(s) for api: content v3 plugin ansible search collection-versions.'
  name: 'Red Hat Ansible Automation Platform Api: Content V3 Plugin Ansible Search Collection-Versions API'
  slug: red-hat-ansible-automation-platform-api-content-v3-plugin-ansible-search-collection-versions-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Content V3 Sync API from Red Hat Ansible Automation Platform — 1 operation(s) for api: content v3 sync.'
  name: 'Red Hat Ansible Automation Platform Api: Content V3 Sync API'
  slug: red-hat-ansible-automation-platform-api-content-v3-sync-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Content V3 Sync Config API from Red Hat Ansible Automation Platform — 1 operation(s) for api: content v3 sync config.'
  name: 'Red Hat Ansible Automation Platform Api: Content V3 Sync Config API'
  slug: red-hat-ansible-automation-platform-api-content-v3-sync-config-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Feature_Flags_State API from Red Hat Ansible Automation Platform — 1 operation(s) for api: feature_flags_state.'
  name: 'Red Hat Ansible Automation Platform Api: Feature_Flags_State API'
  slug: red-hat-ansible-automation-platform-api-feature-flags-state-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Service-Index API from Red Hat Ansible Automation Platform — 1 operation(s) for api: service-index.'
  name: 'Red Hat Ansible Automation Platform Api: Service-Index API'
  slug: red-hat-ansible-automation-platform-api-service-index-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Service-Index Metadata API from Red Hat Ansible Automation Platform — 1 operation(s) for api: service-index metadata.'
  name: 'Red Hat Ansible Automation Platform Api: Service-Index Metadata API'
  slug: red-hat-ansible-automation-platform-api-service-index-metadata-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Service-Index Object-Delete API from Red Hat Ansible Automation Platform — 1 operation(s) for api: service-index object-delete.'
  name: 'Red Hat Ansible Automation Platform Api: Service-Index Object-Delete API'
  slug: red-hat-ansible-automation-platform-api-service-index-object-delete-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Service-Index Resource-Types API from Red Hat Ansible Automation Platform — 2 operation(s) for api: service-index resource-types.'
  name: 'Red Hat Ansible Automation Platform Api: Service-Index Resource-Types API'
  slug: red-hat-ansible-automation-platform-api-service-index-resource-types-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Service-Index Resource-Types Manifest API from Red Hat Ansible Automation Platform — 1 operation(s) for api: service-index resource-types manifest.'
  name: 'Red Hat Ansible Automation Platform Api: Service-Index Resource-Types Manifest API'
  slug: red-hat-ansible-automation-platform-api-service-index-resource-types-manifest-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Service-Index Resources API from Red Hat Ansible Automation Platform — 2 operation(s) for api: service-index resources.'
  name: 'Red Hat Ansible Automation Platform Api: Service-Index Resources API'
  slug: red-hat-ansible-automation-platform-api-service-index-resources-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Service-Index Role-Permissions API from Red Hat Ansible Automation Platform — 1 operation(s) for api: service-index role-permissions.'
  name: 'Red Hat Ansible Automation Platform Api: Service-Index Role-Permissions API'
  slug: red-hat-ansible-automation-platform-api-service-index-role-permissions-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Service-Index Role-Team-Assignments API from Red Hat Ansible Automation Platform — 1 operation(s) for api: service-index role-team-assignments.'
  name: 'Red Hat Ansible Automation Platform Api: Service-Index Role-Team-Assignments API'
  slug: red-hat-ansible-automation-platform-api-service-index-role-team-assignments-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Service-Index Role-Team-Assignments Assign API from Red Hat Ansible Automation Platform — 1 operation(s) for api: service-index role-team-assignments assign.'
  name: 'Red Hat Ansible Automation Platform Api: Service-Index Role-Team-Assignments Assign API'
  slug: red-hat-ansible-automation-platform-api-service-index-role-team-assignments-assign-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Service-Index Role-Team-Assignments Unassign API from Red Hat Ansible Automation Platform — 1 operation(s) for api: service-index role-team-assignments unassign.'
  name: 'Red Hat Ansible Automation Platform Api: Service-Index Role-Team-Assignments Unassign API'
  slug: red-hat-ansible-automation-platform-api-service-index-role-team-assignments-unassign-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Service-Index Role-Types API from Red Hat Ansible Automation Platform — 1 operation(s) for api: service-index role-types.'
  name: 'Red Hat Ansible Automation Platform Api: Service-Index Role-Types API'
  slug: red-hat-ansible-automation-platform-api-service-index-role-types-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Service-Index Role-User-Assignments API from Red Hat Ansible Automation Platform — 1 operation(s) for api: service-index role-user-assignments.'
  name: 'Red Hat Ansible Automation Platform Api: Service-Index Role-User-Assignments API'
  slug: red-hat-ansible-automation-platform-api-service-index-role-user-assignments-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Service-Index Role-User-Assignments Assign API from Red Hat Ansible Automation Platform — 1 operation(s) for api: service-index role-user-assignments assign.'
  name: 'Red Hat Ansible Automation Platform Api: Service-Index Role-User-Assignments Assign API'
  slug: red-hat-ansible-automation-platform-api-service-index-role-user-assignments-assign-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: Service-Index Role-User-Assignments Unassign API from Red Hat Ansible Automation Platform — 1 operation(s) for api: service-index role-user-assignments unassign.'
  name: 'Red Hat Ansible Automation Platform Api: Service-Index Role-User-Assignments Unassign API'
  slug: red-hat-ansible-automation-platform-api-service-index-role-user-assignments-unassign-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui API from Red Hat Ansible Automation Platform — 1 operation(s) for api: _ui.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui API'
  slug: red-hat-ansible-automation-platform-api-ui-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui V1 Auth Login API from Red Hat Ansible Automation Platform — 1 operation(s) for api: _ui v1 auth login.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui V1 Auth Login API'
  slug: red-hat-ansible-automation-platform-api-ui-v1-auth-login-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui V1 Auth Logout API from Red Hat Ansible Automation Platform — 1 operation(s) for api: _ui v1 auth logout.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui V1 Auth Logout API'
  slug: red-hat-ansible-automation-platform-api-ui-v1-auth-logout-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui V1 Collection_Signing API from Red Hat Ansible Automation Platform — 5 operation(s) for api: _ui v1 collection_signing.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui V1 Collection_Signing API'
  slug: red-hat-ansible-automation-platform-api-ui-v1-collection-signing-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui V1 Collection-Versions API from Red Hat Ansible Automation Platform — 2 operation(s) for api: _ui v1 collection-versions.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui V1 Collection-Versions API'
  slug: red-hat-ansible-automation-platform-api-ui-v1-collection-versions-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui V1 Controllers API from Red Hat Ansible Automation Platform — 1 operation(s) for api: _ui v1 controllers.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui V1 Controllers API'
  slug: red-hat-ansible-automation-platform-api-ui-v1-controllers-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui V1 Distributions API from Red Hat Ansible Automation Platform — 2 operation(s) for api: _ui v1 distributions.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui V1 Distributions API'
  slug: red-hat-ansible-automation-platform-api-ui-v1-distributions-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui V1 Feature-Flags API from Red Hat Ansible Automation Platform — 1 operation(s) for api: _ui v1 feature-flags.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui V1 Feature-Flags API'
  slug: red-hat-ansible-automation-platform-api-ui-v1-feature-flags-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui V1 Imports Collections API from Red Hat Ansible Automation Platform — 2 operation(s) for api: _ui v1 imports collections.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui V1 Imports Collections API'
  slug: red-hat-ansible-automation-platform-api-ui-v1-imports-collections-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui V1 Landing-Page API from Red Hat Ansible Automation Platform — 1 operation(s) for api: _ui v1 landing-page.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui V1 Landing-Page API'
  slug: red-hat-ansible-automation-platform-api-ui-v1-landing-page-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui V1 Me API from Red Hat Ansible Automation Platform — 1 operation(s) for api: _ui v1 me.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui V1 Me API'
  slug: red-hat-ansible-automation-platform-api-ui-v1-me-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui V1 My-Distributions API from Red Hat Ansible Automation Platform — 2 operation(s) for api: _ui v1 my-distributions.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui V1 My-Distributions API'
  slug: red-hat-ansible-automation-platform-api-ui-v1-my-distributions-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui V1 My-Namespaces API from Red Hat Ansible Automation Platform — 2 operation(s) for api: _ui v1 my-namespaces.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui V1 My-Namespaces API'
  slug: red-hat-ansible-automation-platform-api-ui-v1-my-namespaces-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui V1 My-Synclists API from Red Hat Ansible Automation Platform — 2 operation(s) for api: _ui v1 my-synclists.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui V1 My-Synclists API'
  slug: red-hat-ansible-automation-platform-api-ui-v1-my-synclists-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui V1 My-Synclists Curate API from Red Hat Ansible Automation Platform — 1 operation(s) for api: _ui v1 my-synclists curate.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui V1 My-Synclists Curate API'
  slug: red-hat-ansible-automation-platform-api-ui-v1-my-synclists-curate-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui V1 Namespaces API from Red Hat Ansible Automation Platform — 2 operation(s) for api: _ui v1 namespaces.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui V1 Namespaces API'
  slug: red-hat-ansible-automation-platform-api-ui-v1-namespaces-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui V1 Remotes API from Red Hat Ansible Automation Platform — 2 operation(s) for api: _ui v1 remotes.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui V1 Remotes API'
  slug: red-hat-ansible-automation-platform-api-ui-v1-remotes-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui V1 Repo API from Red Hat Ansible Automation Platform — 2 operation(s) for api: _ui v1 repo.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui V1 Repo API'
  slug: red-hat-ansible-automation-platform-api-ui-v1-repo-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui V1 Search API from Red Hat Ansible Automation Platform — 1 operation(s) for api: _ui v1 search.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui V1 Search API'
  slug: red-hat-ansible-automation-platform-api-ui-v1-search-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui V1 Settings API from Red Hat Ansible Automation Platform — 1 operation(s) for api: _ui v1 settings.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui V1 Settings API'
  slug: red-hat-ansible-automation-platform-api-ui-v1-settings-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui V1 Synclists API from Red Hat Ansible Automation Platform — 2 operation(s) for api: _ui v1 synclists.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui V1 Synclists API'
  slug: red-hat-ansible-automation-platform-api-ui-v1-synclists-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui V1 Tags API from Red Hat Ansible Automation Platform — 1 operation(s) for api: _ui v1 tags.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui V1 Tags API'
  slug: red-hat-ansible-automation-platform-api-ui-v1-tags-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui V1 Tags Collections API from Red Hat Ansible Automation Platform — 1 operation(s) for api: _ui v1 tags collections.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui V1 Tags Collections API'
  slug: red-hat-ansible-automation-platform-api-ui-v1-tags-collections-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui V1 Tags Roles API from Red Hat Ansible Automation Platform — 1 operation(s) for api: _ui v1 tags roles.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui V1 Tags Roles API'
  slug: red-hat-ansible-automation-platform-api-ui-v1-tags-roles-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui V1 Users API from Red Hat Ansible Automation Platform — 2 operation(s) for api: _ui v1 users.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui V1 Users API'
  slug: red-hat-ansible-automation-platform-api-ui-v1-users-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui V2 Groups API from Red Hat Ansible Automation Platform — 2 operation(s) for api: _ui v2 groups.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui V2 Groups API'
  slug: red-hat-ansible-automation-platform-api-ui-v2-groups-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui V2 Me API from Red Hat Ansible Automation Platform — 1 operation(s) for api: _ui v2 me.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui V2 Me API'
  slug: red-hat-ansible-automation-platform-api-ui-v2-me-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui V2 Organizations API from Red Hat Ansible Automation Platform — 2 operation(s) for api: _ui v2 organizations.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui V2 Organizations API'
  slug: red-hat-ansible-automation-platform-api-ui-v2-organizations-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui V2 Role_Definitions API from Red Hat Ansible Automation Platform — 2 operation(s) for api: _ui v2 role_definitions.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui V2 Role_Definitions API'
  slug: red-hat-ansible-automation-platform-api-ui-v2-role-definitions-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui V2 Role_Definitions Team_Assignments API from Red Hat Ansible Automation Platform — 1 operation(s) for api: _ui v2 role_definitions team_assignments.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui V2 Role_Definitions Team_Assignments API'
  slug: red-hat-ansible-automation-platform-api-ui-v2-role-definitions-team-assignments-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui V2 Role_Definitions User_Assignments API from Red Hat Ansible Automation Platform — 1 operation(s) for api: _ui v2 role_definitions user_assignments.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui V2 Role_Definitions User_Assignments API'
  slug: red-hat-ansible-automation-platform-api-ui-v2-role-definitions-user-assignments-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui V2 Role_Metadata API from Red Hat Ansible Automation Platform — 1 operation(s) for api: _ui v2 role_metadata.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui V2 Role_Metadata API'
  slug: red-hat-ansible-automation-platform-api-ui-v2-role-metadata-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui V2 Role_Team_Access API from Red Hat Ansible Automation Platform — 2 operation(s) for api: _ui v2 role_team_access.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui V2 Role_Team_Access API'
  slug: red-hat-ansible-automation-platform-api-ui-v2-role-team-access-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui V2 Role_Team_Assignments API from Red Hat Ansible Automation Platform — 2 operation(s) for api: _ui v2 role_team_assignments.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui V2 Role_Team_Assignments API'
  slug: red-hat-ansible-automation-platform-api-ui-v2-role-team-assignments-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui V2 Role_User_Access API from Red Hat Ansible Automation Platform — 2 operation(s) for api: _ui v2 role_user_access.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui V2 Role_User_Access API'
  slug: red-hat-ansible-automation-platform-api-ui-v2-role-user-access-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui V2 Role_User_Assignments API from Red Hat Ansible Automation Platform — 2 operation(s) for api: _ui v2 role_user_assignments.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui V2 Role_User_Assignments API'
  slug: red-hat-ansible-automation-platform-api-ui-v2-role-user-assignments-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui V2 Teams API from Red Hat Ansible Automation Platform — 2 operation(s) for api: _ui v2 teams.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui V2 Teams API'
  slug: red-hat-ansible-automation-platform-api-ui-v2-teams-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: _Ui V2 Users API from Red Hat Ansible Automation Platform — 2 operation(s) for api: _ui v2 users.'
  name: 'Red Hat Ansible Automation Platform Api: _Ui V2 Users API'
  slug: red-hat-ansible-automation-platform-api-ui-v2-users-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: V3 API from Red Hat Ansible Automation Platform — 1 operation(s) for api: v3.'
  name: 'Red Hat Ansible Automation Platform Api: V3 API'
  slug: red-hat-ansible-automation-platform-api-v3-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: V3 Artifacts Collections API from Red Hat Ansible Automation Platform — 1 operation(s) for api: v3 artifacts collections.'
  name: 'Red Hat Ansible Automation Platform Api: V3 Artifacts Collections API'
  slug: red-hat-ansible-automation-platform-api-v3-artifacts-collections-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: V3 Auth Token API from Red Hat Ansible Automation Platform — 1 operation(s) for api: v3 auth token.'
  name: 'Red Hat Ansible Automation Platform Api: V3 Auth Token API'
  slug: red-hat-ansible-automation-platform-api-v3-auth-token-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: V3 Collection_Versions All API from Red Hat Ansible Automation Platform — 1 operation(s) for api: v3 collection_versions all.'
  name: 'Red Hat Ansible Automation Platform Api: V3 Collection_Versions All API'
  slug: red-hat-ansible-automation-platform-api-v3-collection-versions-all-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: V3 Collections All API from Red Hat Ansible Automation Platform — 1 operation(s) for api: v3 collections all.'
  name: 'Red Hat Ansible Automation Platform Api: V3 Collections All API'
  slug: red-hat-ansible-automation-platform-api-v3-collections-all-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: V3 Collections API from Red Hat Ansible Automation Platform — 2 operation(s) for api: v3 collections.'
  name: 'Red Hat Ansible Automation Platform Api: V3 Collections API'
  slug: red-hat-ansible-automation-platform-api-v3-collections-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: V3 Collections Versions API from Red Hat Ansible Automation Platform — 2 operation(s) for api: v3 collections versions.'
  name: 'Red Hat Ansible Automation Platform Api: V3 Collections Versions API'
  slug: red-hat-ansible-automation-platform-api-v3-collections-versions-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: V3 Collections Versions Copy API from Red Hat Ansible Automation Platform — 1 operation(s) for api: v3 collections versions copy.'
  name: 'Red Hat Ansible Automation Platform Api: V3 Collections Versions Copy API'
  slug: red-hat-ansible-automation-platform-api-v3-collections-versions-copy-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: V3 Collections Versions Docs-Blob API from Red Hat Ansible Automation Platform — 1 operation(s) for api: v3 collections versions docs-blob.'
  name: 'Red Hat Ansible Automation Platform Api: V3 Collections Versions Docs-Blob API'
  slug: red-hat-ansible-automation-platform-api-v3-collections-versions-docs-blob-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: V3 Collections Versions Move API from Red Hat Ansible Automation Platform — 1 operation(s) for api: v3 collections versions move.'
  name: 'Red Hat Ansible Automation Platform Api: V3 Collections Versions Move API'
  slug: red-hat-ansible-automation-platform-api-v3-collections-versions-move-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: V3 Excludes API from Red Hat Ansible Automation Platform — 1 operation(s) for api: v3 excludes.'
  name: 'Red Hat Ansible Automation Platform Api: V3 Excludes API'
  slug: red-hat-ansible-automation-platform-api-v3-excludes-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: V3 Imports Collections API from Red Hat Ansible Automation Platform — 1 operation(s) for api: v3 imports collections.'
  name: 'Red Hat Ansible Automation Platform Api: V3 Imports Collections API'
  slug: red-hat-ansible-automation-platform-api-v3-imports-collections-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: V3 Namespaces API from Red Hat Ansible Automation Platform — 2 operation(s) for api: v3 namespaces.'
  name: 'Red Hat Ansible Automation Platform Api: V3 Namespaces API'
  slug: red-hat-ansible-automation-platform-api-v3-namespaces-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: V3 Openapi.Json API from Red Hat Ansible Automation Platform — 1 operation(s) for api: v3 openapi.json.'
  name: 'Red Hat Ansible Automation Platform Api: V3 Openapi.Json API'
  slug: red-hat-ansible-automation-platform-api-v3-openapi-json-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: V3 Openapi.Yaml API from Red Hat Ansible Automation Platform — 1 operation(s) for api: v3 openapi.yaml.'
  name: 'Red Hat Ansible Automation Platform Api: V3 Openapi.Yaml API'
  slug: red-hat-ansible-automation-platform-api-v3-openapi-yaml-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: V3 Plugin Ansible Client-Configuration API from Red Hat Ansible Automation Platform — 1 operation(s) for api: v3 plugin ansible client-configuration.'
  name: 'Red Hat Ansible Automation Platform Api: V3 Plugin Ansible Client-Configuration API'
  slug: red-hat-ansible-automation-platform-api-v3-plugin-ansible-client-configuration-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: V3 Plugin Ansible Content Collections All-Collections API from Red Hat Ansible Automation Platform — 1 operation(s) for api: v3 plugin ansible content collections all-collections.'
  name: 'Red Hat Ansible Automation Platform Api: V3 Plugin Ansible Content Collections All-Collections API'
  slug: red-hat-ansible-automation-platform-api-v3-plugin-ansible-content-collections-all-collections-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: V3 Plugin Ansible Content Collections All-Versions API from Red Hat Ansible Automation Platform — 1 operation(s) for api: v3 plugin ansible content collections all-versions.'
  name: 'Red Hat Ansible Automation Platform Api: V3 Plugin Ansible Content Collections All-Versions API'
  slug: red-hat-ansible-automation-platform-api-v3-plugin-ansible-content-collections-all-versions-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: V3 Plugin Ansible Content Collections API from Red Hat Ansible Automation Platform — 1 operation(s) for api: v3 plugin ansible content collections.'
  name: 'Red Hat Ansible Automation Platform Api: V3 Plugin Ansible Content Collections API'
  slug: red-hat-ansible-automation-platform-api-v3-plugin-ansible-content-collections-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: V3 Plugin Ansible Content Collections Artifacts API from Red Hat Ansible Automation Platform — 1 operation(s) for api: v3 plugin ansible content collections artifacts.'
  name: 'Red Hat Ansible Automation Platform Api: V3 Plugin Ansible Content Collections Artifacts API'
  slug: red-hat-ansible-automation-platform-api-v3-plugin-ansible-content-collections-artifacts-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: V3 Plugin Ansible Content Collections Index API from Red Hat Ansible Automation Platform — 2 operation(s) for api: v3 plugin ansible content collections index.'
  name: 'Red Hat Ansible Automation Platform Api: V3 Plugin Ansible Content Collections Index API'
  slug: red-hat-ansible-automation-platform-api-v3-plugin-ansible-content-collections-index-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: V3 Plugin Ansible Content Collections Index Versions API from Red Hat Ansible Automation Platform — 2 operation(s) for api: v3 plugin ansible content collections index versions.'
  name: 'Red Hat Ansible Automation Platform Api: V3 Plugin Ansible Content Collections Index Versions API'
  slug: red-hat-ansible-automation-platform-api-v3-plugin-ansible-content-collections-index-versions-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: V3 Plugin Ansible Content Collections Index Versions Docs-Blob API from Red Hat Ansible Automation Platform — 1 operation(s) for api: v3 plugin ansible content collections index versions docs'
  name: 'Red Hat Ansible Automation Platform Api: V3 Plugin Ansible Content Collections Index Versions Docs-Blob API'
  slug: red-hat-ansible-automation-platform-api-v3-plugin-ansible-content-collections-index-versions-docs-blob-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: V3 Plugin Ansible Content Namespaces API from Red Hat Ansible Automation Platform — 2 operation(s) for api: v3 plugin ansible content namespaces.'
  name: 'Red Hat Ansible Automation Platform Api: V3 Plugin Ansible Content Namespaces API'
  slug: red-hat-ansible-automation-platform-api-v3-plugin-ansible-content-namespaces-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: V3 Plugin Ansible Imports Collections API from Red Hat Ansible Automation Platform — 1 operation(s) for api: v3 plugin ansible imports collections.'
  name: 'Red Hat Ansible Automation Platform Api: V3 Plugin Ansible Imports Collections API'
  slug: red-hat-ansible-automation-platform-api-v3-plugin-ansible-imports-collections-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Api: V3 Plugin Ansible Search Collection-Versions API from Red Hat Ansible Automation Platform — 1 operation(s) for api: v3 plugin ansible search collection-versions.'
  name: 'Red Hat Ansible Automation Platform Api: V3 Plugin Ansible Search Collection-Versions API'
  slug: red-hat-ansible-automation-platform-api-v3-plugin-ansible-search-collection-versions-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The app_urls API from Red Hat Ansible Automation Platform — 1 operation(s) for app_urls.
  name: Red Hat Ansible Automation Platform App URLS API
  slug: red-hat-ansible-automation-platform-app-urls-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The applications API from Red Hat Ansible Automation Platform — 3 operation(s) for applications.
  name: Red Hat Ansible Automation Platform Applications API
  slug: red-hat-ansible-automation-platform-applications-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The Artifacts API from Red Hat Ansible Automation Platform — 2 operation(s) for artifacts.
  name: Red Hat Ansible Automation Platform Artifacts API
  slug: red-hat-ansible-automation-platform-artifacts-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The audit-rules API from Red Hat Ansible Automation Platform — 4 operation(s) for audit-rules.
  name: Red Hat Ansible Automation Platform Audit Rules API
  slug: red-hat-ansible-automation-platform-audit-rules-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The auth API from Red Hat Ansible Automation Platform — 3 operation(s) for auth.
  name: Red Hat Ansible Automation Platform Auth API
  slug: red-hat-ansible-automation-platform-auth-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The authenticator_maps API from Red Hat Ansible Automation Platform — 5 operation(s) for authenticator_maps.
  name: Red Hat Ansible Automation Platform Authenticator Maps API
  slug: red-hat-ansible-automation-platform-authenticator-maps-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The authenticator_plugins API from Red Hat Ansible Automation Platform — 1 operation(s) for authenticator_plugins.
  name: Red Hat Ansible Automation Platform Authenticator Plugins API
  slug: red-hat-ansible-automation-platform-authenticator-plugins-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The authenticator_users API from Red Hat Ansible Automation Platform — 3 operation(s) for authenticator_users.
  name: Red Hat Ansible Automation Platform Authenticator Users API
  slug: red-hat-ansible-automation-platform-authenticator-users-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The authenticators API from Red Hat Ansible Automation Platform — 4 operation(s) for authenticators.
  name: Red Hat Ansible Automation Platform Authenticators API
  slug: red-hat-ansible-automation-platform-authenticators-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The AWX API API from Red Hat Ansible Automation Platform — 1 operation(s) for awx api.
  name: Red Hat Ansible Automation Platform AWX API
  slug: red-hat-ansible-automation-platform-awx-api-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The bulk API from Red Hat Ansible Automation Platform — 4 operation(s) for bulk.
  name: Red Hat Ansible Automation Platform Bulk API
  slug: red-hat-ansible-automation-platform-bulk-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The config API from Red Hat Ansible Automation Platform — 4 operation(s) for config.
  name: Red Hat Ansible Automation Platform Config API
  slug: red-hat-ansible-automation-platform-config-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The constructed_inventories API from Red Hat Ansible Automation Platform — 2 operation(s) for constructed_inventories.
  name: Red Hat Ansible Automation Platform Constructed Inventories API
  slug: red-hat-ansible-automation-platform-constructed-inventories-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The Content API from Red Hat Ansible Automation Platform — 1 operation(s) for content.
  name: Red Hat Ansible Automation Platform Content API
  slug: red-hat-ansible-automation-platform-content-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Content: Blobs API from Red Hat Ansible Automation Platform — 2 operation(s) for content: blobs.'
  name: 'Red Hat Ansible Automation Platform Content: Blobs API'
  slug: red-hat-ansible-automation-platform-content-blobs-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Content: Collection_Deprecations API from Red Hat Ansible Automation Platform — 2 operation(s) for content: collection_deprecations.'
  name: 'Red Hat Ansible Automation Platform Content: Collection_Deprecations API'
  slug: red-hat-ansible-automation-platform-content-collection-deprecations-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Content: Collection_Marks API from Red Hat Ansible Automation Platform — 2 operation(s) for content: collection_marks.'
  name: 'Red Hat Ansible Automation Platform Content: Collection_Marks API'
  slug: red-hat-ansible-automation-platform-content-collection-marks-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Content: Collection_Signatures API from Red Hat Ansible Automation Platform — 2 operation(s) for content: collection_signatures.'
  name: 'Red Hat Ansible Automation Platform Content: Collection_Signatures API'
  slug: red-hat-ansible-automation-platform-content-collection-signatures-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Content: Collection_Versions API from Red Hat Ansible Automation Platform — 2 operation(s) for content: collection_versions.'
  name: 'Red Hat Ansible Automation Platform Content: Collection_Versions API'
  slug: red-hat-ansible-automation-platform-content-collection-versions-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Content: Files API from Red Hat Ansible Automation Platform — 2 operation(s) for content: files.'
  name: 'Red Hat Ansible Automation Platform Content: Files API'
  slug: red-hat-ansible-automation-platform-content-files-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Content: Manifests API from Red Hat Ansible Automation Platform — 2 operation(s) for content: manifests.'
  name: 'Red Hat Ansible Automation Platform Content: Manifests API'
  slug: red-hat-ansible-automation-platform-content-manifests-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Content: Namespaces API from Red Hat Ansible Automation Platform — 3 operation(s) for content: namespaces.'
  name: 'Red Hat Ansible Automation Platform Content: Namespaces API'
  slug: red-hat-ansible-automation-platform-content-namespaces-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Content: Roles API from Red Hat Ansible Automation Platform — 2 operation(s) for content: roles.'
  name: 'Red Hat Ansible Automation Platform Content: Roles API'
  slug: red-hat-ansible-automation-platform-content-roles-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Content: Signatures API from Red Hat Ansible Automation Platform — 2 operation(s) for content: signatures.'
  name: 'Red Hat Ansible Automation Platform Content: Signatures API'
  slug: red-hat-ansible-automation-platform-content-signatures-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Content: Tags API from Red Hat Ansible Automation Platform — 2 operation(s) for content: tags.'
  name: 'Red Hat Ansible Automation Platform Content: Tags API'
  slug: red-hat-ansible-automation-platform-content-tags-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The Contentguards API from Red Hat Ansible Automation Platform — 1 operation(s) for contentguards.
  name: Red Hat Ansible Automation Platform Contentguards API
  slug: red-hat-ansible-automation-platform-contentguards-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Contentguards: Composite API from Red Hat Ansible Automation Platform — 6 operation(s) for contentguards: composite.'
  name: 'Red Hat Ansible Automation Platform Contentguards: Composite API'
  slug: red-hat-ansible-automation-platform-contentguards-composite-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Contentguards: Content_Redirect API from Red Hat Ansible Automation Platform — 6 operation(s) for contentguards: content_redirect.'
  name: 'Red Hat Ansible Automation Platform Contentguards: Content_Redirect API'
  slug: red-hat-ansible-automation-platform-contentguards-content-redirect-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Contentguards: Header API from Red Hat Ansible Automation Platform — 6 operation(s) for contentguards: header.'
  name: 'Red Hat Ansible Automation Platform Contentguards: Header API'
  slug: red-hat-ansible-automation-platform-contentguards-header-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Contentguards: Rbac API from Red Hat Ansible Automation Platform — 6 operation(s) for contentguards: rbac.'
  name: 'Red Hat Ansible Automation Platform Contentguards: Rbac API'
  slug: red-hat-ansible-automation-platform-contentguards-rbac-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Contentguards: Rhsm API from Red Hat Ansible Automation Platform — 2 operation(s) for contentguards: rhsm.'
  name: 'Red Hat Ansible Automation Platform Contentguards: Rhsm API'
  slug: red-hat-ansible-automation-platform-contentguards-rhsm-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Contentguards: X509 API from Red Hat Ansible Automation Platform — 2 operation(s) for contentguards: x509.'
  name: 'Red Hat Ansible Automation Platform Contentguards: X509 API'
  slug: red-hat-ansible-automation-platform-contentguards-x509-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The credential_input_sources API from Red Hat Ansible Automation Platform — 4 operation(s) for credential_input_sources.
  name: Red Hat Ansible Automation Platform Credential Input Sources API
  slug: red-hat-ansible-automation-platform-credential-input-sources-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The credential_types API from Red Hat Ansible Automation Platform — 8 operation(s) for credential_types.
  name: Red Hat Ansible Automation Platform Credential Types API
  slug: red-hat-ansible-automation-platform-credential-types-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The credentials API from Red Hat Ansible Automation Platform — 10 operation(s) for credentials.
  name: Red Hat Ansible Automation Platform Credentials API
  slug: red-hat-ansible-automation-platform-credentials-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The dashboard API from Red Hat Ansible Automation Platform — 2 operation(s) for dashboard.
  name: Red Hat Ansible Automation Platform Dashboard API
  slug: red-hat-ansible-automation-platform-dashboard-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The decision-environments API from Red Hat Ansible Automation Platform — 2 operation(s) for decision-environments.
  name: Red Hat Ansible Automation Platform Decision Environments API
  slug: red-hat-ansible-automation-platform-decision-environments-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Distributions: Ansible API from Red Hat Ansible Automation Platform — 8 operation(s) for distributions: ansible.'
  name: 'Red Hat Ansible Automation Platform Distributions: Ansible API'
  slug: red-hat-ansible-automation-platform-distributions-ansible-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The Distributions API from Red Hat Ansible Automation Platform — 1 operation(s) for distributions.
  name: Red Hat Ansible Automation Platform Distributions API
  slug: red-hat-ansible-automation-platform-distributions-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Distributions: Artifacts API from Red Hat Ansible Automation Platform — 2 operation(s) for distributions: artifacts.'
  name: 'Red Hat Ansible Automation Platform Distributions: Artifacts API'
  slug: red-hat-ansible-automation-platform-distributions-artifacts-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Distributions: Container API from Red Hat Ansible Automation Platform — 8 operation(s) for distributions: container.'
  name: 'Red Hat Ansible Automation Platform Distributions: Container API'
  slug: red-hat-ansible-automation-platform-distributions-container-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Distributions: File API from Red Hat Ansible Automation Platform — 8 operation(s) for distributions: file.'
  name: 'Red Hat Ansible Automation Platform Distributions: File API'
  slug: red-hat-ansible-automation-platform-distributions-file-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Distributions: Pull-Through API from Red Hat Ansible Automation Platform — 8 operation(s) for distributions: pull-through.'
  name: 'Red Hat Ansible Automation Platform Distributions: Pull-Through API'
  slug: red-hat-ansible-automation-platform-distributions-pull-through-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Docs: Api.Json API from Red Hat Ansible Automation Platform — 1 operation(s) for docs: api.json.'
  name: 'Red Hat Ansible Automation Platform Docs: Api.Json API'
  slug: red-hat-ansible-automation-platform-docs-api-json-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The docs API from Red Hat Ansible Automation Platform — 1 operation(s) for docs.
  name: Red Hat Ansible Automation Platform Docs API
  slug: red-hat-ansible-automation-platform-docs-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Docs: Api.Yaml API from Red Hat Ansible Automation Platform — 1 operation(s) for docs: api.yaml.'
  name: 'Red Hat Ansible Automation Platform Docs: Api.Yaml API'
  slug: red-hat-ansible-automation-platform-docs-api-yaml-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The Domains API from Red Hat Ansible Automation Platform — 2 operation(s) for domains.
  name: Red Hat Ansible Automation Platform Domains API
  slug: red-hat-ansible-automation-platform-domains-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The eda-credentials API from Red Hat Ansible Automation Platform — 5 operation(s) for eda-credentials.
  name: Red Hat Ansible Automation Platform Eda Credentials API
  slug: red-hat-ansible-automation-platform-eda-credentials-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The event-streams API from Red Hat Ansible Automation Platform — 3 operation(s) for event-streams.
  name: Red Hat Ansible Automation Platform Event Streams API
  slug: red-hat-ansible-automation-platform-event-streams-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The execution_environments API from Red Hat Ansible Automation Platform — 5 operation(s) for execution_environments.
  name: Red Hat Ansible Automation Platform Execution Environments API
  slug: red-hat-ansible-automation-platform-execution-environments-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Exporters: Filesystem API from Red Hat Ansible Automation Platform — 2 operation(s) for exporters: filesystem.'
  name: 'Red Hat Ansible Automation Platform Exporters: Filesystem API'
  slug: red-hat-ansible-automation-platform-exporters-filesystem-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Exporters: Filesystem Exports API from Red Hat Ansible Automation Platform — 2 operation(s) for exporters: filesystem exports.'
  name: 'Red Hat Ansible Automation Platform Exporters: Filesystem Exports API'
  slug: red-hat-ansible-automation-platform-exporters-filesystem-exports-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Exporters: Pulp API from Red Hat Ansible Automation Platform — 2 operation(s) for exporters: pulp.'
  name: 'Red Hat Ansible Automation Platform Exporters: Pulp API'
  slug: red-hat-ansible-automation-platform-exporters-pulp-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Exporters: Pulp Exports API from Red Hat Ansible Automation Platform — 2 operation(s) for exporters: pulp exports.'
  name: 'Red Hat Ansible Automation Platform Exporters: Pulp Exports API'
  slug: red-hat-ansible-automation-platform-exporters-pulp-exports-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The feature_flags API from Red Hat Ansible Automation Platform — 8 operation(s) for feature_flags.
  name: Red Hat Ansible Automation Platform Feature Flags API
  slug: red-hat-ansible-automation-platform-feature-flags-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The feature_flags_state API from Red Hat Ansible Automation Platform — 3 operation(s) for feature_flags_state.
  name: Red Hat Ansible Automation Platform Feature Flags State API
  slug: red-hat-ansible-automation-platform-feature-flags-state-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Galaxy_Ng: Container-Distribution-Proxy API from Red Hat Ansible Automation Platform — 1 operation(s) for galaxy_ng: container-distribution-proxy.'
  name: 'Red Hat Ansible Automation Platform Galaxy_Ng: Container-Distribution-Proxy API'
  slug: red-hat-ansible-automation-platform-galaxy-ng-container-distribution-proxy-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Galaxy_Ng: Registry-Remote API from Red Hat Ansible Automation Platform — 1 operation(s) for galaxy_ng: registry-remote.'
  name: 'Red Hat Ansible Automation Platform Galaxy_Ng: Registry-Remote API'
  slug: red-hat-ansible-automation-platform-galaxy-ng-registry-remote-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The Gateway API from Red Hat Ansible Automation Platform — 1 operation(s) for gateway.
  name: Red Hat Ansible Automation Platform Gateway API
  slug: red-hat-ansible-automation-platform-gateway-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The groups API from Red Hat Ansible Automation Platform — 20 operation(s) for groups.
  name: Red Hat Ansible Automation Platform Groups API
  slug: red-hat-ansible-automation-platform-groups-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Groups: Roles API from Red Hat Ansible Automation Platform — 2 operation(s) for groups: roles.'
  name: 'Red Hat Ansible Automation Platform Groups: Roles API'
  slug: red-hat-ansible-automation-platform-groups-roles-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Groups: Users API from Red Hat Ansible Automation Platform — 4 operation(s) for groups: users.'
  name: 'Red Hat Ansible Automation Platform Groups: Users API'
  slug: red-hat-ansible-automation-platform-groups-users-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The health API from Red Hat Ansible Automation Platform — 3 operation(s) for health.
  name: Red Hat Ansible Automation Platform Health API
  slug: red-hat-ansible-automation-platform-health-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The host_metric_summary_monthly API from Red Hat Ansible Automation Platform — 1 operation(s) for host_metric_summary_monthly.
  name: Red Hat Ansible Automation Platform Host Metric Summary Monthly API
  slug: red-hat-ansible-automation-platform-host-metric-summary-monthly-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The host_metrics API from Red Hat Ansible Automation Platform — 2 operation(s) for host_metrics.
  name: Red Hat Ansible Automation Platform Host Metrics API
  slug: red-hat-ansible-automation-platform-host-metrics-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The hosts API from Red Hat Ansible Automation Platform — 13 operation(s) for hosts.
  name: Red Hat Ansible Automation Platform Hosts API
  slug: red-hat-ansible-automation-platform-hosts-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The http_ports API from Red Hat Ansible Automation Platform — 5 operation(s) for http_ports.
  name: Red Hat Ansible Automation Platform HTTP Ports API
  slug: red-hat-ansible-automation-platform-http-ports-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Importers: Pulp API from Red Hat Ansible Automation Platform — 2 operation(s) for importers: pulp.'
  name: 'Red Hat Ansible Automation Platform Importers: Pulp API'
  slug: red-hat-ansible-automation-platform-importers-pulp-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Importers: Pulp Import-Check API from Red Hat Ansible Automation Platform — 1 operation(s) for importers: pulp import-check.'
  name: 'Red Hat Ansible Automation Platform Importers: Pulp Import-Check API'
  slug: red-hat-ansible-automation-platform-importers-pulp-import-check-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Importers: Pulp Imports API from Red Hat Ansible Automation Platform — 2 operation(s) for importers: pulp imports.'
  name: 'Red Hat Ansible Automation Platform Importers: Pulp Imports API'
  slug: red-hat-ansible-automation-platform-importers-pulp-imports-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The instance_groups API from Red Hat Ansible Automation Platform — 6 operation(s) for instance_groups.
  name: Red Hat Ansible Automation Platform Instance Groups API
  slug: red-hat-ansible-automation-platform-instance-groups-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The instances API from Red Hat Ansible Automation Platform — 8 operation(s) for instances.
  name: Red Hat Ansible Automation Platform Instances API
  slug: red-hat-ansible-automation-platform-instances-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The inventories API from Red Hat Ansible Automation Platform — 19 operation(s) for inventories.
  name: Red Hat Ansible Automation Platform Inventories API
  slug: red-hat-ansible-automation-platform-inventories-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The inventory_sources API from Red Hat Ansible Automation Platform — 12 operation(s) for inventory_sources.
  name: Red Hat Ansible Automation Platform Inventory Sources API
  slug: red-hat-ansible-automation-platform-inventory-sources-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The inventory_updates API from Red Hat Ansible Automation Platform — 7 operation(s) for inventory_updates.
  name: Red Hat Ansible Automation Platform Inventory Updates API
  slug: red-hat-ansible-automation-platform-inventory-updates-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The job_events API from Red Hat Ansible Automation Platform — 2 operation(s) for job_events.
  name: Red Hat Ansible Automation Platform Job Events API
  slug: red-hat-ansible-automation-platform-job-events-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The job_host_summaries API from Red Hat Ansible Automation Platform — 1 operation(s) for job_host_summaries.
  name: Red Hat Ansible Automation Platform Job Host Summaries API
  slug: red-hat-ansible-automation-platform-job-host-summaries-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The job_templates API from Red Hat Ansible Automation Platform — 22 operation(s) for job_templates.
  name: Red Hat Ansible Automation Platform Job Templates API
  slug: red-hat-ansible-automation-platform-job-templates-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The jobs API from Red Hat Ansible Automation Platform — 13 operation(s) for jobs.
  name: Red Hat Ansible Automation Platform Jobs API
  slug: red-hat-ansible-automation-platform-jobs-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The jwt_claims API from Red Hat Ansible Automation Platform — 1 operation(s) for jwt_claims.
  name: Red Hat Ansible Automation Platform JWT Claims API
  slug: red-hat-ansible-automation-platform-jwt-claims-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The jwt_key API from Red Hat Ansible Automation Platform — 1 operation(s) for jwt_key.
  name: Red Hat Ansible Automation Platform JWT Key API
  slug: red-hat-ansible-automation-platform-jwt-key-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The labels API from Red Hat Ansible Automation Platform — 2 operation(s) for labels.
  name: Red Hat Ansible Automation Platform Labels API
  slug: red-hat-ansible-automation-platform-labels-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: Authenticated user information
  name: Red Hat Ansible Automation Platform Me API
  slug: red-hat-ansible-automation-platform-me-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The mesh_visualizer API from Red Hat Ansible Automation Platform — 1 operation(s) for mesh_visualizer.
  name: Red Hat Ansible Automation Platform Mesh Visualizer API
  slug: red-hat-ansible-automation-platform-mesh-visualizer-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The metrics API from Red Hat Ansible Automation Platform — 1 operation(s) for metrics.
  name: Red Hat Ansible Automation Platform Metrics API
  slug: red-hat-ansible-automation-platform-metrics-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The notification_templates API from Red Hat Ansible Automation Platform — 5 operation(s) for notification_templates.
  name: Red Hat Ansible Automation Platform Notification Templates API
  slug: red-hat-ansible-automation-platform-notification-templates-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The notifications API from Red Hat Ansible Automation Platform — 2 operation(s) for notifications.
  name: Red Hat Ansible Automation Platform Notifications API
  slug: red-hat-ansible-automation-platform-notifications-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The organizations API from Red Hat Ansible Automation Platform — 33 operation(s) for organizations.
  name: Red Hat Ansible Automation Platform Organizations API
  slug: red-hat-ansible-automation-platform-organizations-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The Orphans API from Red Hat Ansible Automation Platform — 1 operation(s) for orphans.
  name: Red Hat Ansible Automation Platform Orphans API
  slug: red-hat-ansible-automation-platform-orphans-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Orphans: Cleanup API from Red Hat Ansible Automation Platform — 1 operation(s) for orphans: cleanup.'
  name: 'Red Hat Ansible Automation Platform Orphans: Cleanup API'
  slug: red-hat-ansible-automation-platform-orphans-cleanup-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The ping API from Red Hat Ansible Automation Platform — 2 operation(s) for ping.
  name: Red Hat Ansible Automation Platform Ping API
  slug: red-hat-ansible-automation-platform-ping-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The project_updates API from Red Hat Ansible Automation Platform — 7 operation(s) for project_updates.
  name: Red Hat Ansible Automation Platform Project Updates API
  slug: red-hat-ansible-automation-platform-project-updates-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The projects API from Red Hat Ansible Automation Platform — 19 operation(s) for projects.
  name: Red Hat Ansible Automation Platform Projects API
  slug: red-hat-ansible-automation-platform-projects-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The Publications API from Red Hat Ansible Automation Platform — 1 operation(s) for publications.
  name: Red Hat Ansible Automation Platform Publications API
  slug: red-hat-ansible-automation-platform-publications-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Publications: File API from Red Hat Ansible Automation Platform — 6 operation(s) for publications: file.'
  name: 'Red Hat Ansible Automation Platform Publications: File API'
  slug: red-hat-ansible-automation-platform-publications-file-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Api API from Red Hat Ansible Automation Platform — 1 operation(s) for pulp_ansible: api.'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-api-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Api V1 Roles API from Red Hat Ansible Automation Platform — 1 operation(s) for pulp_ansible: api v1 roles.'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Api V1 Roles API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-api-v1-roles-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Api V1 Roles Versions API from Red Hat Ansible Automation Platform — 1 operation(s) for pulp_ansible: api v1 roles versions.'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Api V1 Roles Versions API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-api-v1-roles-versions-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Api V3 API from Red Hat Ansible Automation Platform — 1 operation(s) for pulp_ansible: api v3.'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Api V3 API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-api-v3-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Api V3 Artifacts Collections API from Red Hat Ansible Automation Platform — 1 operation(s) for pulp_ansible: api v3 artifacts collections.'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Api V3 Artifacts Collections API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-api-v3-artifacts-collections-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Api V3 Collection_Versions All API from Red Hat Ansible Automation Platform — 1 operation(s) for pulp_ansible: api v3 collection_versions all.'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Api V3 Collection_Versions All API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-api-v3-collection-versions-all-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Api V3 Collections All API from Red Hat Ansible Automation Platform — 1 operation(s) for pulp_ansible: api v3 collections all.'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Api V3 Collections All API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-api-v3-collections-all-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Api V3 Collections API from Red Hat Ansible Automation Platform — 2 operation(s) for pulp_ansible: api v3 collections.'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Api V3 Collections API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-api-v3-collections-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Api V3 Collections Versions API from Red Hat Ansible Automation Platform — 2 operation(s) for pulp_ansible: api v3 collections versions.'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Api V3 Collections Versions API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-api-v3-collections-versions-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Api V3 Collections Versions Docs-Blob API from Red Hat Ansible Automation Platform — 1 operation(s) for pulp_ansible: api v3 collections versions docs-blob.'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Api V3 Collections Versions Docs-Blob API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-api-v3-collections-versions-docs-blob-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Api V3 Imports Collections API from Red Hat Ansible Automation Platform — 1 operation(s) for pulp_ansible: api v3 imports collections.'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Api V3 Imports Collections API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-api-v3-imports-collections-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Api V3 Namespaces API from Red Hat Ansible Automation Platform — 2 operation(s) for pulp_ansible: api v3 namespaces.'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Api V3 Namespaces API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-api-v3-namespaces-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Api V3 Plugin Ansible Client-Configuration API from Red Hat Ansible Automation Platform — 1 operation(s) for pulp_ansible: api v3 plugin ansible client-configuration.'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Api V3 Plugin Ansible Client-Configuration API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-api-v3-plugin-ansible-client-configuration-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Api V3 Plugin Ansible Content Collections All-Collections API from Red Hat Ansible Automation Platform — 1 operation(s) for pulp_ansible: api v3 plugin ansible content collections al'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Api V3 Plugin Ansible Content Collections All-Collections API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-api-v3-plugin-ansible-content-collections-all-collections-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Api V3 Plugin Ansible Content Collections All-Versions API from Red Hat Ansible Automation Platform — 1 operation(s) for pulp_ansible: api v3 plugin ansible content collections all-v'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Api V3 Plugin Ansible Content Collections All-Versions API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-api-v3-plugin-ansible-content-collections-all-versions-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Api V3 Plugin Ansible Content Collections API from Red Hat Ansible Automation Platform — 1 operation(s) for pulp_ansible: api v3 plugin ansible content collections.'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Api V3 Plugin Ansible Content Collections API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-api-v3-plugin-ansible-content-collections-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Api V3 Plugin Ansible Content Collections Artifacts API from Red Hat Ansible Automation Platform — 1 operation(s) for pulp_ansible: api v3 plugin ansible content collections artifact'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Api V3 Plugin Ansible Content Collections Artifacts API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-api-v3-plugin-ansible-content-collections-artifacts-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Api V3 Plugin Ansible Content Collections Index API from Red Hat Ansible Automation Platform — 2 operation(s) for pulp_ansible: api v3 plugin ansible content collections index.'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Api V3 Plugin Ansible Content Collections Index API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-api-v3-plugin-ansible-content-collections-index-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Api V3 Plugin Ansible Content Collections Index Versions API from Red Hat Ansible Automation Platform — 2 operation(s) for pulp_ansible: api v3 plugin ansible content collections ind'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Api V3 Plugin Ansible Content Collections Index Versions API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-api-v3-plugin-ansible-content-collections-index-versions-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Api V3 Plugin Ansible Content Collections Index Versions Docs-Blob API from Red Hat Ansible Automation Platform — 1 operation(s) for pulp_ansible: api v3 plugin ansible content colle'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Api V3 Plugin Ansible Content Collections Index Versions Docs-Blob API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-api-v3-plugin-ansible-content-collections-index-versions-docs-blob-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Api V3 Plugin Ansible Content Namespaces API from Red Hat Ansible Automation Platform — 2 operation(s) for pulp_ansible: api v3 plugin ansible content namespaces.'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Api V3 Plugin Ansible Content Namespaces API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-api-v3-plugin-ansible-content-namespaces-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Api V3 Plugin Ansible Imports Collections API from Red Hat Ansible Automation Platform — 1 operation(s) for pulp_ansible: api v3 plugin ansible imports collections.'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Api V3 Plugin Ansible Imports Collections API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-api-v3-plugin-ansible-imports-collections-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Api V3 Plugin Ansible Search Collection-Versions API from Red Hat Ansible Automation Platform — 1 operation(s) for pulp_ansible: api v3 plugin ansible search collection-versions.'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Api V3 Plugin Ansible Search Collection-Versions API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-api-v3-plugin-ansible-search-collection-versions-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Artifacts Collections V3 API from Red Hat Ansible Automation Platform — 8 operation(s) for pulp_ansible: artifacts collections v3.'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Artifacts Collections V3 API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-artifacts-collections-v3-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Default Api API from Red Hat Ansible Automation Platform — 1 operation(s) for pulp_ansible: default api.'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Default API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-default-api-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Default Api V3 API from Red Hat Ansible Automation Platform — 1 operation(s) for pulp_ansible: default api v3.'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Default Api V3 API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-default-api-v3-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Default Api V3 Artifacts Collections API from Red Hat Ansible Automation Platform — 1 operation(s) for pulp_ansible: default api v3 artifacts collections.'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Default Api V3 Artifacts Collections API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-default-api-v3-artifacts-collections-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Default Api V3 Collection_Versions All API from Red Hat Ansible Automation Platform — 1 operation(s) for pulp_ansible: default api v3 collection_versions all.'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Default Api V3 Collection_Versions All API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-default-api-v3-collection-versions-all-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Default Api V3 Collections All API from Red Hat Ansible Automation Platform — 1 operation(s) for pulp_ansible: default api v3 collections all.'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Default Api V3 Collections All API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-default-api-v3-collections-all-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Default Api V3 Collections API from Red Hat Ansible Automation Platform — 2 operation(s) for pulp_ansible: default api v3 collections.'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Default Api V3 Collections API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-default-api-v3-collections-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Default Api V3 Collections Versions API from Red Hat Ansible Automation Platform — 2 operation(s) for pulp_ansible: default api v3 collections versions.'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Default Api V3 Collections Versions API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-default-api-v3-collections-versions-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Default Api V3 Collections Versions Docs-Blob API from Red Hat Ansible Automation Platform — 1 operation(s) for pulp_ansible: default api v3 collections versions docs-blob.'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Default Api V3 Collections Versions Docs-Blob API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-default-api-v3-collections-versions-docs-blob-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Default Api V3 Imports Collections API from Red Hat Ansible Automation Platform — 1 operation(s) for pulp_ansible: default api v3 imports collections.'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Default Api V3 Imports Collections API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-default-api-v3-imports-collections-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Default Api V3 Namespaces API from Red Hat Ansible Automation Platform — 2 operation(s) for pulp_ansible: default api v3 namespaces.'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Default Api V3 Namespaces API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-default-api-v3-namespaces-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Default Api V3 Plugin Ansible Client-Configuration API from Red Hat Ansible Automation Platform — 1 operation(s) for pulp_ansible: default api v3 plugin ansible client-configuration.'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Default Api V3 Plugin Ansible Client-Configuration API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-default-api-v3-plugin-ansible-client-configuration-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Default Api V3 Plugin Ansible Content Collections All-Collections API from Red Hat Ansible Automation Platform — 1 operation(s) for pulp_ansible: default api v3 plugin ansible conten'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Default Api V3 Plugin Ansible Content Collections All-Collections API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-default-api-v3-plugin-ansible-content-collections-all-collections-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Default Api V3 Plugin Ansible Content Collections All-Versions API from Red Hat Ansible Automation Platform — 1 operation(s) for pulp_ansible: default api v3 plugin ansible content c'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Default Api V3 Plugin Ansible Content Collections All-Versions API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-default-api-v3-plugin-ansible-content-collections-all-versions-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Default Api V3 Plugin Ansible Content Collections API from Red Hat Ansible Automation Platform — 1 operation(s) for pulp_ansible: default api v3 plugin ansible content collections.'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Default Api V3 Plugin Ansible Content Collections API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-default-api-v3-plugin-ansible-content-collections-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Default Api V3 Plugin Ansible Content Collections Artifacts API from Red Hat Ansible Automation Platform — 1 operation(s) for pulp_ansible: default api v3 plugin ansible content coll'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Default Api V3 Plugin Ansible Content Collections Artifacts API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-default-api-v3-plugin-ansible-content-collections-artifacts-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Default Api V3 Plugin Ansible Content Collections Index API from Red Hat Ansible Automation Platform — 2 operation(s) for pulp_ansible: default api v3 plugin ansible content collecti'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Default Api V3 Plugin Ansible Content Collections Index API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-default-api-v3-plugin-ansible-content-collections-index-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Default Api V3 Plugin Ansible Content Collections Index Versions API from Red Hat Ansible Automation Platform — 2 operation(s) for pulp_ansible: default api v3 plugin ansible content'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Default Api V3 Plugin Ansible Content Collections Index Versions API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-default-api-v3-plugin-ansible-content-collections-index-versions-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Default Api V3 Plugin Ansible Content Collections Index Versions Docs-Blob API from Red Hat Ansible Automation Platform — 1 operation(s) for pulp_ansible: default api v3 plugin ansib'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Default Api V3 Plugin Ansible Content Collections Index Versions Docs-Blob API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-default-api-v3-plugin-ansible-content-collections-index-versions-docs-blob-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Default Api V3 Plugin Ansible Content Namespaces API from Red Hat Ansible Automation Platform — 2 operation(s) for pulp_ansible: default api v3 plugin ansible content namespaces.'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Default Api V3 Plugin Ansible Content Namespaces API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-default-api-v3-plugin-ansible-content-namespaces-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Default Api V3 Plugin Ansible Imports Collections API from Red Hat Ansible Automation Platform — 1 operation(s) for pulp_ansible: default api v3 plugin ansible imports collections.'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Default Api V3 Plugin Ansible Imports Collections API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-default-api-v3-plugin-ansible-imports-collections-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Default Api V3 Plugin Ansible Search Collection-Versions API from Red Hat Ansible Automation Platform — 1 operation(s) for pulp_ansible: default api v3 plugin ansible search collecti'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Default Api V3 Plugin Ansible Search Collection-Versions API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-default-api-v3-plugin-ansible-search-collection-versions-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Namespaces API from Red Hat Ansible Automation Platform — 2 operation(s) for pulp_ansible: namespaces.'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Namespaces API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-namespaces-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Ansible: Tags API from Red Hat Ansible Automation Platform — 1 operation(s) for pulp_ansible: tags.'
  name: 'Red Hat Ansible Automation Platform Pulp_Ansible: Tags API'
  slug: red-hat-ansible-automation-platform-pulp-ansible-tags-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp: Api API from Red Hat Ansible Automation Platform — 1 operation(s) for pulp: api.'
  name: 'Red Hat Ansible Automation Platform Pulp: API'
  slug: red-hat-ansible-automation-platform-pulp-api-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp_Container: Namespaces API from Red Hat Ansible Automation Platform — 6 operation(s) for pulp_container: namespaces.'
  name: 'Red Hat Ansible Automation Platform Pulp_Container: Namespaces API'
  slug: red-hat-ansible-automation-platform-pulp-container-namespaces-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Pulp: V3 Ansible Copy API from Red Hat Ansible Automation Platform — 1 operation(s) for pulp: v3 ansible copy.'
  name: 'Red Hat Ansible Automation Platform Pulp: V3 Ansible Copy API'
  slug: red-hat-ansible-automation-platform-pulp-v3-ansible-copy-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The receptor_addresses API from Red Hat Ansible Automation Platform — 2 operation(s) for receptor_addresses.
  name: Red Hat Ansible Automation Platform Receptor Addresses API
  slug: red-hat-ansible-automation-platform-receptor-addresses-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The Remotes API from Red Hat Ansible Automation Platform — 1 operation(s) for remotes.
  name: Red Hat Ansible Automation Platform Remotes API
  slug: red-hat-ansible-automation-platform-remotes-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Remotes: Collection API from Red Hat Ansible Automation Platform — 8 operation(s) for remotes: collection.'
  name: 'Red Hat Ansible Automation Platform Remotes: Collection API'
  slug: red-hat-ansible-automation-platform-remotes-collection-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Remotes: Container API from Red Hat Ansible Automation Platform — 8 operation(s) for remotes: container.'
  name: 'Red Hat Ansible Automation Platform Remotes: Container API'
  slug: red-hat-ansible-automation-platform-remotes-container-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Remotes: File API from Red Hat Ansible Automation Platform — 8 operation(s) for remotes: file.'
  name: 'Red Hat Ansible Automation Platform Remotes: File API'
  slug: red-hat-ansible-automation-platform-remotes-file-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Remotes: Git API from Red Hat Ansible Automation Platform — 8 operation(s) for remotes: git.'
  name: 'Red Hat Ansible Automation Platform Remotes: Git API'
  slug: red-hat-ansible-automation-platform-remotes-git-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Remotes: Pull-Through API from Red Hat Ansible Automation Platform — 8 operation(s) for remotes: pull-through.'
  name: 'Red Hat Ansible Automation Platform Remotes: Pull-Through API'
  slug: red-hat-ansible-automation-platform-remotes-pull-through-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Remotes: Role API from Red Hat Ansible Automation Platform — 8 operation(s) for remotes: role.'
  name: 'Red Hat Ansible Automation Platform Remotes: Role API'
  slug: red-hat-ansible-automation-platform-remotes-role-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The Repair API from Red Hat Ansible Automation Platform — 1 operation(s) for repair.
  name: Red Hat Ansible Automation Platform Repair API
  slug: red-hat-ansible-automation-platform-repair-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Repositories: Ansible API from Red Hat Ansible Automation Platform — 16 operation(s) for repositories: ansible.'
  name: 'Red Hat Ansible Automation Platform Repositories: Ansible API'
  slug: red-hat-ansible-automation-platform-repositories-ansible-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Repositories: Ansible Versions API from Red Hat Ansible Automation Platform — 4 operation(s) for repositories: ansible versions.'
  name: 'Red Hat Ansible Automation Platform Repositories: Ansible Versions API'
  slug: red-hat-ansible-automation-platform-repositories-ansible-versions-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The Repositories API from Red Hat Ansible Automation Platform — 1 operation(s) for repositories.
  name: Red Hat Ansible Automation Platform Repositories API
  slug: red-hat-ansible-automation-platform-repositories-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Repositories: Container API from Red Hat Ansible Automation Platform — 17 operation(s) for repositories: container.'
  name: 'Red Hat Ansible Automation Platform Repositories: Container API'
  slug: red-hat-ansible-automation-platform-repositories-container-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Repositories: Container-Push API from Red Hat Ansible Automation Platform — 11 operation(s) for repositories: container-push.'
  name: 'Red Hat Ansible Automation Platform Repositories: Container-Push API'
  slug: red-hat-ansible-automation-platform-repositories-container-push-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Repositories: Container-Push Versions API from Red Hat Ansible Automation Platform — 3 operation(s) for repositories: container-push versions.'
  name: 'Red Hat Ansible Automation Platform Repositories: Container-Push Versions API'
  slug: red-hat-ansible-automation-platform-repositories-container-push-versions-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Repositories: Container Versions API from Red Hat Ansible Automation Platform — 3 operation(s) for repositories: container versions.'
  name: 'Red Hat Ansible Automation Platform Repositories: Container Versions API'
  slug: red-hat-ansible-automation-platform-repositories-container-versions-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Repositories: File API from Red Hat Ansible Automation Platform — 10 operation(s) for repositories: file.'
  name: 'Red Hat Ansible Automation Platform Repositories: File API'
  slug: red-hat-ansible-automation-platform-repositories-file-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Repositories: File Versions API from Red Hat Ansible Automation Platform — 3 operation(s) for repositories: file versions.'
  name: 'Red Hat Ansible Automation Platform Repositories: File Versions API'
  slug: red-hat-ansible-automation-platform-repositories-file-versions-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Repositories: Reclaim_Space API from Red Hat Ansible Automation Platform — 1 operation(s) for repositories: reclaim_space.'
  name: 'Red Hat Ansible Automation Platform Repositories: Reclaim_Space API'
  slug: red-hat-ansible-automation-platform-repositories-reclaim-space-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The Repository_Versions API from Red Hat Ansible Automation Platform — 1 operation(s) for repository_versions.
  name: Red Hat Ansible Automation Platform Repository Versions API
  slug: red-hat-ansible-automation-platform-repository-versions-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The role_definitions API from Red Hat Ansible Automation Platform — 12 operation(s) for role_definitions.
  name: Red Hat Ansible Automation Platform Role Definitions API
  slug: red-hat-ansible-automation-platform-role-definitions-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The role_metadata API from Red Hat Ansible Automation Platform — 2 operation(s) for role_metadata.
  name: Red Hat Ansible Automation Platform Role Metadata API
  slug: red-hat-ansible-automation-platform-role-metadata-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The role_team_access API from Red Hat Ansible Automation Platform — 6 operation(s) for role_team_access.
  name: Red Hat Ansible Automation Platform Role Team Access API
  slug: red-hat-ansible-automation-platform-role-team-access-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The role_team_assignments API from Red Hat Ansible Automation Platform — 6 operation(s) for role_team_assignments.
  name: Red Hat Ansible Automation Platform Role Team Assignments API
  slug: red-hat-ansible-automation-platform-role-team-assignments-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The role_user_access API from Red Hat Ansible Automation Platform — 6 operation(s) for role_user_access.
  name: Red Hat Ansible Automation Platform Role User Access API
  slug: red-hat-ansible-automation-platform-role-user-access-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The role_user_assignments API from Red Hat Ansible Automation Platform — 6 operation(s) for role_user_assignments.
  name: Red Hat Ansible Automation Platform Role User Assignments API
  slug: red-hat-ansible-automation-platform-role-user-assignments-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The roles API from Red Hat Ansible Automation Platform — 6 operation(s) for roles.
  name: Red Hat Ansible Automation Platform Roles API
  slug: red-hat-ansible-automation-platform-roles-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The routes API from Red Hat Ansible Automation Platform — 2 operation(s) for routes.
  name: Red Hat Ansible Automation Platform Routes API
  slug: red-hat-ansible-automation-platform-routes-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The rulebooks API from Red Hat Ansible Automation Platform — 4 operation(s) for rulebooks.
  name: Red Hat Ansible Automation Platform Rulebooks API
  slug: red-hat-ansible-automation-platform-rulebooks-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The schedules API from Red Hat Ansible Automation Platform — 8 operation(s) for schedules.
  name: Red Hat Ansible Automation Platform Schedules API
  slug: red-hat-ansible-automation-platform-schedules-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The service_clusters API from Red Hat Ansible Automation Platform — 10 operation(s) for service_clusters.
  name: Red Hat Ansible Automation Platform Service Clusters API
  slug: red-hat-ansible-automation-platform-service-clusters-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The service-index API from Red Hat Ansible Automation Platform — 49 operation(s) for service-index.
  name: Red Hat Ansible Automation Platform Service Index API
  slug: red-hat-ansible-automation-platform-service-index-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The service_keys API from Red Hat Ansible Automation Platform — 2 operation(s) for service_keys.
  name: Red Hat Ansible Automation Platform Service Keys API
  slug: red-hat-ansible-automation-platform-service-keys-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The service_nodes API from Red Hat Ansible Automation Platform — 2 operation(s) for service_nodes.
  name: Red Hat Ansible Automation Platform Service Nodes API
  slug: red-hat-ansible-automation-platform-service-nodes-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The service_types API from Red Hat Ansible Automation Platform — 3 operation(s) for service_types.
  name: Red Hat Ansible Automation Platform Service Types API
  slug: red-hat-ansible-automation-platform-service-types-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The services API from Red Hat Ansible Automation Platform — 2 operation(s) for services.
  name: Red Hat Ansible Automation Platform Services API
  slug: red-hat-ansible-automation-platform-services-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The session API from Red Hat Ansible Automation Platform — 1 operation(s) for session.
  name: Red Hat Ansible Automation Platform Session API
  slug: red-hat-ansible-automation-platform-session-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The settings API from Red Hat Ansible Automation Platform — 6 operation(s) for settings.
  name: Red Hat Ansible Automation Platform Settings API
  slug: red-hat-ansible-automation-platform-settings-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The Signing-Services API from Red Hat Ansible Automation Platform — 2 operation(s) for signing-services.
  name: Red Hat Ansible Automation Platform Signing Services API
  slug: red-hat-ansible-automation-platform-signing-services-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The Status API from Red Hat Ansible Automation Platform — 3 operation(s) for status.
  name: Red Hat Ansible Automation Platform Status API
  slug: red-hat-ansible-automation-platform-status-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The system_job_templates API from Red Hat Ansible Automation Platform — 8 operation(s) for system_job_templates.
  name: Red Hat Ansible Automation Platform System Job Templates API
  slug: red-hat-ansible-automation-platform-system-job-templates-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The system_jobs API from Red Hat Ansible Automation Platform — 5 operation(s) for system_jobs.
  name: Red Hat Ansible Automation Platform System Jobs API
  slug: red-hat-ansible-automation-platform-system-jobs-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The Task-Groups API from Red Hat Ansible Automation Platform — 2 operation(s) for task-groups.
  name: Red Hat Ansible Automation Platform Task Groups API
  slug: red-hat-ansible-automation-platform-task-groups-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The Task-Schedules API from Red Hat Ansible Automation Platform — 6 operation(s) for task-schedules.
  name: Red Hat Ansible Automation Platform Task Schedules API
  slug: red-hat-ansible-automation-platform-task-schedules-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The Tasks API from Red Hat Ansible Automation Platform — 11 operation(s) for tasks.
  name: Red Hat Ansible Automation Platform Tasks API
  slug: red-hat-ansible-automation-platform-tasks-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The teams API from Red Hat Ansible Automation Platform — 19 operation(s) for teams.
  name: Red Hat Ansible Automation Platform Teams API
  slug: red-hat-ansible-automation-platform-teams-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The telemetry API from Red Hat Ansible Automation Platform — 1 operation(s) for telemetry.
  name: Red Hat Ansible Automation Platform Telemetry API
  slug: red-hat-ansible-automation-platform-telemetry-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The Token API from Red Hat Ansible Automation Platform — 1 operation(s) for token.
  name: Red Hat Ansible Automation Platform Token API
  slug: red-hat-ansible-automation-platform-token-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The tokens API from Red Hat Ansible Automation Platform — 2 operation(s) for tokens.
  name: Red Hat Ansible Automation Platform Tokens API
  slug: red-hat-ansible-automation-platform-tokens-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The trigger_definition API from Red Hat Ansible Automation Platform — 1 operation(s) for trigger_definition.
  name: Red Hat Ansible Automation Platform Trigger Definition API
  slug: red-hat-ansible-automation-platform-trigger-definition-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The ui_auth API from Red Hat Ansible Automation Platform — 1 operation(s) for ui_auth.
  name: Red Hat Ansible Automation Platform UI Auth API
  slug: red-hat-ansible-automation-platform-ui-auth-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The ui_plugin_routes API from Red Hat Ansible Automation Platform — 2 operation(s) for ui_plugin_routes.
  name: Red Hat Ansible Automation Platform UI Plugin Routes API
  slug: red-hat-ansible-automation-platform-ui-plugin-routes-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The unified_job_templates API from Red Hat Ansible Automation Platform — 1 operation(s) for unified_job_templates.
  name: Red Hat Ansible Automation Platform Unified Job Templates API
  slug: red-hat-ansible-automation-platform-unified-job-templates-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The unified_jobs API from Red Hat Ansible Automation Platform — 1 operation(s) for unified_jobs.
  name: Red Hat Ansible Automation Platform Unified Jobs API
  slug: red-hat-ansible-automation-platform-unified-jobs-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The Uploads API from Red Hat Ansible Automation Platform — 7 operation(s) for uploads.
  name: Red Hat Ansible Automation Platform Uploads API
  slug: red-hat-ansible-automation-platform-uploads-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The Upstream-Pulps API from Red Hat Ansible Automation Platform — 7 operation(s) for upstream-pulps.
  name: Red Hat Ansible Automation Platform Upstream Pulps API
  slug: red-hat-ansible-automation-platform-upstream-pulps-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The users API from Red Hat Ansible Automation Platform — 25 operation(s) for users.
  name: Red Hat Ansible Automation Platform Users API
  slug: red-hat-ansible-automation-platform-users-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'The Users: Roles API from Red Hat Ansible Automation Platform — 2 operation(s) for users: roles.'
  name: 'Red Hat Ansible Automation Platform Users: Roles API'
  slug: red-hat-ansible-automation-platform-users-roles-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: watsonx Code Assistant
  name: Red Hat Ansible Automation Platform Wca API
  slug: red-hat-ansible-automation-platform-wca-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The Workers API from Red Hat Ansible Automation Platform — 2 operation(s) for workers.
  name: Red Hat Ansible Automation Platform Workers API
  slug: red-hat-ansible-automation-platform-workers-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The workflow_approval_templates API from Red Hat Ansible Automation Platform — 2 operation(s) for workflow_approval_templates.
  name: Red Hat Ansible Automation Platform Workflow Approval Templates API
  slug: red-hat-ansible-automation-platform-workflow-approval-templates-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The workflow_approvals API from Red Hat Ansible Automation Platform — 4 operation(s) for workflow_approvals.
  name: Red Hat Ansible Automation Platform Workflow Approvals API
  slug: red-hat-ansible-automation-platform-workflow-approvals-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The workflow_job_nodes API from Red Hat Ansible Automation Platform — 8 operation(s) for workflow_job_nodes.
  name: Red Hat Ansible Automation Platform Workflow Job Nodes API
  slug: red-hat-ansible-automation-platform-workflow-job-nodes-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The workflow_job_template_nodes API from Red Hat Ansible Automation Platform — 9 operation(s) for workflow_job_template_nodes.
  name: Red Hat Ansible Automation Platform Workflow Job Template Nodes API
  slug: red-hat-ansible-automation-platform-workflow-job-template-nodes-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The workflow_job_templates API from Red Hat Ansible Automation Platform — 20 operation(s) for workflow_job_templates.
  name: Red Hat Ansible Automation Platform Workflow Job Templates API
  slug: red-hat-ansible-automation-platform-workflow-job-templates-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: The workflow_jobs API from Red Hat Ansible Automation Platform — 8 operation(s) for workflow_jobs.
  name: Red Hat Ansible Automation Platform Workflow Jobs API
  slug: red-hat-ansible-automation-platform-workflow-jobs-api
- baseURL: https://catalog-host/api/v1/
  baseurl_source: declared
  description: The Cacertificates API from Red Hat Ansible Automation Platform — 2 operation(s) for cacertificates.
  name: Red Hat Ansible Automation Platform Cacertificates API
  slug: red-hat-ansible-automation-platform-cacertificates-api
artifact_total: 359
asyncapis:
- description: ''
  name: Red Hat Ansible Automation Platform Webhooks
  slug: red-hat-ansible-automation-platform-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-ansible-automation-platform/refs/heads/main/overlays/red-hat-ansible-automation-platform-automation-controller-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/red-hat-ansible-automation-platform-automation-controller-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-ansible-automation-platform/refs/heads/main/overlays/red-hat-ansible-automation-platform-automation-hub-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/red-hat-ansible-automation-platform-automation-hub-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-ansible-automation-platform/refs/heads/main/overlays/red-hat-ansible-automation-platform-event-driven-ansible-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/red-hat-ansible-automation-platform-event-driven-ansible-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-ansible-automation-platform/refs/heads/main/overlays/red-hat-ansible-automation-platform-platform-gateway-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/red-hat-ansible-automation-platform-platform-gateway-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-ansible-automation-platform/refs/heads/main/overlays/red-hat-ansible-automation-platform-ansible-lightspeed-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/red-hat-ansible-automation-platform-ansible-lightspeed-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.redhat.com/en/technologies/management/ansible
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-ansible-automation-platform/refs/heads/main/packages/red-hat-ansible-automation-platform-packages.yml
  title: ''
  type: SDKs
  url: packages/red-hat-ansible-automation-platform-packages.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-ansible-automation-platform/refs/heads/main/lifecycle/red-hat-ansible-automation-platform-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/red-hat-ansible-automation-platform-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-ansible-automation-platform/refs/heads/main/security/red-hat-ansible-automation-platform-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/red-hat-ansible-automation-platform-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Compliance
  url: https://access.redhat.com/compliance
- group: start
  title: ''
  type: Console
  url: https://www.redhat.com/en/interactive-labs/ansible
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-ansible-automation-platform/refs/heads/main/plans/red-hat-ansible-automation-platform-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/red-hat-ansible-automation-platform-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-ansible-automation-platform/refs/heads/main/rate-limits/red-hat-ansible-automation-platform-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/red-hat-ansible-automation-platform-rate-limits.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-ansible-automation-platform/refs/heads/main/sandbox/red-hat-ansible-automation-platform-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/red-hat-ansible-automation-platform-sandbox.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-ansible-automation-platform/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-ansible-automation-platform/refs/heads/main/asyncapi/red-hat-ansible-automation-platform-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/red-hat-ansible-automation-platform-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-ansible-automation-platform/refs/heads/main/data-model/red-hat-ansible-automation-platform-data-model.yml
  title: ''
  type: DataModel
  url: data-model/red-hat-ansible-automation-platform-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-ansible-automation-platform/refs/heads/main/cli/red-hat-ansible-automation-platform-cli.yml
  title: ''
  type: CLI
  url: cli/red-hat-ansible-automation-platform-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-ansible-automation-platform/refs/heads/main/changelog/red-hat-ansible-automation-platform-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/red-hat-ansible-automation-platform-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-ansible-automation-platform/refs/heads/main/conventions/red-hat-ansible-automation-platform-conventions.yml
  title: ''
  type: Conventions
  url: conventions/red-hat-ansible-automation-platform-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-ansible-automation-platform/refs/heads/main/security/red-hat-ansible-automation-platform-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/red-hat-ansible-automation-platform-trust-center.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-ansible-automation-platform/refs/heads/main/lifecycle/red-hat-ansible-automation-platform-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/red-hat-ansible-automation-platform-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-ansible-automation-platform/refs/heads/main/errors/red-hat-ansible-automation-platform-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/red-hat-ansible-automation-platform-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-ansible-automation-platform/refs/heads/main/conformance/red-hat-ansible-automation-platform-conformance.yml
  title: ''
  type: Conformance
  url: conformance/red-hat-ansible-automation-platform-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-ansible-automation-platform/refs/heads/main/llms/red-hat-ansible-automation-platform-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/red-hat-ansible-automation-platform-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-ansible-automation-platform/refs/heads/main/mcp/red-hat-ansible-automation-platform-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/red-hat-ansible-automation-platform-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-ansible-automation-platform/refs/heads/main/mcp/red-hat-ansible-automation-platform-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/red-hat-ansible-automation-platform-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-ansible-automation-platform/refs/heads/main/well-known/red-hat-ansible-automation-platform-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/red-hat-ansible-automation-platform-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-ansible-automation-platform/refs/heads/main/well-known/red-hat-ansible-automation-platform-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/red-hat-ansible-automation-platform-well-known.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-ansible-automation-platform/refs/heads/main/packages/red-hat-ansible-automation-platform-packages.yml
  title: ''
  type: Packages
  url: packages/red-hat-ansible-automation-platform-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-ansible-automation-platform/refs/heads/main/authentication/red-hat-ansible-automation-platform-authentication.yml
  title: ''
  type: Authentication
  url: authentication/red-hat-ansible-automation-platform-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-ansible-automation-platform/refs/heads/main/scopes/red-hat-ansible-automation-platform-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/red-hat-ansible-automation-platform-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-ansible-automation-platform/refs/heads/main/security/red-hat-ansible-automation-platform-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/red-hat-ansible-automation-platform-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-ansible-automation-platform/refs/heads/main/security/red-hat-ansible-automation-platform-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/red-hat-ansible-automation-platform-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ansible
- group: start
  title: ''
  type: Portal
  url: https://www.redhat.com/en/technologies/management/ansible
- group: docs
  title: ''
  type: Documentation
  url: https://access.redhat.com/documentation/en-us/red_hat_ansible_automation_platform/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.redhat.com/en/technologies/management/ansible/trial
- group: company
  title: ''
  type: Blog
  url: https://www.redhat.com/en/blog/channel/red-hat-ansible-automation
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ansible
- group: operate
  title: ''
  type: Support
  url: https://access.redhat.com/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.redhat.com/en/about/agreements
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.redhat.com/en/about/privacy-policy
- group: learn
  title: ''
  type: Training
  url: https://www.redhat.com/en/services/training/do007-ansible-essentials-simplicity-automation-technical-overview
- group: commercial
  title: ''
  type: Pricing
  url: https://www.redhat.com/en/technologies/management/ansible/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.redhat.com/
created: '2024-01-01'
description: Red Hat Ansible Automation Platform is an enterprise automation solution that provides a framework for building and operating IT automation at scale. It includes the Automation Controller, Automation Hub, Event-Driven Ansible, and Ansible Lightspeed with IBM watsonx Code Assistant, providing REST APIs for managing automation across hybrid cloud infrastructure.
features:
- description: Centralized management of automation with RBAC, audit logging, and credential management.
  name: Enterprise Automation Controller
- description: Curate and distribute certified and custom Ansible content collections within the enterprise.
  name: Private Automation Hub
- description: Automated response to infrastructure events using rulebook activations and event sources.
  name: Event-Driven Automation
- description: AI-powered automation content generation with IBM watsonx Code Assistant.
  name: Ansible Lightspeed
- description: Containerized automation runtime environments for consistent and portable execution.
  name: Execution Environments
- description: Distributed automation execution architecture for scaling across global infrastructure.
  name: Automation Mesh
finops:
- name: Red Hat Ansible Automation Platform Finops
  service_category: API
  slug: red-hat-ansible-automation-platform-finops
image: /assets/icons/red-hat-ansible-automation-platform.png
integrations:
- description: Container platform integration for deploying and managing Ansible on Kubernetes.
  name: Red Hat OpenShift
- description: Content management and patching integration for RHEL infrastructure automation.
  name: Red Hat Satellite
- description: ITSM integration for change management and incident remediation workflows.
  name: ServiceNow
- description: Cloud automation for AWS services with certified content collections.
  name: AWS
- description: Cloud automation for Azure services with certified content collections.
  name: Microsoft Azure
- description: Cloud automation for GCP services with certified content collections.
  name: Google Cloud
layout: provider
mcp_servers:
- description: 'Red Hat ships a first-party Model Context Protocol server for Ansible Automation Platform. It is a Node.js service (Apache-2.0, github.com/ansible/aap-mcp-server) that reads the AAP component OpenAPI '
  name: AAP MCP Service
  slug: aap-mcp-service
modified: '2026-08-29'
name: Red Hat Ansible Automation Platform
nav: Providers
network: true
overview: 'Red Hat Ansible Automation Platform publishes 331 APIs on the [APIs.io](https://apis.io/) network, including Access Policies API, Acs: File API, Activation Instances API, and 328 more. Tagged areas include Automation, Configuration Management, DevOps, Enterprise, and Red Hat.


  The Red Hat Ansible Automation Platform catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Red Hat Ansible Automation Platform''s developer surface includes developer console, sandbox, CLI, changelog, authentication, developer portal, documentation, and 39 more developer resources.'
plans:
- name: Red Hat Ansible Automation Platform Plans Pricing
  plan_count: 2
  slug: red-hat-ansible-automation-platform-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Red Hat Ansible Automation Platform Rate Limits
  slug: red-hat-ansible-automation-platform-rate-limits
scopes:
- name: Red Hat Ansible Automation Platform Scopes
  scope_count: 3
  slug: red-hat-ansible-automation-platform-scopes
  summary_line: 3 scopes · authorizationCode/password
score:
  band: strong
  composite: 63.0
  coverage:
    artifact_dirs: 24
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.2
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 54.4
    developer_ergonomics: 80.4
    discoverability: 75.9
    operational_transparency: 60.5
  previous_composite: 63.2
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.3
      total: 332
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://raw.githubusercontent.com/api-evangelist/red-hat-ansible-automation-platform/refs/heads/main/screenshots/red-hat-ansible-automation-platform-2026-06-20T192716.png
security:
- kind: authentication
  name: Red Hat Ansible Automation Platform Authentication
  slug: red-hat-ansible-automation-platform-authentication
  summary_line: apiKey/http/oauth2 · 6 schemes
- kind: domain-security
  name: Red Hat Ansible Automation Platform Domain Security
  slug: red-hat-ansible-automation-platform-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Red Hat Ansible Automation Platform Vulnerability Disclosure
  slug: red-hat-ansible-automation-platform-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Red Hat Ansible Automation Platform Trust Center
  slug: red-hat-ansible-automation-platform-trust-center
  summary_line: Common Criteria, FIPS 140, ISO/IEC 27001, ISO/IEC 27018, ISO 42001, ISO/SAE 21434, DISA STIG, HIPAA, HDS, CIS Benchmarks, BSI, CCN-STIC / ENS, EU Cyber Resilience Act, EU AI Act, Accessibility Conformance Reports (VPAT)
slug: red-hat-ansible-automation-platform
tags:
- Automation
- Configuration Management
- DevOps
- Enterprise
- Red Hat
- Ansible
- IT Operations
- Event-Driven Architecture
- Infrastructure as Code
- MCP
use_cases:
- description: Standardize and scale IT automation across the enterprise with governance and compliance controls.
  name: Enterprise IT Automation
- description: Automate infrastructure provisioning and management across on-premises and multi-cloud environments.
  name: Hybrid Cloud Management
- description: Automated security response and compliance enforcement with event-driven remediation.
  name: Security Automation
- description: Manage and automate edge infrastructure at scale with automation mesh and execution environments.
  name: Edge Computing
- description: Enable self-service automation ordering through the services catalog with approval workflows.
  name: Self-Service IT
website: https://www.redhat.com/en/technologies/management/ansible
---
