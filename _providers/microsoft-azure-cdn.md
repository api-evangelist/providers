---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: full
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 78
  human_in_the_loop: 2
  name: Microsoft Azure Cdn Agentic Access
  operation_count: 122
  slug: microsoft-azure-cdn-agentic-access
  summary_line: 122 operations · 78 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Operations operations
  name: microsoft-azure-cdn Operations API
  phrasing_intents:
  - id: Operations_List
    intent: List operations of the CDN resource provider
    question: Which management operations does the Microsoft.Cdn resource provider support?
  phrasing_ops: 1
  slug: microsoft-azure-cdn-operations-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Profiles operations
  name: microsoft-azure-cdn Profiles API
  phrasing_intents:
  - id: Profiles_List
    intent: List all CDN and Front Door profiles in a subscription
    question: Which CDN and Front Door profiles exist across my whole Azure subscription?
  - id: Profiles_ListByResourceGroup
    intent: List CDN and Front Door profiles in a resource group
    question: Which profiles live in one particular resource group?
  - id: Profiles_Get
    intent: Get a CDN or Front Door profile
    question: What SKU and provisioning state does one of my profiles have?
  - id: Profiles_Create
    intent: Create a CDN or Front Door profile
    question: How do I create a new Azure Front Door Premium or CDN profile?
  - id: Profiles_Update
    intent: Update tags or identity on a profile
    question: Can I change tags or the managed identity on an existing profile?
  - id: Profiles_Delete
    intent: Delete a profile and all its sub-resources
    question: Does deleting a profile also delete its endpoints, origins and custom domains?
  - id: Profiles_CdnCanMigrateToAfd
    intent: Check if a CDN profile can move to Front Door
    question: Is my existing CDN profile eligible to become a Front Door Standard or Premium profile?
  - id: Profiles_CdnMigrateToAfd
    intent: Prepare a CDN profile's migration to Front Door
    question: How do I migrate a CDN profile to Azure Front Door Standard or Premium?
  phrasing_ops: 28
  slug: microsoft-azure-cdn-profiles-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The AFDDomains API from Microsoft Azure Cdn — 3 operation(s) for afddomains.
  name: Microsoft Azure Cdn AFD Domains API
  phrasing_intents:
  - id: AFDCustomDomains_ListByProfile
    intent: List Front Door custom domains in a profile
    question: Which custom domains are attached to my Azure Front Door profile?
  - id: AFDCustomDomains_Get
    intent: Get a Front Door custom domain
    question: What is the validation state and TLS setup of one of my Front Door custom domains?
  - id: AFDCustomDomains_Create
    intent: Add a custom domain to a Front Door profile
    question: How do I add my own hostname to an Azure Front Door profile?
  - id: AFDCustomDomains_Update
    intent: Update an existing Front Door custom domain
    question: Can I change the TLS or DNS zone settings on a Front Door domain I already added?
  - id: AFDCustomDomains_Delete
    intent: Remove a custom domain from a Front Door profile
    question: What happens when I delete a custom domain from Front Door?
  - id: AFDCustomDomains_RefreshValidationToken
    intent: Refresh a custom domain's validation token
    question: My Front Door domain validation token expired, can I get a new one?
  phrasing_ops: 6
  slug: microsoft-azure-cdn-afddomains-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The AFDEndpoints API from Microsoft Azure Cdn — 5 operation(s) for afdendpoints.
  name: Microsoft Azure Cdn AFD Endpoints API
  phrasing_intents:
  - id: AFDEndpoints_ListByProfile
    intent: List Front Door endpoints in a profile
    question: Which endpoints exist on my Azure Front Door profile?
  - id: AFDEndpoints_Get
    intent: Get a Front Door endpoint
    question: What hostname and enabled state does one of my Front Door endpoints have?
  - id: AFDEndpoints_Create
    intent: Create a Front Door endpoint
    question: How do I add a new endpoint to my Azure Front Door profile?
  - id: AFDEndpoints_Update
    intent: Update tags or state of a Front Door endpoint
    question: Can I change the tags or enabled state of an existing Front Door endpoint?
  - id: AFDEndpoints_Delete
    intent: Delete a Front Door endpoint
    question: What happens to traffic when I delete an AFD endpoint?
  - id: AFDEndpoints_PurgeContent
    intent: Purge cached content from a Front Door endpoint
    question: How do I clear cached files from Azure Front Door after a deploy?
  - id: AFDEndpoints_ListResourceUsage
    intent: Check quota usage of a Front Door endpoint
    question: How close is my Front Door endpoint to its resource quota?
  - id: AFDEndpoints_ValidateCustomDomain
    intent: Validate a domain's DNS mapping to a Front Door endpoint
    question: Is my custom hostname's CNAME pointing at the right Front Door endpoint?
  phrasing_ops: 8
  slug: microsoft-azure-cdn-afdendpoints-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The AFDOriginGroups API from Microsoft Azure Cdn — 3 operation(s) for afdorigingroups.
  name: Microsoft Azure Cdn AFD Origin Groups API
  phrasing_intents:
  - id: AFDOriginGroups_ListByProfile
    intent: List origin groups in a Front Door profile
    question: Which origin groups are defined on my Azure Front Door profile?
  - id: AFDOriginGroups_Get
    intent: Get a Front Door origin group
    question: What health probe and load balancing settings does my origin group use?
  - id: AFDOriginGroups_Create
    intent: Create a Front Door origin group
    question: How do I set up a new backend pool with health probes on Front Door?
  - id: AFDOriginGroups_Update
    intent: Update an existing Front Door origin group
    question: Can I change the health probe interval on an origin group I already have?
  - id: AFDOriginGroups_Delete
    intent: Delete a Front Door origin group
    question: Can I remove an origin group that no route uses anymore?
  - id: AFDOriginGroups_ListResourceUsage
    intent: Check quota usage of a Front Door origin group
    question: How many origins can one origin group hold before I hit the quota?
  phrasing_ops: 6
  slug: microsoft-azure-cdn-afdorigingroups-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The AFDOrigins API from Microsoft Azure Cdn — 2 operation(s) for afdorigins.
  name: Microsoft Azure Cdn AFD Origins API
  phrasing_intents:
  - id: AFDOrigins_ListByOriginGroup
    intent: List origins in a Front Door origin group
    question: Which backend servers are in one of my Front Door origin groups?
  - id: AFDOrigins_Get
    intent: Get a Front Door origin
    question: What hostname, priority and weight does one of my Front Door origins have?
  - id: AFDOrigins_Create
    intent: Add an origin to a Front Door origin group
    question: How do I add a new backend server to my Azure Front Door origin group?
  - id: AFDOrigins_Update
    intent: Update an existing Front Door origin
    question: Can I change the weight or disable an origin that is already in a group?
  - id: AFDOrigins_Delete
    intent: Remove an origin from a Front Door origin group
    question: Can I take a retired backend out of my Front Door origin group?
  phrasing_ops: 5
  slug: microsoft-azure-cdn-afdorigins-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The CdnWebApplicationFirewallPolicies API from Microsoft Azure Cdn — 2 operation(s) for cdnwebapplicationfirewallpolicies.
  name: Microsoft Azure Cdn Cdn Web Application Firewall Policies API
  phrasing_intents:
  - id: Policies_List
    intent: List CDN WAF policies in a resource group
    question: Which web application firewall policies exist for my Azure CDN resources?
  - id: Policies_Get
    intent: Get a CDN WAF policy
    question: What custom and managed rules does one of my CDN WAF policies contain?
  - id: Policies_CreateOrUpdate
    intent: Create or replace a CDN WAF policy
    question: How do I create a web application firewall policy for Azure CDN?
  - id: Policies_Update
    intent: Update tags on a CDN WAF policy
    question: Can I change just the tags on an existing CDN firewall policy?
  - id: Policies_Delete
    intent: Delete a CDN WAF policy
    question: Can I delete a web application firewall policy I no longer use?
  phrasing_ops: 5
  slug: microsoft-azure-cdn-cdnwebapplicationfirewallpolicies-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Endpoints API from Microsoft Azure Cdn — 8 operation(s) for endpoints.
  name: Microsoft Azure Cdn Endpoints API
  phrasing_intents:
  - id: Endpoints_ListByProfile
    intent: List CDN endpoints in a profile
    question: Which classic CDN endpoints exist under my Azure CDN profile?
  - id: Endpoints_Get
    intent: Get a CDN endpoint
    question: Is my CDN endpoint currently running or stopped?
  - id: Endpoints_Create
    intent: Create a CDN endpoint
    question: How do I create a new endpoint in an Azure CDN profile?
  - id: Endpoints_Update
    intent: Update an existing CDN endpoint
    question: Can I change tags or caching behavior on an endpoint I already created?
  - id: Endpoints_Delete
    intent: Delete a CDN endpoint
    question: What happens to cached content when I delete a CDN endpoint?
  - id: Endpoints_ListResourceUsage
    intent: Check geo filter and domain quota on an endpoint
    question: How many geo filters and custom domains can I still add to this endpoint?
  - id: Endpoints_LoadContent
    intent: Pre-load content onto the CDN
    question: Can I warm the CDN cache with files before users request them?
  - id: Endpoints_PurgeContent
    intent: Purge cached content from a CDN endpoint
    question: How do I force the CDN to drop stale files after I update my site?
  phrasing_ops: 11
  slug: microsoft-azure-cdn-endpoints-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The OriginGroups API from Microsoft Azure Cdn — 2 operation(s) for origingroups.
  name: Microsoft Azure Cdn Origin Groups API
  phrasing_intents:
  - id: OriginGroups_ListByEndpoint
    intent: List origin groups on a CDN endpoint
    question: Which origin groups are configured on my classic CDN endpoint?
  - id: OriginGroups_Get
    intent: Get an origin group on a CDN endpoint
    question: What health probe settings does an origin group on my endpoint use?
  - id: OriginGroups_Create
    intent: Create an origin group on a CDN endpoint
    question: How do I group several origins for failover on a CDN endpoint?
  - id: OriginGroups_Update
    intent: Update an origin group on a CDN endpoint
    question: Can I change which origins belong to an existing endpoint origin group?
  - id: OriginGroups_Delete
    intent: Delete an origin group from a CDN endpoint
    question: Can I remove an origin group my endpoint no longer uses?
  phrasing_ops: 5
  slug: microsoft-azure-cdn-origingroups-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Origins API from Microsoft Azure Cdn — 2 operation(s) for origins.
  name: Microsoft Azure Cdn Origins API
  phrasing_intents:
  - id: Origins_ListByEndpoint
    intent: List origins on a CDN endpoint
    question: Which origin servers does my classic CDN endpoint pull content from?
  - id: Origins_Get
    intent: Get an origin on a CDN endpoint
    question: What hostname and ports does one of my CDN endpoint origins use?
  - id: Origins_Create
    intent: Add an origin to a CDN endpoint
    question: How do I add another origin server to an existing CDN endpoint?
  - id: Origins_Update
    intent: Update an origin on a CDN endpoint
    question: Can I change the hostname or priority of an origin that already exists?
  - id: Origins_Delete
    intent: Remove an origin from a CDN endpoint
    question: Can I take a decommissioned server out of my CDN endpoint's origins?
  phrasing_ops: 5
  slug: microsoft-azure-cdn-origins-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Providers API from Microsoft Azure Cdn — 2 operation(s) for providers.
  name: Microsoft Azure Cdn Providers API
  phrasing_intents:
  - id: CheckNameAvailability
    intent: Check if a CDN resource name is globally free
    question: Is the CDN endpoint name I want already taken globally?
  - id: EdgeNodes_List
    intent: List CDN edge node POP locations
    question: Where are the Azure CDN points of presence located?
  phrasing_ops: 2
  slug: microsoft-azure-cdn-providers-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Routes API from Microsoft Azure Cdn — 2 operation(s) for routes.
  name: Microsoft Azure Cdn Routes API
  phrasing_intents:
  - id: Routes_ListByEndpoint
    intent: List routes on a Front Door endpoint
    question: Which routes are configured on my Azure Front Door endpoint?
  - id: Routes_Get
    intent: Get a Front Door route
    question: What patterns, protocols and origin group does one of my Front Door routes use?
  - id: Routes_Create
    intent: Create a route on a Front Door endpoint
    question: How do I send traffic for a path pattern to an origin group on Front Door?
  - id: Routes_Update
    intent: Update an existing Front Door route
    question: Can I change the origin group or HTTPS redirect on a route I already have?
  - id: Routes_Delete
    intent: Delete a Front Door route
    question: What happens to requests matching a route after I delete it?
  phrasing_ops: 5
  slug: microsoft-azure-cdn-routes-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Rules API from Microsoft Azure Cdn — 2 operation(s) for rules.
  name: Microsoft Azure Cdn Rules API
  phrasing_intents:
  - id: Rules_ListByRuleSet
    intent: List delivery rules in a rule set
    question: Which delivery rules are inside one of my Front Door rule sets?
  - id: Rules_Get
    intent: Get a delivery rule
    question: What conditions and actions does one of my delivery rules apply?
  - id: Rules_Create
    intent: Add a delivery rule to a rule set
    question: How do I add a header rewrite or redirect rule on Azure Front Door?
  - id: Rules_Update
    intent: Update an existing delivery rule
    question: Can I change the conditions or actions of a rule I already created?
  - id: Rules_Delete
    intent: Delete a delivery rule
    question: Can I remove one rule without deleting its whole rule set?
  phrasing_ops: 5
  slug: microsoft-azure-cdn-rules-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The RuleSets API from Microsoft Azure Cdn — 3 operation(s) for rulesets.
  name: Microsoft Azure Cdn Rule Sets API
  phrasing_intents:
  - id: RuleSets_ListByProfile
    intent: List rule sets in a Front Door profile
    question: Which rule sets exist on my Azure Front Door profile?
  - id: RuleSets_Get
    intent: Get a Front Door rule set
    question: What is the provisioning state of one of my rule sets?
  - id: RuleSets_Create
    intent: Create a Front Door rule set
    question: How do I create a container for delivery rules on Front Door?
  - id: RuleSets_Delete
    intent: Delete a Front Door rule set
    question: Can I delete a rule set that routes no longer reference?
  - id: RuleSets_ListResourceUsage
    intent: Check quota usage of a rule set
    question: How many more rules can I add before a rule set hits its quota?
  phrasing_ops: 5
  slug: microsoft-azure-cdn-rulesets-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Secrets API from Microsoft Azure Cdn — 2 operation(s) for secrets.
  name: Microsoft Azure Cdn Secrets API
  phrasing_intents:
  - id: Secrets_ListByProfile
    intent: List secrets in a Front Door profile
    question: Which certificates and secrets are registered on my Azure Front Door profile?
  - id: Secrets_Get
    intent: Get a Front Door secret
    question: What Key Vault certificate and version does one of my secrets point to?
  - id: Secrets_Create
    intent: Add a secret to a Front Door profile
    question: How do I register my own TLS certificate from Key Vault with Front Door?
  - id: Secrets_Delete
    intent: Delete a Front Door secret
    question: Can I remove a certificate secret I no longer use?
  phrasing_ops: 4
  slug: microsoft-azure-cdn-secrets-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Subscriptions API from Microsoft Azure Cdn — 7 operation(s) for subscriptions.
  name: Microsoft Azure Cdn Subscriptions API
  phrasing_intents:
  - id: ManagedRuleSets_List
    intent: List available CDN WAF managed rule sets
    question: Which managed rule sets can I enable in a CDN web application firewall policy?
  - id: CheckNameAvailabilityWithSubscription
    intent: Check a CDN name's availability in my subscription
    question: Is a CDN endpoint name free to use within my Azure subscription?
  - id: ResourceUsage_List
    intent: Check CDN profile quota for my subscription
    question: How many CDN profiles am I allowed in my subscription and how many do I use?
  - id: ValidateProbe
    intent: Validate a dynamic site acceleration probe path
    question: Is my probe file reachable on the origin for dynamic site acceleration?
  - id: Profiles_CanMigrate
    intent: Check if a classic CDN profile can migrate
    question: Can my classic CDN profile be moved to Front Door Standard or Premium?
  - id: CheckEndpointNameAvailability
    intent: Check an AFD endpoint name in a resource group
    question: Is an Azure Front Door endpoint name available in my resource group?
  - id: Profiles_Migrate
    intent: Migrate a classic resource to a new Front Door profile
    question: How do I start migrating a classic Front Door or CDN resource into a new profile?
  phrasing_ops: 7
  slug: microsoft-azure-cdn-subscriptions-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Custom Domains API from Microsoft Azure Cdn — 4 operation(s) for custom domains.
  name: Microsoft Azure Cdn Custom Domains API
  phrasing_intents:
  - id: CustomDomains_ListByEndpoint
    intent: List custom domains on a CDN endpoint
    question: Which custom hostnames are mapped to my classic Azure CDN endpoint?
  - id: CustomDomains_Get
    intent: Get a custom domain on a CDN endpoint
    question: What is the HTTPS provisioning state of a custom domain on my CDN endpoint?
  - id: CustomDomains_Create
    intent: Map a custom domain to a CDN endpoint
    question: How do I attach my own hostname to an Azure CDN endpoint?
  - id: CustomDomains_Delete
    intent: Remove a custom domain from a CDN endpoint
    question: Can I detach a hostname from my CDN endpoint?
  - id: CustomDomains_DisableCustomHttps
    intent: Turn off HTTPS on a CDN custom domain
    question: How do I stop serving HTTPS on one of my CDN custom domains?
  - id: CustomDomains_EnableCustomHttps
    intent: Turn on HTTPS for a CDN custom domain
    question: Can I use a CDN-managed certificate or my own Key Vault certificate for a custom domain?
  phrasing_ops: 6
  slug: microsoft-azure-cdn-custom-domains-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Security Policies API from Microsoft Azure Cdn — 2 operation(s) for security policies.
  name: Microsoft Azure Cdn Security Policies API
  phrasing_intents:
  - id: SecurityPolicies_ListByProfile
    intent: List security policies in a Front Door profile
    question: Which security policies are associated with my Azure Front Door profile?
  - id: SecurityPolicies_Get
    intent: Get a Front Door security policy
    question: Which domains and WAF policy does one of my security policies cover?
  - id: SecurityPolicies_Create
    intent: Create a Front Door security policy
    question: How do I attach a WAF policy to my Front Door domains?
  - id: SecurityPolicies_Patch
    intent: Update an existing Front Door security policy
    question: Can I add more domains to a security policy I already have?
  - id: SecurityPolicies_Delete
    intent: Delete a Front Door security policy
    question: What happens to WAF protection when I delete a security policy?
  phrasing_ops: 5
  slug: microsoft-azure-cdn-security-policies-api
artifact_total: 95
collections:
- collection_type: open
  name: Azure CDN REST Operations API
  slug: open-microsoft-azure-cdn-operations-api
- collection_type: open
  name: Azure CDN REST Operations Profiles API
  slug: open-microsoft-azure-cdn-profiles-api
- collection_type: open
  name: Azure CDN REST API
  slug: open-microsoft-azure-cdn
common:
- group: design
  href: https://artifacts.apis.io/microsoft-azure-cdn/rules/microsoft-azure-cdn-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-azure-cdn-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-cdn/json-ld/microsoft-azure-cdn-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microsoft-azure-cdn-context.jsonld
- group: design
  href: https://artifacts.apis.io/microsoft-azure-cdn/vocabulary/microsoft-azure-cdn-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-azure-cdn-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-cdn/hosts/microsoft-azure-cdn-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-azure-cdn-hosts.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-cdn/vendors/microsoft-azure-cdn-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-azure-cdn-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://news.microsoft.com/leadership
- group: other
  href: https://artifacts.apis.io/microsoft-azure-cdn/capabilities/microsoft-azure-cdn-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/microsoft-azure-cdn-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-cdn/security/microsoft-azure-cdn-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/microsoft-azure-cdn-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-cdn/security/microsoft-azure-cdn-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-azure-cdn-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-cdn/agentic-access/microsoft-azure-cdn-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-cdn-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-cdn/security/microsoft-azure-cdn-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-cdn-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-cdn/authentication/microsoft-azure-cdn-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-cdn-authentication.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-cdn/scopes/microsoft-azure-cdn-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-cdn-scopes.yml
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
  url: https://azure.microsoft.com/en-us/pricing/
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
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/feed/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://learn.microsoft.com/en-us/rest/api/cdn/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/frontdoor/
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/rest/api/cdn/profiles
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/frontdoor/create-front-door-portal
- group: start
  title: ''
  type: SignUp
  url: https://azure.microsoft.com/en-us/free/
- group: operate
  title: ''
  type: StatusPage
  url: https://azure.status.microsoft/en-us/status
- group: operate
  href: https://artifacts.apis.io/microsoft-azure-cdn/lifecycle/microsoft-azure-cdn-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/microsoft-azure-cdn-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-cdn/lifecycle/microsoft-azure-cdn-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-azure-cdn-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-azure-cdn/changelog/microsoft-azure-cdn-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/microsoft-azure-cdn-changelog.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-cdn/cli/microsoft-azure-cdn-cli.yml
  title: ''
  type: CLI
  url: cli/microsoft-azure-cdn-cli.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-cdn/packages/microsoft-azure-cdn-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-azure-cdn-packages.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-cdn/packages/microsoft-azure-cdn-packages.yml
  title: ''
  type: SDKs
  url: packages/microsoft-azure-cdn-packages.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-cdn/conventions/microsoft-azure-cdn-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-azure-cdn-conventions.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-cdn/conventions/microsoft-azure-cdn-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/microsoft-azure-cdn-conventions.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-cdn/conformance/microsoft-azure-cdn-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-azure-cdn-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://learn.microsoft.com/en-us/azure/compliance/
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-cdn/security/microsoft-azure-cdn-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/microsoft-azure-cdn-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-cdn/well-known/microsoft-azure-cdn-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-azure-cdn-security.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-cdn/well-known/microsoft-azure-cdn-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-azure-cdn-well-known.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-cdn/mcp/microsoft-azure-cdn-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/microsoft-azure-cdn-mcp.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-cdn/mcp/microsoft-azure-cdn-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/microsoft-azure-cdn-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-cdn/llms/microsoft-azure-cdn-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-azure-cdn-llms.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-cdn/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-cdn/errors/microsoft-azure-cdn-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-azure-cdn-problem-types.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-cdn/data-model/microsoft-azure-cdn-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-azure-cdn-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-cdn/plans/microsoft-azure-cdn-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-azure-cdn-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-azure-cdn/rate-limits/microsoft-azure-cdn-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-azure-cdn-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-cdn/finops/microsoft-azure-cdn-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-azure-cdn-finops.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-cdn/examples/microsoft-azure-cdn-examples.yml
  title: ''
  type: Examples
  url: examples/microsoft-azure-cdn-examples.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-cdn/overlays/microsoft-azure-cdn-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-azure-cdn-management-overlay.yaml
- group: operate
  title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/options/
created: '2026-03-13'
description: 'Azure Content Delivery Network (CDN) caches static web content at strategically placed edge locations to deliver it to users with maximum throughput and minimum latency. The product is operated through the Microsoft.Cdn Azure Resource Manager resource provider, a 115-operation REST contract on management.azure.com that manages CDN profiles, delivery endpoints, origins, origin groups, custom domains and web application firewall policies, and that also serves the Azure Front Door Standard and Premium resource family. Authentication is Microsoft Entra ID OAuth 2.0 with authorization decided by Azure RBAC. Azure CDN Standard from Microsoft (classic) is on a published retirement path: it stopped accepting new instances in 2025 and retires on 30 September 2027, with Microsoft directing customers to Azure Front Door and shipping a validate/migrate/commit API path for the move.'
finops:
- has_sources: true
  method: derived
  name: Microsoft Azure Cdn Finops
  primary_unit: ''
  service_category: ''
  slug: microsoft-azure-cdn-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-cdn.png
json_schemas:
- name: AfdPurgeParameters
  property_count: 2
  slug: microsoft-azure-cdn-afd-purge-parameters
- name: AFDDomainListResult
  property_count: 2
  slug: microsoft-azure-cdn-afddomain-list-result
- name: AFDDomain
  property_count: 1
  slug: microsoft-azure-cdn-afddomain
- name: AFDDomainUpdateParameters
  property_count: 1
  slug: microsoft-azure-cdn-afddomain-update-parameters
- name: AFDEndpointListResult
  property_count: 2
  slug: microsoft-azure-cdn-afdendpoint-list-result
- name: AFDEndpoint
  property_count: 1
  slug: microsoft-azure-cdn-afdendpoint
- name: AFDEndpointUpdateParameters
  property_count: 2
  slug: microsoft-azure-cdn-afdendpoint-update-parameters
- name: AFDOriginGroupListResult
  property_count: 2
  slug: microsoft-azure-cdn-afdorigin-group-list-result
- name: AFDOriginGroup
  property_count: 1
  slug: microsoft-azure-cdn-afdorigin-group
- name: AFDOriginGroupUpdateParameters
  property_count: 1
  slug: microsoft-azure-cdn-afdorigin-group-update-parameters
- name: AFDOriginListResult
  property_count: 2
  slug: microsoft-azure-cdn-afdorigin-list-result
- name: AFDOrigin
  property_count: 1
  slug: microsoft-azure-cdn-afdorigin
- name: AFDOriginUpdateParameters
  property_count: 1
  slug: microsoft-azure-cdn-afdorigin-update-parameters
- name: CdnWebApplicationFirewallPolicyList
  property_count: 2
  slug: microsoft-azure-cdn-cdn-web-application-firewall-policy-list
- name: CdnWebApplicationFirewallPolicyPatchParameters
  property_count: 1
  slug: microsoft-azure-cdn-cdn-web-application-firewall-policy-patch-parameters
- name: CdnWebApplicationFirewallPolicy
  property_count: 3
  slug: microsoft-azure-cdn-cdn-web-application-firewall-policy
- name: CheckEndpointNameAvailabilityInput
  property_count: 3
  slug: microsoft-azure-cdn-check-endpoint-name-availability-input
- name: CheckEndpointNameAvailabilityOutput
  property_count: 4
  slug: microsoft-azure-cdn-check-endpoint-name-availability-output
- name: CheckNameAvailabilityInput
  property_count: 2
  slug: microsoft-azure-cdn-check-name-availability-input
- name: CheckNameAvailabilityOutput
  property_count: 3
  slug: microsoft-azure-cdn-check-name-availability-output
- name: CustomDomainHttpsParameters
  property_count: 3
  slug: microsoft-azure-cdn-custom-domain-https-parameters
- name: CustomDomainListResult
  property_count: 2
  slug: microsoft-azure-cdn-custom-domain-list-result
- name: CustomDomainParameters
  property_count: 1
  slug: microsoft-azure-cdn-custom-domain-parameters
- name: CustomDomain
  property_count: 1
  slug: microsoft-azure-cdn-custom-domain
- name: EdgenodeResult
  property_count: 2
  slug: microsoft-azure-cdn-edgenode-result
- name: EndpointListResult
  property_count: 2
  slug: microsoft-azure-cdn-endpoint-list-result
- name: Endpoint
  property_count: 1
  slug: microsoft-azure-cdn-endpoint
- name: EndpointUpdateParameters
  property_count: 2
  slug: microsoft-azure-cdn-endpoint-update-parameters
- name: ManagedRuleSetDefinitionList
  property_count: 2
  slug: microsoft-azure-cdn-managed-rule-set-definition-list
- name: MigrationParameters
  property_count: 4
  slug: microsoft-azure-cdn-migration-parameters
- name: OperationsListResult
  property_count: 2
  slug: microsoft-azure-cdn-operations-list-result
- name: OriginGroupListResult
  property_count: 2
  slug: microsoft-azure-cdn-origin-group-list-result
- name: OriginGroup
  property_count: 1
  slug: microsoft-azure-cdn-origin-group
- name: OriginGroupUpdateParameters
  property_count: 1
  slug: microsoft-azure-cdn-origin-group-update-parameters
- name: OriginListResult
  property_count: 2
  slug: microsoft-azure-cdn-origin-list-result
- name: Origin
  property_count: 1
  slug: microsoft-azure-cdn-origin
- name: OriginUpdateParameters
  property_count: 1
  slug: microsoft-azure-cdn-origin-update-parameters
- name: Profile
  property_count: 4
  slug: microsoft-azure-cdn-profile
- name: ProfileUpdateParameters
  property_count: 3
  slug: microsoft-azure-cdn-profile-update-parameters
- name: PurgeParameters
  property_count: 1
  slug: microsoft-azure-cdn-purge-parameters
- name: ResourceUsageListResult
  property_count: 2
  slug: microsoft-azure-cdn-resource-usage-list-result
- name: RouteListResult
  property_count: 2
  slug: microsoft-azure-cdn-route-list-result
- name: Route
  property_count: 1
  slug: microsoft-azure-cdn-route
- name: RouteUpdateParameters
  property_count: 1
  slug: microsoft-azure-cdn-route-update-parameters
- name: RuleListResult
  property_count: 2
  slug: microsoft-azure-cdn-rule-list-result
- name: Rule
  property_count: 1
  slug: microsoft-azure-cdn-rule
- name: RuleSetListResult
  property_count: 2
  slug: microsoft-azure-cdn-rule-set-list-result
- name: RuleSet
  property_count: 1
  slug: microsoft-azure-cdn-rule-set
- name: RuleUpdateParameters
  property_count: 1
  slug: microsoft-azure-cdn-rule-update-parameters
- name: SecretListResult
  property_count: 2
  slug: microsoft-azure-cdn-secret-list-result
- name: Secret
  property_count: 1
  slug: microsoft-azure-cdn-secret
- name: SecurityPolicyListResult
  property_count: 2
  slug: microsoft-azure-cdn-security-policy-list-result
- name: SecurityPolicy
  property_count: 1
  slug: microsoft-azure-cdn-security-policy
- name: SecurityPolicyUpdateParameters
  property_count: 1
  slug: microsoft-azure-cdn-security-policy-update-parameters
- name: UsagesListResult
  property_count: 2
  slug: microsoft-azure-cdn-usages-list-result
- name: ValidateCustomDomainOutput
  property_count: 3
  slug: microsoft-azure-cdn-validate-custom-domain-output
- name: ValidateProbeOutput
  property_count: 3
  slug: microsoft-azure-cdn-validate-probe-output
- name: ValidateSecretInput
  property_count: 3
  slug: microsoft-azure-cdn-validate-secret-input
jsonld:
- class_count: 120
  name: Microsoft Azure Cdn Context
  property_count: 140
  slug: microsoft-azure-cdn-context
layout: provider
mcp_servers:
- description: Remote MCP server at learn.microsoft.com.
  name: Microsoft Azure Cdn MCP Server
  slug: microsoft-azure-cdn-mcp-yml
modified: '2026-09-17'
name: Microsoft Azure Cdn
nav: Providers
network: true
overview: 'Microsoft Azure Cdn publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including microsoft-azure-cdn Operations API, microsoft-azure-cdn Profiles API, AFD Domains API, and 15 more. Tagged areas include CDN, Edge, Caching, Cloud Infrastructure, and Networking.


  The Microsoft Azure Cdn catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Microsoft Azure Cdn''s developer surface includes authentication, developer portal, pricing, support, engineering blog, documentation, API reference, and 45 more developer resources.'
plans:
- name: Microsoft Azure Cdn Plans Pricing
  plan_count: 3
  slug: microsoft-azure-cdn-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 6
  name: Microsoft Azure Cdn Rate Limits
  slug: microsoft-azure-cdn-rate-limits
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: Microsoft Azure Cdn API Rules
  rule_count: 57
  severity_counts:
    error: 42
    hint: 0
    info: 6
    warn: 9
  slug: microsoft-azure-cdn-rules
scopes:
- name: Microsoft Azure Cdn Scopes
  scope_count: 2
  slug: microsoft-azure-cdn-scopes
  summary_line: 2 scopes · implicit
score:
  band: exemplar
  composite: 76.9
  coverage:
    artifact_dirs: 36
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.0
  facets:
    access_clarity: 92.1
    contract_governance: 35.6
    contract_quality: 59.8
    developer_ergonomics: 73.2
    discoverability: 76.7
    operational_transparency: 84.2
  previous_composite: 72.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/microsoft-azure-cdn/microsoft-azure-cdn-2026-06-20T185404.png
security:
- kind: authentication
  name: Microsoft Azure Cdn Authentication
  slug: microsoft-azure-cdn-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Cdn Domain Security
  slug: microsoft-azure-cdn-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Azure Cdn Vulnerability Disclosure
  slug: microsoft-azure-cdn-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Azure Cdn Trust Center
  slug: microsoft-azure-cdn-trust-center
  summary_line: GDPR
skill_count: 4
skills:
- name: audit-profiles-and-usage
  slug: microsoft-azure-cdn-audit-profiles-and-usage
- name: migrate-to-front-door
  slug: microsoft-azure-cdn-migrate-to-front-door
- name: provision-cdn-profile-and-endpoint
  slug: microsoft-azure-cdn-provision-cdn-profile-and-endpoint
- name: purge-cached-content
  slug: microsoft-azure-cdn-purge-cached-content
slug: microsoft-azure-cdn
tags:
- CDN
- Edge
- Caching
- Cloud Infrastructure
- Networking
- Web Performance
- Microsoft Azure
- Content Delivery
- Web Application Firewall
website: https://www.microsoft.com/
---
