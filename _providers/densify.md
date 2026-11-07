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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    mcp_server: templated
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 35
  human_in_the_loop: 0
  name: Densify Agentic Access
  operation_count: 73
  slug: densify-agentic-access
  summary_line: 73 operations · 35 acting
api_count: 23
apis:
- baseURL: https://{host}/api/v2
  baseurl_source: declared
  description: The Analysis Webhook API from Densify — 2 operation(s) for analysis webhook.
  name: Densify Analysis Webhook API
  phrasing_intents:
  - id: listAnalysisWebhooksByPlatform
    intent: List analysis webhooks for a platform
    question: Which analyses already have a results webhook configured for my cloud platform?
  - id: getAnalysisWebhook
    intent: Get the webhook set on one analysis
    question: What webhook URI is a specific analysis currently delivering its results to?
  - id: addAnalysisWebhook
    intent: Attach a new webhook to an analysis
    question: How do I get analysis results pushed to my endpoint when an analysis has no webhook yet?
  - id: updateAnalysisWebhook
    intent: Change the webhook on an analysis
    question: Can I point an analysis's existing webhook to a new URL?
  - id: deleteAnalysisWebhook
    intent: Remove the webhook from an analysis
    question: How do I stop an analysis from posting results to my webhook?
  phrasing_ops: 5
  slug: densify-analysis-webhook-api
- baseURL: https://{host}/api/v2
  baseurl_source: declared
  description: The Authentication API from Densify — 1 operation(s) for authentication.
  name: Densify Authentication API
  phrasing_intents:
  - id: authorize
    intent: Get a JWT bearer token
    question: How do I get a bearer token to call the Kubex API?
  phrasing_ops: 1
  slug: densify-authentication-api
- baseURL: https://{host}/api/v2
  baseurl_source: declared
  description: The AWS Analysis API from Densify — 2 operation(s) for aws analysis.
  name: Densify AWS Analysis API
  phrasing_intents:
  - id: deleteAwsAnalysis
    intent: Delete an AWS cloud connection and analysis
    question: How do I stop analyzing an AWS account and remove its cloud connection?
  - id: getAwsRecommendations
    intent: Get AWS rightsizing recommendations for an analysis
    question: Which EC2, RDS and ASG instances should I resize in my analyzed AWS account?
  phrasing_ops: 2
  slug: densify-aws-analysis-api
- baseURL: https://{host}/api/v2
  baseurl_source: declared
  description: The AWS Analyze API from Densify — 2 operation(s) for aws analyze.
  name: Densify AWS Analyze API
  phrasing_intents:
  - id: analyzeAws
    intent: Onboard an AWS account for analysis
    question: How do I connect an AWS account so its CloudWatch data gets analyzed nightly?
  - id: listAwsAnalyses
    intent: List AWS accounts under analysis
    question: Which AWS accounts is Kubex currently analyzing?
  phrasing_ops: 2
  slug: densify-aws-analyze-api
- baseURL: https://{host}/api/v2
  baseurl_source: declared
  description: The Azure Analysis API from Densify — 5 operation(s) for azure analysis.
  name: Densify Azure Analysis API
  phrasing_intents:
  - id: analyzeAzure
    intent: Onboard an Azure subscription for analysis
    question: How do I connect an Azure subscription so it gets optimization analysis every night?
  - id: listAzureAnalyses
    intent: List Azure subscriptions under analysis
    question: Which Azure subscriptions are being analyzed right now?
  - id: getAzureAnalysisStatus
    intent: Check analysis status for an Azure subscription
    question: Has data collection finished for my Azure subscription yet?
  - id: deleteAzureAnalysisAudit
    intent: Delete an Azure cloud connection and analysis
    question: How do I remove an Azure subscription's connection and analysis from Kubex?
  - id: listAzureRecommendations
    intent: Get Azure VM recommendations for an analysis
    question: Which Azure virtual machines should be upsized or downsized?
  phrasing_ops: 5
  slug: densify-azure-analysis-api
- baseURL: https://{host}/api/v2
  baseurl_source: declared
  description: The Cloud Analysis API from Densify — 3 operation(s) for cloud analysis.
  name: Densify Cloud Analysis API
  phrasing_intents:
  - id: startAwsAnalysis
    intent: Start AWS collection with access keys (legacy)
    question: Can I start AWS data collection with an access key and secret instead of an IAM role?
  - id: startAzureAnalysis
    intent: Start Azure collection with access keys (legacy)
    question: Is there a simpler endpoint to start Azure collection with just an account number and keys?
  - id: startGcpAnalysis
    intent: Start GCP collection with access keys (legacy)
    question: Can I start GCP data collection with an access key pair rather than a service account?
  phrasing_ops: 3
  slug: densify-cloud-analysis-api
- baseURL: https://{host}/api/v2
  baseurl_source: declared
  description: The GCP Analysis API from Densify — 5 operation(s) for gcp analysis.
  name: Densify GCP Analysis API
  phrasing_intents:
  - id: analyzeGcp
    intent: Onboard a GCP project or re-run its analysis
    question: How do I connect a GCP project with a service account so it's analyzed nightly?
  - id: historicalAuditGcp
    intent: Run a one-off 30-day historical audit on GCP
    question: Can I backfill up to 30 days of history for a GCP project I already connected?
  - id: listGcpAnalyses
    intent: List GCP projects under analysis
    question: Which GCP projects have analyses generated in Kubex?
  - id: deleteGcpAnalysisAudit
    intent: Delete a GCP cloud connection and analysis
    question: How do I remove a GCP project's cloud connection and analysis?
  - id: listGcpRecommendations
    intent: Get Compute Engine recommendations for a GCP analysis
    question: Which Compute Engine instances in my GCP project should be resized?
  phrasing_ops: 5
  slug: densify-gcp-analysis-api
- baseURL: https://{host}/api/v2
  baseurl_source: declared
  description: The Kubernetes API from Densify — 2 operation(s) for kubernetes.
  name: Densify Kubernetes API
  phrasing_intents:
  - id: listKubernetesClusters
    intent: List monitored Kubernetes clusters
    question: Which Kubernetes clusters is Kubex monitoring?
  - id: getKubernetesContainers
    intent: Get container recommendations for a cluster
    question: What CPU and memory changes are recommended for containers in my cluster?
  phrasing_ops: 2
  slug: densify-kubernetes-api
- baseURL: https://{host}/api/v2
  baseurl_source: declared
  description: Container recommendations for a given cluster
  name: Densify Kubernetes Cluster Results API
  phrasing_intents:
  - id: getKubernetesClusterContainers
    intent: List base container recommendations for a cluster
    question: What are the base container manifest recommendations for my cluster?
  - id: getKubernetesClusterContainersDetailed
    intent: List detailed container recommendations
    question: Which containers in my cluster had OOM kills in the last 7 days?
  phrasing_ops: 2
  slug: densify-kubernetes-cluster-results-api
- baseURL: https://{host}/api/v2
  baseurl_source: declared
  description: Clusters discovered via the data forwarder
  name: Densify Kubernetes Clusters API
  phrasing_intents:
  - id: listKubernetesClusters
    intent: List Kubernetes clusters collecting data
    question: Which Kubernetes clusters is data being collected from?
  - id: getKubernetesClusterDetails
    intent: Get namespaces, pods and containers of a cluster
    question: What namespaces and pods are in one of my Kubernetes clusters?
  phrasing_ops: 2
  slug: densify-kubernetes-clusters-api
- baseURL: https://{host}/api/v2
  baseurl_source: declared
  description: The Recommendations API from Densify — 3 operation(s) for recommendations.
  name: Densify Recommendations API
  phrasing_intents:
  - id: getAwsRecommendations
    intent: Retrieve AWS optimization recommendations
    question: What AWS optimization recommendations came out of my analysis?
  - id: getAzureRecommendations
    intent: Retrieve Azure optimization recommendations
    question: What Azure optimization recommendations did my analysis produce?
  - id: getGcpRecommendations
    intent: Retrieve GCP optimization recommendations
    question: What GCP optimization recommendations did my analysis return?
  phrasing_ops: 3
  slug: densify-recommendations-api
- baseURL: https://{host}/api/v2
  baseurl_source: declared
  description: The Subscriptions API from Densify — 6 operation(s) for subscriptions.
  name: Densify Subscriptions API
  phrasing_intents:
  - id: listSubscriptionsDefaultPlatform
    intent: List cloud subscriptions (default alias)
    question: Can I list my subscriptions without specifying a platform?
  - id: listSubscriptions
    intent: List subscriptions for a platform
    question: Which recommendation subscriptions exist for containers?
  - id: createSubscriptions
    intent: Create subscriptions in bulk
    question: How do I create several recommendation subscriptions in one request?
  - id: deleteSubscriptions
    intent: Delete several subscriptions at once
    question: Can I delete a set of subscriptions in one call?
  - id: replaceSubscription
    intent: Replace a subscription's settings
    question: How do I change a subscription's webhook or schedule?
  - id: deleteSubscription
    intent: Delete one subscription
    question: How do I delete a single subscription?
  - id: getSubscriptionResults
    intent: Get a subscription's current results
    question: What recommendations does a subscription return right now, on demand?
  - id: getSubscriptionResultsDefaultPlatform
    intent: Get subscription results (default cloud alias)
    question: Can I get a subscription's results without naming the platform in the path?
  phrasing_ops: 10
  slug: densify-subscriptions-api
- baseURL: https://{host}/api/v2
  baseurl_source: declared
  description: The Subscriptions Properties API from Densify — 3 operation(s) for subscriptions properties.
  name: Densify Subscriptions Properties API
  phrasing_intents:
  - id: listSubscriptionProperties
    intent: List subscription properties for a platform
    question: Which properties are in the containers catalog for subscriptions?
  - id: addSubscriptionProperties
    intent: Add properties to a catalog in bulk
    question: How do I add new properties to the subscription catalog?
  - id: replaceSubscriptionProperties
    intent: Replace several properties at once
    question: Can I edit several catalog properties in one request?
  - id: deleteSubscriptionProperties
    intent: Delete several properties at once
    question: Can I delete multiple catalog properties in one call?
  - id: getSubscriptionProperty
    intent: Get one catalog property
    question: How do I look up a single subscription property by its ID?
  - id: replaceSubscriptionProperty
    intent: Replace a single property
    question: How do I rename one catalog property or change its alias?
  - id: deleteSubscriptionProperty
    intent: Delete one property
    question: How do I remove a single property from the catalog?
  - id: listSubscriptionPropertiesDefaultPlatform
    intent: List properties (default cloud alias)
    question: Can I list catalog properties without naming a platform?
  phrasing_ops: 8
  slug: densify-subscriptions-properties-api
- baseURL: https://{host}/api/v2
  baseurl_source: declared
  description: The Subscriptions Suppressions API from Densify — 3 operation(s) for subscriptions suppressions.
  name: Densify Subscriptions Suppressions API
  phrasing_intents:
  - id: listSuppressions
    intent: List suppressions for a platform
    question: Which suppressions are defined for my containers subscriptions?
  - id: createSuppressions
    intent: Add suppressions in bulk
    question: How do I suppress a resource tag or container label from subscription results?
  - id: replaceSuppressions
    intent: Replace several suppressions at once
    question: Can I update multiple suppressions in one request?
  - id: deleteSuppressions
    intent: Delete several suppressions at once
    question: Can I delete a list of suppressions in one call?
  - id: getSuppression
    intent: Get one suppression
    question: How do I look up a single suppression by its ID?
  - id: replaceSuppression
    intent: Replace a single suppression
    question: How do I change what attribute one suppression hides?
  - id: deleteSuppression
    intent: Delete one suppression
    question: How do I remove a single suppression?
  - id: listSuppressionsDefaultPlatform
    intent: List suppressions (default cloud alias)
    question: Can I list suppressions without naming the platform?
  phrasing_ops: 8
  slug: densify-subscriptions-suppressions-api
- baseURL: https://{host}/api/v2
  baseurl_source: declared
  description: The Subscriptions Tags API from Densify — 3 operation(s) for subscriptions tags.
  name: Densify Subscriptions Tags API
  phrasing_intents:
  - id: listSubscriptionTags
    intent: List subscription tags for a platform
    question: Which tags are in the containers catalog for subscriptions?
  - id: addSubscriptionTags
    intent: Add tags to a catalog in bulk
    question: How do I add resource tags to the subscription catalog?
  - id: replaceSubscriptionTags
    intent: Replace several tags at once
    question: Can I edit multiple catalog tags in one request?
  - id: deleteSubscriptionTags
    intent: Delete several tags at once
    question: Can I delete a list of catalog tags in one call?
  - id: getSubscriptionTag
    intent: Get one catalog tag
    question: How do I look up a single tag by its ID?
  - id: replaceSubscriptionTag
    intent: Replace a single tag
    question: How do I rename one catalog tag or change its attribute?
  - id: deleteSubscriptionTag
    intent: Delete one tag
    question: How do I remove a single tag from the catalog?
  - id: listSubscriptionTagsDefaultPlatform
    intent: List tags (default cloud alias)
    question: Can I list catalog tags without naming the platform?
  phrasing_ops: 8
  slug: densify-subscriptions-tags-api
- baseURL: https://{host}/api/v2
  baseurl_source: declared
  description: The System API from Densify — 1 operation(s) for system.
  name: Densify System API
  phrasing_intents:
  - id: ping
    intent: Check the API is reachable
    question: Is the Kubex API up and reachable from my network?
  phrasing_ops: 1
  slug: densify-system-api
- baseURL: https://{host}/api/v2
  baseurl_source: declared
  description: Systems collection and single-system resources
  name: Densify Systems API
  phrasing_intents:
  - id: listSystems
    intent: List systems tracked by data collection
    question: Which systems has recent data collection picked up?
  - id: getSystem
    intent: Get one system's configuration and attributes
    question: What configuration and attributes does a specific system have?
  - id: getSystemAnalysisDetails
    intent: Get instance type details and optimal targets
    question: What are the optimal instance types for one of my systems?
  - id: downloadAnalysisReport
    intent: Download a system's impact analysis PDF
    question: Can I download the Application Owner report for a system as a PDF?
  - id: modifySystemAttributes
    intent: Set or add attribute values on a system
    question: How do I update attribute values on a system?
  - id: deleteSystemAttributes
    intent: Delete attribute values from a system
    question: How do I remove an attribute value from a system?
  phrasing_ops: 6
  slug: densify-systems-api
artifact_total: 37
asyncapis:
- description: ''
  name: Densify Webhooks
  slug: densify-webhooks
collections:
- collection_type: open
  name: Densify / Kubex Public Cloud Authentication API
  slug: open-densify-authentication-api
- collection_type: open
  name: Densify / Kubex Public Cloud Authentication Cloud Analysis API
  slug: open-densify-cloud-analysis-api
- collection_type: open
  name: Densify / Kubex Public Cloud Authentication Kubernetes API
  slug: open-densify-kubernetes-api
- collection_type: open
  name: Densify / Kubex Public Cloud Authentication Recommendations API
  slug: open-densify-recommendations-api
- collection_type: open
  name: Densify / Kubex Public Cloud Authentication System API
  slug: open-densify-system-api
- collection_type: open
  name: Densify / Kubex Public Cloud API
  slug: open-densify
common:
- group: commercial
  href: https://artifacts.apis.io/densify/finops/densify-finops.yml
  title: ''
  type: FinOps
  url: finops/densify-finops.yml
- group: other
  href: https://artifacts.apis.io/densify/capabilities/densify-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/densify-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/densify/overlays/densify-authorize-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/densify-authorize-overlay.yaml
- group: other
  href: https://artifacts.apis.io/densify/overlays/densify-ping-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/densify-ping-overlay.yaml
- group: other
  href: https://artifacts.apis.io/densify/overlays/densify-public-cloud-analysis-aws-analyze-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/densify-public-cloud-analysis-aws-analyze-overlay.yaml
- group: other
  href: https://artifacts.apis.io/densify/overlays/densify-public-cloud-analysis-aws-delete-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/densify-public-cloud-analysis-aws-delete-overlay.yaml
- group: other
  href: https://artifacts.apis.io/densify/overlays/densify-public-cloud-analysis-aws-results-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/densify-public-cloud-analysis-aws-results-overlay.yaml
- group: other
  href: https://artifacts.apis.io/densify/overlays/densify-public-cloud-analysis-azure-analyze-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/densify-public-cloud-analysis-azure-analyze-overlay.yaml
- group: other
  href: https://artifacts.apis.io/densify/overlays/densify-public-cloud-analysis-azure-delete-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/densify-public-cloud-analysis-azure-delete-overlay.yaml
- group: other
  href: https://artifacts.apis.io/densify/overlays/densify-public-cloud-analysis-azure-results-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/densify-public-cloud-analysis-azure-results-overlay.yaml
- group: other
  href: https://artifacts.apis.io/densify/overlays/densify-public-cloud-analysis-gcp-analyze-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/densify-public-cloud-analysis-gcp-analyze-overlay.yaml
- group: other
  href: https://artifacts.apis.io/densify/overlays/densify-public-cloud-analysis-gcp-delete-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/densify-public-cloud-analysis-gcp-delete-overlay.yaml
- group: other
  href: https://artifacts.apis.io/densify/overlays/densify-public-cloud-analysis-gcp-results-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/densify-public-cloud-analysis-gcp-results-overlay.yaml
- group: other
  href: https://artifacts.apis.io/densify/overlays/densify-public-cloud-analysis-webhook-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/densify-public-cloud-analysis-webhook-overlay.yaml
- group: other
  href: https://artifacts.apis.io/densify/overlays/densify-public-cloud-subscriptions-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/densify-public-cloud-subscriptions-overlay.yaml
- group: other
  href: https://artifacts.apis.io/densify/overlays/densify-public-cloud-subscriptions-properties-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/densify-public-cloud-subscriptions-properties-overlay.yaml
- group: other
  href: https://artifacts.apis.io/densify/overlays/densify-public-cloud-subscriptions-results-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/densify-public-cloud-subscriptions-results-overlay.yaml
- group: other
  href: https://artifacts.apis.io/densify/overlays/densify-public-cloud-subscriptions-status-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/densify-public-cloud-subscriptions-status-overlay.yaml
- group: other
  href: https://artifacts.apis.io/densify/overlays/densify-public-cloud-subscriptions-suppressions-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/densify-public-cloud-subscriptions-suppressions-overlay.yaml
- group: other
  href: https://artifacts.apis.io/densify/overlays/densify-public-cloud-subscriptions-tags-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/densify-public-cloud-subscriptions-tags-overlay.yaml
- group: other
  href: https://artifacts.apis.io/densify/overlays/densify-systems-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/densify-systems-overlay.yaml
- group: other
  href: https://artifacts.apis.io/densify/overlays/densify-kubernetes-kubernetes-clusters-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/densify-kubernetes-kubernetes-clusters-overlay.yaml
- group: other
  href: https://artifacts.apis.io/densify/overlays/densify-kubernetes-kubernetes-clusters-results-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/densify-kubernetes-kubernetes-clusters-results-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://kubex.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.kubex.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kubex.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.kubex.ai/docs-api/WebHelp_Densify_API_Cloud/Content/API_Guide/API_Reference_Public_Cloud
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.kubex.ai/docs-kubex/Content/Kubex/Automation_Engine_Getting_Started
- group: build
  title: ''
  type: Postman
  url: https://docs.kubex.ai/docs-api/WebHelp_Densify_API_Cloud/Content/API_Guide/Postman_Collection
- group: operate
  title: ''
  type: Support
  url: https://kubex.ai/contact/
- group: operate
  title: ''
  type: Contact
  url: https://kubex.ai/contact/
- group: company
  title: ''
  type: Blog
  url: https://kubex.ai/blog/
- group: other
  title: ''
  type: Resources
  url: https://kubex.ai/resources/
- group: commercial
  title: ''
  type: Pricing
  url: https://kubex.ai/pricing/
- group: commercial
  href: https://artifacts.apis.io/densify/plans/densify-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/densify-plans-pricing.yml
- group: start
  title: ''
  type: SignUp
  url: https://kubex.ai/product/trial/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kubex.ai/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kubex.ai/legal/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/densify-dev
- group: company
  title: ''
  type: LinkedIn
  url: https://ca.linkedin.com/company/kubex-ai
- group: operate
  title: ''
  type: StatusPage
  url: https://kubex.statuspage.io
- group: operate
  href: https://artifacts.apis.io/densify/changelog/densify-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/densify-changelog.yml
- group: design
  href: https://artifacts.apis.io/densify/lifecycle/densify-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/densify-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/densify/authentication/densify-authentication.yml
  title: ''
  type: Authentication
  url: authentication/densify-authentication.yml
- group: design
  href: https://artifacts.apis.io/densify/conventions/densify-conventions.yml
  title: ''
  type: Conventions
  url: conventions/densify-conventions.yml
- group: design
  href: https://artifacts.apis.io/densify/errors/densify-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/densify-problem-types.yml
- group: design
  href: https://artifacts.apis.io/densify/data-model/densify-data-model.yml
  title: ''
  type: DataModel
  url: data-model/densify-data-model.yml
- group: operate
  href: https://artifacts.apis.io/densify/rate-limits/densify-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/densify-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/densify/asyncapi/densify-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/densify-webhooks.yml
- group: build
  href: https://artifacts.apis.io/densify/packages/densify-packages.yml
  title: ''
  type: Packages
  url: packages/densify-packages.yml
- group: build
  href: https://artifacts.apis.io/densify/packages/densify-packages.yml
  title: ''
  type: SDKs
  url: packages/densify-packages.yml
- group: other
  href: https://artifacts.apis.io/densify/grpc/densify-kubexrecommendation.proto
  title: ''
  type: Protobuf
  url: grpc/densify-kubexrecommendation.proto
- group: agent
  href: https://artifacts.apis.io/densify/mcp/densify-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/densify-mcp.yml
- group: build
  href: https://artifacts.apis.io/densify/mcp/densify-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/densify-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/densify/a2a/densify-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/densify-a2a.yml
- group: agent
  href: https://artifacts.apis.io/densify/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/densify/well-known/densify-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/densify-well-known.yml
- group: agent
  href: https://artifacts.apis.io/densify/agentic-access/densify-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/densify-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/densify/conformance/densify-conformance.yml
  title: ''
  type: Conformance
  url: conformance/densify-conformance.yml
- group: auth
  href: https://artifacts.apis.io/densify/conformance/densify-conformance.yml
  title: ''
  type: Compliance
  url: conformance/densify-conformance.yml
- group: auth
  href: https://artifacts.apis.io/densify/security/densify-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/densify-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/densify/security/densify-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/densify-domain-security.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.kubex.ai/llms.txt
- group: agent
  href: https://artifacts.apis.io/densify/llms/densify-docs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/densify-docs-llms.txt
- group: design
  href: https://artifacts.apis.io/densify/json-ld/densify-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/densify-context.jsonld
- group: design
  href: https://artifacts.apis.io/densify/vocabulary/densify-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/densify-vocabulary.yml
created: '2026-03-16'
description: Densify — now trading as Kubex — provides a machine-learning driven cloud, GPU and container optimization platform that continuously right-sizes resources to cut cost and protect performance across Kubernetes, public cloud and GPU/AI infrastructure. The Kubex REST API publishes 65 operations across 21 first-party OpenAPI documents covering cloud account onboarding and analysis, AWS/Azure/GCP right-sizing recommendations, Kubernetes cluster and container recommendations, the system inventory, analysis webhooks and a customizable Subscriptions surface, so optimization can be embedded into CI/CD pipelines, Terraform and other infrastructure-as-code, and FinOps workflows. Kubex also ships a per-tenant Model Context Protocol server and publishes an A2A agent card and an Agent Skill from its documentation host.
finops:
- has_sources: true
  method: derived
  name: Densify Finops
  primary_unit: vcpu
  service_category: ''
  slug: densify-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/densify.png
jsonld:
- class_count: 0
  name: Densify Context
  property_count: 6
  slug: densify-context
layout: provider
mcp_servers:
- description: Densify (trading as Kubex) publishes TWO distinct MCP servers. The product server is a per-tenant remote endpoint derived from the customer's dashboard hostname and is the one that exposes optimizatio
  name: Densify MCP Server
  slug: densify-mcp-yml
modified: '2026-09-06'
name: Densify
nav: Providers
network: true
overview: 'Densify publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analysis Webhook API, Authentication API, AWS Analysis API, and 14 more. Tagged areas include Cloud Cost, Container-Optimization, FinOps, Kubernetes, and Machine Learning.


  The Densify catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Densify''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 59 more developer resources.'
plans:
- name: Densify Plans Pricing
  plan_count: 2
  slug: densify-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Densify Rate Limits
  slug: densify-rate-limits
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: Densify API Rules
  rule_count: 58
  severity_counts:
    error: 44
    hint: 0
    info: 2
    warn: 12
  slug: densify-rules
score:
  band: exemplar
  composite: 71.2
  coverage:
    artifact_dirs: 34
    catalog_earned: 73.0
    catalog_earned_first_party: 16.0
    catalog_gap: 42.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 89.5
    contract_governance: 45.5
    contract_quality: 60.0
    developer_ergonomics: 75.5
    discoverability: 73.3
    operational_transparency: 63.2
  previous_composite: 71.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/densify/densify-2026-06-20T175916.png
security:
- kind: authentication
  name: Densify Authentication
  slug: densify-authentication
  summary_line: http/oauth2 · 1 scheme
- kind: domain-security
  name: Densify Domain Security
  slug: densify-domain-security
  summary_line: TLSv1.3
- kind: trust-center
  name: Densify Trust Center
  slug: densify-trust-center
  summary_line: SOC 2, ISO 27001
skill_count: 3
skills:
- name: Kubex
  slug: densify-kubex
- name: densify-onboard-cloud-account
  slug: densify-onboard-cloud-account
- name: densify-rightsize-containers
  slug: densify-rightsize-containers
slug: densify
tags:
- Cloud Cost
- Container-Optimization
- FinOps
- Kubernetes
- Machine Learning
- Recommendations
- Rightsizing
- A2A
website: https://kubex.ai/
---
