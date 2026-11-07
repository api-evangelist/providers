---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 172
  human_in_the_loop: 119
  name: Avetta Agentic Access
  operation_count: 488
  slug: avetta-agentic-access
  summary_line: 488 operations · 172 acting · 119 human-in-the-loop
api_count: 6
apis:
- description: 'Avetta''s Open API surface, documented through the Avetta Developer Portal, lets client organizations select contractor and supplier endpoints and customize data synchronization between the Avetta One '
  name: Avetta Developer API
  slug: avetta-developer-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The Account API from Avetta — 9 operation(s) for account.
  name: Avetta Account API
  slug: avetta-account-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The Accounts API allows you to retrieve account information.
  name: Avetta Accounts API
  slug: avetta-accounts-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The Admin API provides administrative endpoints for system overview and management data. Access requires appropriate security permissions.
  name: Avetta Admin API
  slug: avetta-admin-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The Auth API allows you to authenticate into Worker Management. Handles multi-factor authentication, password reset, and single sign-on.
  name: Avetta Auth API
  slug: avetta-auth-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: '## How to authenticate Every request to the Avetta APIs must include an `Authorization` header. You can fill it in using **one** of two methods. Pick the one that fits your integration; you do not nee'
  name: Avetta Authentication API
  slug: avetta-authentication-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The Compliance API from Avetta — 20 operation(s) for compliance.
  name: Avetta Compliance API
  slug: avetta-compliance-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The Countries API allows you to retrieve country information. Get country data, dialing codes, and more.
  name: Avetta Countries API
  slug: avetta-countries-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The endpoints to credit events.
  name: Avetta Credit API
  slug: avetta-credit-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: Endpoints that are deprecated and will be removed in future versions.
  name: Avetta Deprecated Endpoints API
  slug: avetta-deprecated-endpoints-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The Event API allows you to retrieve event / requirement information.
  name: Avetta Event API
  slug: avetta-event-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The Events API allows you to list events.
  name: Avetta Events API
  slug: avetta-events-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The Languages API allows you to retrieve language information.
  name: Avetta Languages API
  slug: avetta-languages-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusLogpoint_activity-controller API from Avetta — 1 operation(s) for pegasuslogpoint_activity-controller.
  name: Avetta Pegasus Logpoint Activity Controller API
  slug: avetta-pegasuslogpoint-activity-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusLogpoint_activity-type-controller API from Avetta — 1 operation(s) for pegasuslogpoint_activity-type-controller.
  name: Avetta Pegasus Logpoint Activity Type Controller API
  slug: avetta-pegasuslogpoint-activity-type-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusLogpoint_induction-controller API from Avetta — 2 operation(s) for pegasuslogpoint_induction-controller.
  name: Avetta Pegasus Logpoint Induction Controller API
  slug: avetta-pegasuslogpoint-induction-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusLogpoint_logpoint-access-controller API from Avetta — 1 operation(s) for pegasuslogpoint_logpoint-access-controller.
  name: Avetta Pegasus Logpoint Logpoint Access Controller API
  slug: avetta-pegasuslogpoint-logpoint-access-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusLogpoint_logpoint-connectivity-controller API from Avetta — 1 operation(s) for pegasuslogpoint_logpoint-connectivity-controller.
  name: Avetta Pegasus Logpoint Logpoint Connectivity Controller API
  slug: avetta-pegasuslogpoint-logpoint-connectivity-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusLogpoint_logpoint-connectivity-controller-v-2 API from Avetta — 1 operation(s) for pegasuslogpoint_logpoint-connectivity-controller-v-2.
  name: Avetta Pegasus Logpoint Logpoint Connectivity Controller V 2 API
  slug: avetta-pegasuslogpoint-logpoint-connectivity-controller-v-2-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusLogpoint_logpoint-controller API from Avetta — 10 operation(s) for pegasuslogpoint_logpoint-controller.
  name: Avetta Pegasus Logpoint Logpoint Controller API
  slug: avetta-pegasuslogpoint-logpoint-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusLogpoint_logpoint-hardware-controller API from Avetta — 1 operation(s) for pegasuslogpoint_logpoint-hardware-controller.
  name: Avetta Pegasus Logpoint Logpoint Hardware Controller API
  slug: avetta-pegasuslogpoint-logpoint-hardware-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusLogpoint_logpoint-licence-controller API from Avetta — 2 operation(s) for pegasuslogpoint_logpoint-licence-controller.
  name: Avetta Pegasus Logpoint Logpoint Licence Controller API
  slug: avetta-pegasuslogpoint-logpoint-licence-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusLogpoint_logpoint-message-controller API from Avetta — 3 operation(s) for pegasuslogpoint_logpoint-message-controller.
  name: Avetta Pegasus Logpoint Logpoint Message Controller API
  slug: avetta-pegasuslogpoint-logpoint-message-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusLogpoint_logpoint-person-controller API from Avetta — 16 operation(s) for pegasuslogpoint_logpoint-person-controller.
  name: Avetta Pegasus Logpoint Logpoint Person Controller API
  slug: avetta-pegasuslogpoint-logpoint-person-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusLogpoint_safety-selection-controller API from Avetta — 3 operation(s) for pegasuslogpoint_safety-selection-controller.
  name: Avetta Pegasus Logpoint Safety Selection Controller API
  slug: avetta-pegasuslogpoint-safety-selection-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_external-company-subscription-controller API from Avetta — 3 operation(s) for pegasusscope_external-company-subscription-controller.
  name: Avetta Pegasus Scope External Company Subscription Controller API
  slug: avetta-pegasusscope-external-company-subscription-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_login-controller API from Avetta — 1 operation(s) for pegasusscope_login-controller.
  name: Avetta Pegasus Scope Login Controller API
  slug: avetta-pegasusscope-login-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_rto-employee-controller API from Avetta — 2 operation(s) for pegasusscope_rto-employee-controller.
  name: Avetta Pegasus Scope Rto Employee Controller API
  slug: avetta-pegasusscope-rto-employee-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-access-key-controller API from Avetta — 1 operation(s) for pegasusscope_scope-access-key-controller.
  name: Avetta Pegasus Scope Scope Access Key Controller API
  slug: avetta-pegasusscope-scope-access-key-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-card-design-controller API from Avetta — 2 operation(s) for pegasusscope_scope-card-design-controller.
  name: Avetta Pegasus Scope Scope Card Design Controller API
  slug: avetta-pegasusscope-scope-card-design-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-cert-controller API from Avetta — 1 operation(s) for pegasusscope_scope-cert-controller.
  name: Avetta Pegasus Scope Scope Cert Controller API
  slug: avetta-pegasusscope-scope-cert-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-company-cert-controller API from Avetta — 2 operation(s) for pegasusscope_scope-company-cert-controller.
  name: Avetta Pegasus Scope Scope Company Cert Controller API
  slug: avetta-pegasusscope-scope-company-cert-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-company-controller API from Avetta — 13 operation(s) for pegasusscope_scope-company-controller.
  name: Avetta Pegasus Scope Scope Company Controller API
  slug: avetta-pegasusscope-scope-company-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-company-relationship-controller API from Avetta — 8 operation(s) for pegasusscope_scope-company-relationship-controller.
  name: Avetta Pegasus Scope Scope Company Relationship Controller API
  slug: avetta-pegasusscope-scope-company-relationship-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-company-site-controller API from Avetta — 1 operation(s) for pegasusscope_scope-company-site-controller.
  name: Avetta Pegasus Scope Scope Company Site Controller API
  slug: avetta-pegasusscope-scope-company-site-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-company-sms-review-controller API from Avetta — 1 operation(s) for pegasusscope_scope-company-sms-review-controller.
  name: Avetta Pegasus Scope Scope Company Sms Review Controller API
  slug: avetta-pegasusscope-scope-company-sms-review-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-company-subscription-controller API from Avetta — 2 operation(s) for pegasusscope_scope-company-subscription-controller.
  name: Avetta Pegasus Scope Scope Company Subscription Controller API
  slug: avetta-pegasusscope-scope-company-subscription-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-competency-assignment-controller API from Avetta — 2 operation(s) for pegasusscope_scope-competency-assignment-controller.
  name: Avetta Pegasus Scope Scope Competency Assignment Controller API
  slug: avetta-pegasusscope-scope-competency-assignment-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-competency-controller API from Avetta — 7 operation(s) for pegasusscope_scope-competency-controller.
  name: Avetta Pegasus Scope Scope Competency Controller API
  slug: avetta-pegasusscope-scope-competency-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-controller API from Avetta — 5 operation(s) for pegasusscope_scope-controller.
  name: Avetta Pegasus Scope Scope Controller API
  slug: avetta-pegasusscope-scope-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-crew-controller API from Avetta — 10 operation(s) for pegasusscope_scope-crew-controller.
  name: Avetta Pegasus Scope Scope Crew Controller API
  slug: avetta-pegasusscope-scope-crew-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-employee-competency-controller API from Avetta — 2 operation(s) for pegasusscope_scope-employee-competency-controller.
  name: Avetta Pegasus Scope Scope Employee Competency Controller API
  slug: avetta-pegasusscope-scope-employee-competency-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-employee-controller API from Avetta — 6 operation(s) for pegasusscope_scope-employee-controller.
  name: Avetta Pegasus Scope Scope Employee Controller API
  slug: avetta-pegasusscope-scope-employee-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-enrolment-controller API from Avetta — 1 operation(s) for pegasusscope_scope-enrolment-controller.
  name: Avetta Pegasus Scope Scope Enrolment Controller API
  slug: avetta-pegasusscope-scope-enrolment-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-evacuation-controller API from Avetta — 3 operation(s) for pegasusscope_scope-evacuation-controller.
  name: Avetta Pegasus Scope Scope Evacuation Controller API
  slug: avetta-pegasusscope-scope-evacuation-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-hierarchy-controller API from Avetta — 2 operation(s) for pegasusscope_scope-hierarchy-controller.
  name: Avetta Pegasus Scope Scope Hierarchy Controller API
  slug: avetta-pegasusscope-scope-hierarchy-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-logpoint-controller API from Avetta — 1 operation(s) for pegasusscope_scope-logpoint-controller.
  name: Avetta Pegasus Scope Scope Logpoint Controller API
  slug: avetta-pegasusscope-scope-logpoint-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-onsite-log-controller API from Avetta — 5 operation(s) for pegasusscope_scope-onsite-log-controller.
  name: Avetta Pegasus Scope Scope Onsite Log Controller API
  slug: avetta-pegasusscope-scope-onsite-log-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-person-access-controller API from Avetta — 1 operation(s) for pegasusscope_scope-person-access-controller.
  name: Avetta Pegasus Scope Scope Person Access Controller API
  slug: avetta-pegasusscope-scope-person-access-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-person-access-key-controller API from Avetta — 4 operation(s) for pegasusscope_scope-person-access-key-controller.
  name: Avetta Pegasus Scope Scope Person Access Key Controller API
  slug: avetta-pegasusscope-scope-person-access-key-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-person-assignable-role-controller API from Avetta — 1 operation(s) for pegasusscope_scope-person-assignable-role-controller.
  name: Avetta Pegasus Scope Scope Person Assignable Role Controller API
  slug: avetta-pegasusscope-scope-person-assignable-role-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-person-block-controller API from Avetta — 3 operation(s) for pegasusscope_scope-person-block-controller.
  name: Avetta Pegasus Scope Scope Person Block Controller API
  slug: avetta-pegasusscope-scope-person-block-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-person-by-other-id-site-controller API from Avetta — 1 operation(s) for pegasusscope_scope-person-by-other-id-site-controller.
  name: Avetta Pegasus Scope Scope Person By Other ID Site Controller API
  slug: avetta-pegasusscope-scope-person-by-other-id-site-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-person-card-print-controller API from Avetta — 1 operation(s) for pegasusscope_scope-person-card-print-controller.
  name: Avetta Pegasus Scope Scope Person Card Print Controller API
  slug: avetta-pegasusscope-scope-person-card-print-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-person-company-client-controller API from Avetta — 1 operation(s) for pegasusscope_scope-person-company-client-controller.
  name: Avetta Pegasus Scope Scope Person Company Client Controller API
  slug: avetta-pegasusscope-scope-person-company-client-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-person-company-controller API from Avetta — 2 operation(s) for pegasusscope_scope-person-company-controller.
  name: Avetta Pegasus Scope Scope Person Company Controller API
  slug: avetta-pegasusscope-scope-person-company-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-person-company-realm-controller API from Avetta — 1 operation(s) for pegasusscope_scope-person-company-realm-controller.
  name: Avetta Pegasus Scope Scope Person Company Realm Controller API
  slug: avetta-pegasusscope-scope-person-company-realm-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-person-company-site-client-controller API from Avetta — 1 operation(s) for pegasusscope_scope-person-company-site-client-controller.
  name: Avetta Pegasus Scope Scope Person Company Site Client Controller API
  slug: avetta-pegasusscope-scope-person-company-site-client-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-person-company-site-controller API from Avetta — 4 operation(s) for pegasusscope_scope-person-company-site-controller.
  name: Avetta Pegasus Scope Scope Person Company Site Controller API
  slug: avetta-pegasusscope-scope-person-company-site-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-person-competency-client-controller API from Avetta — 1 operation(s) for pegasusscope_scope-person-competency-client-controller.
  name: Avetta Pegasus Scope Scope Person Competency Client Controller API
  slug: avetta-pegasusscope-scope-person-competency-client-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-person-competency-controller API from Avetta — 24 operation(s) for pegasusscope_scope-person-competency-controller.
  name: Avetta Pegasus Scope Scope Person Competency Controller API
  slug: avetta-pegasusscope-scope-person-competency-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-person-competency-permission-controller API from Avetta — 4 operation(s) for pegasusscope_scope-person-competency-permission-controller.
  name: Avetta Pegasus Scope Scope Person Competency Permission Controller API
  slug: avetta-pegasusscope-scope-person-competency-permission-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-person-controller API from Avetta — 20 operation(s) for pegasusscope_scope-person-controller.
  name: Avetta Pegasus Scope Scope Person Controller API
  slug: avetta-pegasusscope-scope-person-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-person-crew-controller API from Avetta — 4 operation(s) for pegasusscope_scope-person-crew-controller.
  name: Avetta Pegasus Scope Scope Person Crew Controller API
  slug: avetta-pegasusscope-scope-person-crew-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-person-external-id-controller API from Avetta — 3 operation(s) for pegasusscope_scope-person-external-id-controller.
  name: Avetta Pegasus Scope Scope Person External ID Controller API
  slug: avetta-pegasusscope-scope-person-external-id-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-person-file-controller API from Avetta — 1 operation(s) for pegasusscope_scope-person-file-controller.
  name: Avetta Pegasus Scope Scope Person File Controller API
  slug: avetta-pegasusscope-scope-person-file-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-person-message-controller API from Avetta — 1 operation(s) for pegasusscope_scope-person-message-controller.
  name: Avetta Pegasus Scope Scope Person Message Controller API
  slug: avetta-pegasusscope-scope-person-message-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-person-onsite-log-controller API from Avetta — 5 operation(s) for pegasusscope_scope-person-onsite-log-controller.
  name: Avetta Pegasus Scope Scope Person Onsite Log Controller API
  slug: avetta-pegasusscope-scope-person-onsite-log-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-person-photo-bulk-controller API from Avetta — 1 operation(s) for pegasusscope_scope-person-photo-bulk-controller.
  name: Avetta Pegasus Scope Scope Person Photo Bulk Controller API
  slug: avetta-pegasusscope-scope-person-photo-bulk-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-person-photo-controller API from Avetta — 4 operation(s) for pegasusscope_scope-person-photo-controller.
  name: Avetta Pegasus Scope Scope Person Photo Controller API
  slug: avetta-pegasusscope-scope-person-photo-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-person-role-controller API from Avetta — 3 operation(s) for pegasusscope_scope-person-role-controller.
  name: Avetta Pegasus Scope Scope Person Role Controller API
  slug: avetta-pegasusscope-scope-person-role-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-person-site-controller API from Avetta — 4 operation(s) for pegasusscope_scope-person-site-controller.
  name: Avetta Pegasus Scope Scope Person Site Controller API
  slug: avetta-pegasusscope-scope-person-site-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-person-subscription-controller API from Avetta — 1 operation(s) for pegasusscope_scope-person-subscription-controller.
  name: Avetta Pegasus Scope Scope Person Subscription Controller API
  slug: avetta-pegasusscope-scope-person-subscription-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-role-controller API from Avetta — 8 operation(s) for pegasusscope_scope-role-controller.
  name: Avetta Pegasus Scope Scope Role Controller API
  slug: avetta-pegasusscope-scope-role-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-subscription-definition-controller API from Avetta — 1 operation(s) for pegasusscope_scope-subscription-definition-controller.
  name: Avetta Pegasus Scope Scope Subscription Definition Controller API
  slug: avetta-pegasusscope-scope-subscription-definition-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_scope-user-controller API from Avetta — 2 operation(s) for pegasusscope_scope-user-controller.
  name: Avetta Pegasus Scope Scope User Controller API
  slug: avetta-pegasusscope-scope-user-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_user-controller API from Avetta — 1 operation(s) for pegasusscope_user-controller.
  name: Avetta Pegasus Scope User Controller API
  slug: avetta-pegasusscope-user-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope_user-scope-controller API from Avetta — 7 operation(s) for pegasusscope_user-scope-controller.
  name: Avetta Pegasus Scope User Scope Controller API
  slug: avetta-pegasusscope-user-scope-controller-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope2_scope-competency-controller-v-2 API from Avetta — 1 operation(s) for pegasusscope2_scope-competency-controller-v-2.
  name: Avetta Pegasus Scope2 Scope Competency Controller V 2 API
  slug: avetta-pegasusscope2-scope-competency-controller-v-2-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope2_scope-controller-v-2 API from Avetta — 1 operation(s) for pegasusscope2_scope-controller-v-2.
  name: Avetta Pegasus Scope2 Scope Controller V 2 API
  slug: avetta-pegasusscope2-scope-controller-v-2-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope2_scope-employee-controller-v-2 API from Avetta — 1 operation(s) for pegasusscope2_scope-employee-controller-v-2.
  name: Avetta Pegasus Scope2 Scope Employee Controller V 2 API
  slug: avetta-pegasusscope2-scope-employee-controller-v-2-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope2_scope-person-competency-controller-v-2 API from Avetta — 1 operation(s) for pegasusscope2_scope-person-competency-controller-v-2.
  name: Avetta Pegasus Scope2 Scope Person Competency Controller V 2 API
  slug: avetta-pegasusscope2-scope-person-competency-controller-v-2-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope2_scope-person-controller-v-2 API from Avetta — 5 operation(s) for pegasusscope2_scope-person-controller-v-2.
  name: Avetta Pegasus Scope2 Scope Person Controller V 2 API
  slug: avetta-pegasusscope2-scope-person-controller-v-2-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope2_scope-person-role-controller-v-2 API from Avetta — 1 operation(s) for pegasusscope2_scope-person-role-controller-v-2.
  name: Avetta Pegasus Scope2 Scope Person Role Controller V 2 API
  slug: avetta-pegasusscope2-scope-person-role-controller-v-2-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope2_scope-person-verified-document-controller-v-2 API from Avetta — 1 operation(s) for pegasusscope2_scope-person-verified-document-controller-v-2.
  name: Avetta Pegasus Scope2 Scope Person Verified Document Controller V 2 API
  slug: avetta-pegasusscope2-scope-person-verified-document-controller-v-2-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The pegasusScope2_scope-role-controller-v-2 API from Avetta — 3 operation(s) for pegasusscope2_scope-role-controller-v-2.
  name: Avetta Pegasus Scope2 Scope Role Controller V 2 API
  slug: avetta-pegasusscope2-scope-role-controller-v-2-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The Registration API allows you to register a new account or user.
  name: Avetta Registration API
  slug: avetta-registration-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The Reviews API allows admins to perform document reviews for the workers
  name: Avetta Reviews API
  slug: avetta-reviews-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The Roles API allows you to retrieve role information.
  name: Avetta Roles API
  slug: avetta-roles-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The Sites API allows you to retrieve site information and assign users to sites.
  name: Avetta Sites API
  slug: avetta-sites-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The Status API allows you to retrieve status information.
  name: Avetta Status API
  slug: avetta-status-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The User API allows you to retrieve user detail information.
  name: Avetta User API
  slug: avetta-user-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The Users API allows you to retrieve all users information.
  name: Avetta Users API
  slug: avetta-users-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The Variances API allows you to retrieve variance information or create a variance.
  name: Avetta Variances API
  slug: avetta-variances-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: Worksite safety management operations including work requests and project management
  name: Avetta Worksite Safety API
  slug: avetta-worksite-safety-api
- baseURL: https://api.avetta.com
  baseurl_source: declared
  description: The TimeCard API allows you to retrieve a list of workers on site.
  name: Avetta Time Card API
  slug: avetta-time-card-api
artifact_total: 124
common:
- group: other
  href: https://artifacts.apis.io/avetta/capabilities/avetta-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/avetta-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/avetta/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/avetta/overlays/avetta-connect-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avetta-connect-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/avetta/agentic-access/avetta-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/avetta-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/avetta/rate-limits/avetta-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/avetta-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/avetta/plans/avetta-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/avetta-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/avetta/rules/avetta-rules.yml
  title: ''
  type: Spectral
  url: rules/avetta-rules.yml
- group: design
  href: https://artifacts.apis.io/avetta/json-ld/avetta-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/avetta-context.jsonld
- group: design
  href: https://artifacts.apis.io/avetta/vocabulary/avetta-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/avetta-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/avetta/data-model/avetta-data-model.yml
  title: ''
  type: DataModel
  url: data-model/avetta-data-model.yml
- group: operate
  href: https://artifacts.apis.io/avetta/changelog/avetta-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/avetta-changelog.yml
- group: design
  href: https://artifacts.apis.io/avetta/conventions/avetta-conventions.yml
  title: ''
  type: Conventions
  url: conventions/avetta-conventions.yml
- group: start
  href: https://artifacts.apis.io/avetta/sandbox/avetta-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/avetta-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.avetta.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.connect.avetta.com/
- group: design
  href: https://artifacts.apis.io/avetta/lifecycle/avetta-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/avetta-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/avetta/errors/avetta-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/avetta-problem-types.yml
- group: design
  href: https://artifacts.apis.io/avetta/conformance/avetta-conformance.yml
  title: ''
  type: Conformance
  url: conformance/avetta-conformance.yml
- group: other
  href: https://artifacts.apis.io/avetta/hosts/avetta-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avetta-hosts.yml
- group: other
  href: https://artifacts.apis.io/avetta/vendors/avetta-vendors.yml
  title: ''
  type: Vendors
  url: vendors/avetta-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.avetta.com/leadership
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/avetta
- group: auth
  href: https://artifacts.apis.io/avetta/scopes/avetta-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/avetta-scopes.yml
- group: auth
  href: https://artifacts.apis.io/avetta/authentication/avetta-authentication.yml
  title: ''
  type: Authentication
  url: authentication/avetta-authentication.yml
- group: auth
  href: https://artifacts.apis.io/avetta/security/avetta-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/avetta-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/avetta/security/avetta-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avetta-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://avetta.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.api.avetta.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api.avetta.com
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.avetta.com
- group: company
  title: ''
  type: Blog
  url: https://www.avetta.com/blog
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.avetta.com
- group: start
  title: ''
  type: Login
  url: https://app.avetta.com/login
- group: operate
  title: ''
  type: Support
  url: https://help.avetta.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.avetta.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.avetta.com/legal/master-subscription-agreement
- group: commercial
  title: ''
  type: Pricing
  url: https://www.avetta.com/plans
- group: operate
  title: ''
  type: StatusPage
  url: https://status.avetta.com/
- group: agent
  href: https://artifacts.apis.io/avetta/well-known/avetta-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/avetta-well-known.yml
- group: company
  title: ''
  type: Website
  url: https://www.avetta.com
created: '2026-07-17'
description: Avetta operates a cloud-based supply chain risk management (SCRM) and contractor compliance platform, Avetta One, used by more than 360,000 businesses across 120+ countries to prequalify, audit, and continuously monitor contractors and suppliers. The platform spans health and safety compliance, prequalification, worker management, sustainability and ESG (GHG reporting, supplier diversity, supplier ESG due diligence), and business risk (financial, cybersecurity, and insurance verification). Avetta exposes an Open API and ERP connectors through a developer portal (docs.api.avetta.com) so client organizations can synchronize contractor and supplier data into Salesforce, Oracle, Workday, ServiceNow, and internal systems. Avetta is a portfolio company of Norwest Venture Partners.
image: https://cdn.prod.website-files.com/696fddc24f2e82c416e23640/697ba15528499b3ced513224_hero-opg.png
json_schemas:
- name: 1.0.0_CreateWorkRequestRequest
  property_count: 4
  slug: avetta-1-0-0-create-work-request-request
- name: 1.0.0_GetWorkRequestQuestionsResponse
  property_count: 5
  slug: avetta-1-0-0-get-work-request-questions-response
- name: 1.0.0_GetWorkflowResponse
  property_count: 7
  slug: avetta-1-0-0-get-workflow-response
- name: 1.0.0_SupplierProfile
  property_count: 19
  slug: avetta-1-0-0-supplier-profile
- name: 1.0.0_SupplierProfiles
  property_count: 2
  slug: avetta-1-0-0-supplier-profiles
- name: 1.0.0_WorkerOpenWorkRequestsSummary
  property_count: 4
  slug: avetta-1-0-0-worker-open-work-requests-summary
- name: 3.29.14_ClientCompanyRegistrationResource
  property_count: 30
  slug: avetta-3-29-14-client-company-registration-resource
- name: 3.29.14_CompetencyResource
  property_count: 31
  slug: avetta-3-29-14-competency-resource
- name: 3.29.14_EmployeeResource
  property_count: 39
  slug: avetta-3-29-14-employee-resource
- name: 3.29.14_IntegrateEmployeeResource
  property_count: 38
  slug: avetta-3-29-14-integrate-employee-resource
- name: 3.29.14_ScopePermissionResource
  property_count: 2
  slug: avetta-3-29-14-scope-permission-resource
- name: 3.29.14_WorkerResource
  property_count: 38
  slug: avetta-3-29-14-worker-resource
- name: requestStructurePassword
  property_count: 4
  slug: avetta-request-structure-password
- name: requestStructureRefresh
  property_count: 5
  slug: avetta-request-structure-refresh
- name: requestWMConnect
  property_count: 2
  slug: avetta-request-wmconnect
- name: sitesMessageResponse
  property_count: 2
  slug: avetta-sites-message-response
- name: statsSchema
  property_count: 10
  slug: avetta-stats-schema
jsonld:
- class_count: 120
  name: Avetta Context
  property_count: 364
  slug: avetta-context
layout: provider
modified: '2026-10-20'
name: Avetta
nav: Providers
network: true
overview: 'Avetta publishes 96 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Accounts API, Admin API, and 93 more. Tagged areas include Company, Supply Chain, Risk Management, Compliance, and Contractor Management.


  The Avetta catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Avetta''s developer surface includes changelog, sandbox, authentication, documentation, engineering blog, support, pricing, and 33 more developer resources.'
plans:
- name: Avetta Plans Pricing
  plan_count: 5
  slug: avetta-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 2
  name: Avetta Rate Limits
  slug: avetta-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Avetta API Rules
  rule_count: 13
  severity_counts:
    error: 6
    hint: 0
    info: 2
    warn: 5
  slug: avetta-rules
scopes:
- name: Avetta Scopes
  scope_count: 1
  slug: avetta-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 65.2
  coverage:
    artifact_dirs: 31
    catalog_earned: 85.8
    catalog_earned_first_party: 20.0
    catalog_gap: 29.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 63.4
    developer_ergonomics: 44.6
    discoverability: 79.5
    operational_transparency: 51.3
  previous_composite: 66.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 95
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 50.0
screenshot: https://apis.io/screenshots/avetta/avetta-2026-07-25T201923.png
security:
- kind: authentication
  name: Avetta Authentication
  slug: avetta-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Avetta Domain Security
  slug: avetta-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Avetta Trust Center
  slug: avetta-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018
skill_count: 2
skills:
- name: avetta-register-supplier
  slug: avetta-register-supplier
- name: avetta-supplier-compliance-review
  slug: avetta-supplier-compliance-review
slug: avetta
tags:
- Company
- Supply Chain
- Risk Management
- Compliance
- Contractor Management
- Safety
- ESG
- Supplier Management
website: https://avetta.com
---
