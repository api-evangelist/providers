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
  trial: false
  try_now: false
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 232
  human_in_the_loop: 0
  name: Erply Agentic Access
  operation_count: 351
  slug: erply-agentic-access
  summary_line: 351 operations · 232 acting
api_count: 4
apis:
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Assortment API from Erply — 3 operation(s) for assortment.
  name: Erply Assortment API
  slug: erply-assortment-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Assortment To Product Linking API from Erply — 9 operation(s) for assortment to product linking.
  name: Erply Assortment To Product Linking API
  slug: erply-assortment-to-product-linking-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: 'Attributes are attached to entities. The possible entities are: product, recipe, warehouse location, assortment, brand, matrix dimension, matrix dimension value, category, country, family, group, pack'
  name: Erply Attributes API
  slug: erply-attributes-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The auth API from Erply — 1 operation(s) for auth.
  name: Erply Auth API
  slug: erply-auth-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Brand API from Erply — 5 operation(s) for brand.
  name: Erply Brand API
  slug: erply-brand-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The clsf API from Erply — 7 operation(s) for clsf.
  name: Erply Clsf API
  slug: erply-clsf-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The clsf-device-properties API from Erply — 6 operation(s) for clsf-device-properties.
  name: Erply Clsf Device Properties API
  slug: erply-clsf-device-properties-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The clsf-events API from Erply — 2 operation(s) for clsf-events.
  name: Erply Clsf Events API
  slug: erply-clsf-events-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The clsf-labels API from Erply — 4 operation(s) for clsf-labels.
  name: Erply Clsf Labels API
  slug: erply-clsf-labels-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Country API from Erply — 3 operation(s) for country.
  name: Erply Country API
  slug: erply-country-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The device API from Erply — 4 operation(s) for device.
  name: Erply Device API
  slug: erply-device-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The event API from Erply — 1 operation(s) for event.
  name: Erply Event API
  slug: erply-event-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Export API from Erply — 3 operation(s) for export.
  name: Erply Export API
  slug: erply-export-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The External IDs API from Erply — 4 operation(s) for external ids.
  name: Erply External IDs API
  slug: erply-external-ids-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The form API from Erply — 1 operation(s) for form.
  name: Erply Form API
  slug: erply-form-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Franchise Products API from Erply — 2 operation(s) for franchise products.
  name: Erply Franchise Products API
  slug: erply-franchise-products-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The item API from Erply — 4 operation(s) for item.
  name: Erply Item API
  slug: erply-item-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The label API from Erply — 1 operation(s) for label.
  name: Erply Label API
  slug: erply-label-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: Manage substitute and cross-sell products
  name: Erply Linked Products API
  slug: erply-linked-products-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Locations in warehouse API from Erply — 1 operation(s) for locations in warehouse.
  name: Erply Locations in warehouse API
  slug: erply-locations-in-warehouse-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Matrix Dimension API from Erply — 6 operation(s) for matrix dimension.
  name: Erply Matrix Dimension API
  slug: erply-matrix-dimension-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Matrix Dimension Value API from Erply — 6 operation(s) for matrix dimension value.
  name: Erply Matrix Dimension Value API
  slug: erply-matrix-dimension-value-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Matrix Product API from Erply — 7 operation(s) for matrix product.
  name: Erply Matrix Product API
  slug: erply-matrix-product-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Matrix Product Variation API from Erply — 4 operation(s) for matrix product variation.
  name: Erply Matrix Product Variation API
  slug: erply-matrix-product-variation-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The note API from Erply — 2 operation(s) for note.
  name: Erply Note API
  slug: erply-note-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Parameter Set to Group Linking API from Erply — 2 operation(s) for parameter set to group linking.
  name: Erply Parameter Set to Group Linking API
  slug: erply-parameter-set-to-group-linking-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Parameter Set To Product Linking API from Erply — 1 operation(s) for parameter set to product linking.
  name: Erply Parameter Set To Product Linking API
  slug: erply-parameter-set-to-product-linking-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Permissions API from Erply — 2 operation(s) for permissions.
  name: Erply Permissions API
  slug: erply-permissions-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The printout API from Erply — 3 operation(s) for printout.
  name: Erply Printout API
  slug: erply-printout-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Product Category API from Erply — 8 operation(s) for product category.
  name: Erply Product Category API
  slug: erply-product-category-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Product Extra Field 1 API from Erply — 6 operation(s) for product extra field 1.
  name: Erply Product Extra Field 1 API
  slug: erply-product-extra-field-1-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Product Extra Field 2 API from Erply — 6 operation(s) for product extra field 2.
  name: Erply Product Extra Field 2 API
  slug: erply-product-extra-field-2-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Product Extra Field 3 API from Erply — 6 operation(s) for product extra field 3.
  name: Erply Product Extra Field 3 API
  slug: erply-product-extra-field-3-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Product Extra Field 4 API from Erply — 6 operation(s) for product extra field 4.
  name: Erply Product Extra Field 4 API
  slug: erply-product-extra-field-4-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Product Family API from Erply — 4 operation(s) for product family.
  name: Erply Product Family API
  slug: erply-product-family-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Product Fields API from Erply — 2 operation(s) for product fields.
  name: Erply Product Fields API
  slug: erply-product-fields-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Product Group API from Erply — 15 operation(s) for product group.
  name: Erply Product Group API
  slug: erply-product-group-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Product Package API from Erply — 4 operation(s) for product package.
  name: Erply Product Package API
  slug: erply-product-package-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Product Parameter API from Erply — 5 operation(s) for product parameter.
  name: Erply Product Parameter API
  slug: erply-product-parameter-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Product Parameter Option API from Erply — 5 operation(s) for product parameter option.
  name: Erply Product Parameter Option API
  slug: erply-product-parameter-option-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Product Parameter Set API from Erply — 3 operation(s) for product parameter set.
  name: Erply Product Parameter Set API
  slug: erply-product-parameter-set-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Product Parameter Validation Rule API from Erply — 4 operation(s) for product parameter validation rule.
  name: Erply Product Parameter Validation Rule API
  slug: erply-product-parameter-validation-rule-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Product Parameter Value API from Erply — 4 operation(s) for product parameter value.
  name: Erply Product Parameter Value API
  slug: erply-product-parameter-value-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Product Priority Groups API from Erply — 6 operation(s) for product priority groups.
  name: Erply Product Priority Groups API
  slug: erply-product-priority-groups-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Product Recipes API from Erply — 4 operation(s) for product recipes.
  name: Erply Product Recipes API
  slug: erply-product-recipes-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Product Replacement API from Erply — 2 operation(s) for product replacement.
  name: Erply Product Replacement API
  slug: erply-product-replacement-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Product Units API from Erply — 6 operation(s) for product units.
  name: Erply Product Units API
  slug: erply-product-units-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: 'NB: Product picture management is done with CDN API: https://learn-api.erply.com/new-apis/cdn-api'
  name: Erply Products API
  slug: erply-products-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The report API from Erply — 4 operation(s) for report.
  name: Erply Report API
  slug: erply-report-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The resource API from Erply — 3 operation(s) for resource.
  name: Erply Resource API
  slug: erply-resource-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The row API from Erply — 4 operation(s) for row.
  name: Erply Row API
  slug: erply-row-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Special Endpoints API from Erply — 3 operation(s) for special endpoints.
  name: Erply Special Endpoints API
  slug: erply-special-endpoints-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Supplier API from Erply — 6 operation(s) for supplier.
  name: Erply Supplier API
  slug: erply-supplier-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The sync API from Erply — 3 operation(s) for sync.
  name: Erply Sync API
  slug: erply-sync-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The task API from Erply — 4 operation(s) for task.
  name: Erply Task API
  slug: erply-task-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Tasks API from Erply — 2 operation(s) for tasks.
  name: Erply Tasks API
  slug: erply-tasks-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The template API from Erply — 3 operation(s) for template.
  name: Erply Template API
  slug: erply-template-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Warehouse Locations API from Erply — 3 operation(s) for warehouse locations.
  name: Erply Warehouse Locations API
  slug: erply-warehouse-locations-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The webhook API from Erply — 2 operation(s) for webhook.
  name: Erply Webhook API
  slug: erply-webhook-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The webhook-configuration API from Erply — 2 operation(s) for webhook-configuration.
  name: Erply Webhook Configuration API
  slug: erply-webhook-configuration-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The workorder API from Erply — 14 operation(s) for workorder.
  name: Erply Workorder API
  slug: erply-workorder-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Configuration API from Erply — 6 operation(s) for configuration.
  name: Erply Configuration API
  slug: erply-configuration-api
- baseURL: https://api-pim-eu.erply.com
  baseurl_source: declared
  description: The Import And Export API from Erply — 2 operation(s) for import and export.
  name: Erply Import And Export API
  slug: erply-import-and-export-api
artifact_total: 137
asyncapis:
- description: ''
  name: Erply Webhooks
  slug: erply-webhooks
collections:
- collection_type: open
  name: assignments Assortment API
  slug: open-erply-assortment-api
- collection_type: open
  name: assignments Assortment Assortment To Product Linking API
  slug: open-erply-assortment-to-product-linking-api
- collection_type: open
  name: assignments Assortment Attributes API
  slug: open-erply-attributes-api
- collection_type: open
  name: assignments Assortment auth API
  slug: open-erply-auth-api
- collection_type: open
  name: assignments Assortment Brand API
  slug: open-erply-brand-api
- collection_type: open
  name: assignments Assortment clsf API
  slug: open-erply-clsf-api
- collection_type: open
  name: assignments Assortment clsf-device-properties API
  slug: open-erply-clsf-device-properties-api
- collection_type: open
  name: assignments Assortment clsf-events API
  slug: open-erply-clsf-events-api
- collection_type: open
  name: assignments Assortment clsf-labels API
  slug: open-erply-clsf-labels-api
- collection_type: open
  name: assignments Assortment Country API
  slug: open-erply-country-api
- collection_type: open
  name: assignments Assortment device API
  slug: open-erply-device-api
- collection_type: open
  name: assignments Assortment event API
  slug: open-erply-event-api
- collection_type: open
  name: assignments Assortment Export API
  slug: open-erply-export-api
- collection_type: open
  name: assignments Assortment External IDs API
  slug: open-erply-external-ids-api
- collection_type: open
  name: assignments Assortment form API
  slug: open-erply-form-api
- collection_type: open
  name: assignments Assortment Franchise Products API
  slug: open-erply-franchise-products-api
- collection_type: open
  name: assignments Assortment Import & Export API
  slug: open-erply-import-export-api
- collection_type: open
  name: assignments Assortment item API
  slug: open-erply-item-api
- collection_type: open
  name: assignments Assortment label API
  slug: open-erply-label-api
- collection_type: open
  name: assignments Assortment Linked Products API
  slug: open-erply-linked-products-api
- collection_type: open
  name: assignments Assortment Locations in warehouse API
  slug: open-erply-locations-in-warehouse-api
- collection_type: open
  name: assignments Assortment Matrix Dimension API
  slug: open-erply-matrix-dimension-api
- collection_type: open
  name: assignments Assortment Matrix Dimension Value API
  slug: open-erply-matrix-dimension-value-api
- collection_type: open
  name: assignments Assortment Matrix Product API
  slug: open-erply-matrix-product-api
- collection_type: open
  name: assignments Assortment Matrix Product Variation API
  slug: open-erply-matrix-product-variation-api
- collection_type: open
  name: assignments Assortment note API
  slug: open-erply-note-api
- collection_type: open
  name: assignments Assortment Parameter Set to Group Linking API
  slug: open-erply-parameter-set-to-group-linking-api
- collection_type: open
  name: assignments Assortment Parameter Set To Product Linking API
  slug: open-erply-parameter-set-to-product-linking-api
- collection_type: open
  name: assignments Assortment Permissions API
  slug: open-erply-permissions-api
- collection_type: open
  name: assignments Assortment printout API
  slug: open-erply-printout-api
- collection_type: open
  name: assignments Assortment Product Category API
  slug: open-erply-product-category-api
- collection_type: open
  name: assignments Assortment Product Extra Field 1 API
  slug: open-erply-product-extra-field-1-api
- collection_type: open
  name: assignments Assortment Product Extra Field 2 API
  slug: open-erply-product-extra-field-2-api
- collection_type: open
  name: assignments Assortment Product Extra Field 3 API
  slug: open-erply-product-extra-field-3-api
- collection_type: open
  name: assignments Assortment Product Extra Field 4 API
  slug: open-erply-product-extra-field-4-api
- collection_type: open
  name: assignments Assortment Product Family API
  slug: open-erply-product-family-api
- collection_type: open
  name: assignments Assortment Product Fields API
  slug: open-erply-product-fields-api
- collection_type: open
  name: assignments Assortment Product Group API
  slug: open-erply-product-group-api
- collection_type: open
  name: assignments Assortment Product Package API
  slug: open-erply-product-package-api
- collection_type: open
  name: assignments Assortment Product Parameter API
  slug: open-erply-product-parameter-api
- collection_type: open
  name: assignments Assortment Product Parameter Option API
  slug: open-erply-product-parameter-option-api
- collection_type: open
  name: assignments Assortment Product Parameter Set API
  slug: open-erply-product-parameter-set-api
- collection_type: open
  name: assignments Assortment Product Parameter Validation Rule API
  slug: open-erply-product-parameter-validation-rule-api
- collection_type: open
  name: assignments Assortment Product Parameter Value API
  slug: open-erply-product-parameter-value-api
- collection_type: open
  name: assignments Assortment Product Priority Groups API
  slug: open-erply-product-priority-groups-api
- collection_type: open
  name: assignments Assortment Product Recipes API
  slug: open-erply-product-recipes-api
- collection_type: open
  name: assignments Assortment Product Replacement API
  slug: open-erply-product-replacement-api
- collection_type: open
  name: assignments Assortment Product Units API
  slug: open-erply-product-units-api
- collection_type: open
  name: assignments Assortment Products API
  slug: open-erply-products-api
- collection_type: open
  name: assignments Assortment report API
  slug: open-erply-report-api
- collection_type: open
  name: assignments Assortment resource API
  slug: open-erply-resource-api
- collection_type: open
  name: assignments Assortment row API
  slug: open-erply-row-api
- collection_type: open
  name: assignments Assortment Special Endpoints API
  slug: open-erply-special-endpoints-api
- collection_type: open
  name: assignments Assortment Supplier API
  slug: open-erply-supplier-api
- collection_type: open
  name: assignments Assortment sync API
  slug: open-erply-sync-api
- collection_type: open
  name: assignments Assortment task API
  slug: open-erply-task-api
- collection_type: open
  name: assignments Assortment Tasks API
  slug: open-erply-tasks-api
- collection_type: open
  name: assignments Assortment template API
  slug: open-erply-template-api
- collection_type: open
  name: assignments Assortment v1 API
  slug: open-erply-v1-api
- collection_type: open
  name: assignments Assortment v3 API
  slug: open-erply-v3-api
- collection_type: open
  name: assignments Assortment Warehouse Locations API
  slug: open-erply-warehouse-locations-api
- collection_type: open
  name: assignments Assortment webhook API
  slug: open-erply-webhook-api
- collection_type: open
  name: assignments Assortment webhook-configuration API
  slug: open-erply-webhook-configuration-api
- collection_type: open
  name: assignments Assortment workorder API
  slug: open-erply-workorder-api
common:
- group: commercial
  href: https://artifacts.apis.io/erply/plans/erply-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/erply-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/erply/capabilities/erply-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/erply-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/erply/overlays/erply-assignments-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/erply-assignments-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://erply.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://learn-api.erply.com/
- group: docs
  title: ''
  type: Documentation
  url: https://learn-api.erply.com/
- group: docs
  title: ''
  type: APIReference
  url: https://learn-api.erply.com/requests
- group: start
  title: ''
  type: GettingStarted
  url: https://learn-api.erply.com/getting-started
- group: operate
  title: ''
  type: Support
  url: mailto:support@erply.com
- group: company
  title: ''
  type: Blog
  url: https://erply.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://erply.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://erply.com/sign-up/
- group: start
  title: ''
  type: Login
  url: https://go.erply.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://erply.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://erply.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/erply
- group: operate
  title: ''
  type: StatusPage
  url: https://status.erply.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://erply.com/release-notes
- group: operate
  href: https://artifacts.apis.io/erply/changelog/erply-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/erply-changelog.yml
- group: auth
  href: https://artifacts.apis.io/erply/authentication/erply-authentication.yml
  title: ''
  type: Authentication
  url: authentication/erply-authentication.yml
- group: auth
  href: https://artifacts.apis.io/erply/security/erply-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/erply-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/erply/agentic-access/erply-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/erply-agentic-access.yml
- group: build
  href: https://artifacts.apis.io/erply/packages/erply-packages.yml
  title: ''
  type: Packages
  url: packages/erply-packages.yml
- group: build
  href: https://artifacts.apis.io/erply/packages/erply-packages.yml
  title: ''
  type: SDKs
  url: packages/erply-packages.yml
- group: agent
  href: https://artifacts.apis.io/erply/llms/erply-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/erply-llms.txt
- group: agent
  href: https://artifacts.apis.io/erply/mcp/erply-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/erply-mcp.yml
- group: design
  href: https://artifacts.apis.io/erply/conventions/erply-conventions.yml
  title: ''
  type: Conventions
  url: conventions/erply-conventions.yml
- group: design
  href: https://artifacts.apis.io/erply/errors/erply-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/erply-error-codes.yml
- group: operate
  href: https://artifacts.apis.io/erply/rate-limits/erply-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/erply-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/erply/lifecycle/erply-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/erply-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/erply/conformance/erply-conformance.yml
  title: ''
  type: Conformance
  url: conformance/erply-conformance.yml
- group: design
  href: https://artifacts.apis.io/erply/data-model/erply-data-model.yml
  title: ''
  type: DataModel
  url: data-model/erply-data-model.yml
- group: design
  href: https://artifacts.apis.io/erply/asyncapi/erply-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/erply-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/erply/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Erply is a cloud-based retail management platform providing point-of-sale (POS), inventory and warehouse management, product information management (PIM), CRM, sales reporting and ecommerce integrations for retailers running one or more stores, warehouses and online sales channels. Erply exposes a general-purpose classic API plus a growing set of purpose-built JSON REST APIs (PIM, Account/Assignments, CAFA app configuration, Reports, CDN, WMS) documented with Swagger, and a Webhook Manager for real-time POS and sales-order events. Authentication is session-key based (verifyUser -> sessionKey with a per-account clientCode). Surfaced as a portfolio company of 500 Global and Seedcamp and enriched into the API Evangelist network with its real developer surface.
finops:
- has_sources: true
  method: derived
  name: Erply Finops
  primary_unit: store
  service_category: ''
  slug: erply-finops
  template: false
image: https://cdn.erply.com/images/533252/erplyIcon-1.webp
layout: provider
modified: '2026-07-19'
name: Erply
nav: Providers
network: true
overview: 'Erply publishes 63 API contracts indexed on the [APIs.io](https://apis.io/) network, including Assortment API, Assortment To Product Linking API, Attributes API, and 60 more. Tagged areas include Retail, Point-of-Sale, Inventory, Product Information Management, and CRM.


  The Erply catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Erply''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 27 more developer resources.'
plans:
- name: Erply Plans Pricing
  plan_count: 6
  slug: erply-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Erply Rate Limits
  slug: erply-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: Erply API Rules
  rule_count: 54
  severity_counts:
    error: 38
    hint: 0
    info: 1
    warn: 15
  slug: erply-rules
score:
  band: strong
  composite: 62.7
  coverage:
    artifact_dirs: 30
    catalog_earned: 67.5
    catalog_earned_first_party: 20.0
    catalog_gap: 47.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 77.6
    contract_governance: 18.2
    contract_quality: 52.9
    developer_ergonomics: 66.1
    discoverability: 78.6
    operational_transparency: 55.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 62.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 63
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/erply/erply-2026-07-25T213611.png
security:
- kind: authentication
  name: Erply Authentication
  slug: erply-authentication
  summary_line: apiKey · 6 schemes
- kind: domain-security
  name: Erply Domain Security
  slug: erply-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Manage Erply webhooks
  slug: erply-manage-webhooks
- name: Sync products from Erply PIM
  slug: erply-sync-products
slug: erply
tags:
- Retail
- Point-of-Sale
- Inventory
- Product Information Management
- CRM
- E-Commerce
- Warehouse Management
- Webhook
- Company
website: https://erply.com
---
