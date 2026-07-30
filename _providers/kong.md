---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 782
  human_in_the_loop: 122
  name: Kong Agentic Access
  operation_count: 1242
  slug: kong-agentic-access
  summary_line: 1242 operations · 782 acting · 122 human-in-the-loop
api_count: 139
apis:
- description: Kong Gateway is the open-source, lightweight, cloud-native API gateway optimized for microservices, delivering low-latency performance and scalability through a rich plugin ecosystem. It is the data-p
  name: Kong Gateway
  slug: kong
- description: 'Kong AI Gateway is the connectivity and governance layer for AI-native applications. Built on Kong Gateway, it provides a universal LLM API across providers (OpenAI, Anthropic, Gemini, Bedrock, Azure '
  name: Kong AI Gateway
  slug: kong-ai-gateway
- description: Kong Agent Gateway is a capability of Kong AI Gateway (GA April 2026 with AI Gateway 3.14) that governs agent-to-agent (A2A) communication. It enforces agent identity verification, real-time policy an
  name: Kong Agent Gateway
  slug: kong-agent-gateway
- description: Kong MCP Registry (launched February 2026) is an enterprise directory inside Kong Konnect for registering, discovering, and governing MCP servers and AI-native tools. It provides dynamic discovery for
  name: Kong MCP Registry
  slug: kong-mcp-registry
- description: Kong Context Mesh (launched February 2026, tech preview in Konnect) automatically discovers enterprise APIs, transforms them into agent-consumable tooling, packages them as MCP definitions with schema
  name: Kong Context Mesh
  slug: kong-context-mesh
- description: Kong Mesh is an enterprise-grade service mesh built on Kuma and Envoy, providing universal service mesh capabilities across Kubernetes and virtual machine environments. It supports mTLS, traffic polic
  name: Kong Mesh
  slug: kong-mesh
- description: Kong Insomnia is an open-source API development platform for designing, debugging, and testing APIs. It supports REST, GraphQL, gRPC, and WebSocket protocols and provides collections, environments, mo
  name: Kong Insomnia
  slug: kong-insomnia
- description: The ACLs API from Kong — 6 operation(s) for acls.
  name: Kong ACLs API
  slug: kong-acls-api
- description: The Add-Ons API from Kong — 2 operation(s) for add-ons.
  name: Kong Add-Ons API
  slug: kong-add-ons-api
- description: The API API from Kong — 2 operation(s) for api.
  name: Kong API API
  slug: kong-api-api
- description: The API Attributes API from Kong — 1 operation(s) for api attributes.
  name: Kong API Attributes API
  slug: kong-api-attributes-api
- description: The API Documentation API from Kong — 3 operation(s) for api documentation.
  name: Kong API Documentation API
  slug: kong-api-documentation-api
- description: The API Image API from Kong — 2 operation(s) for api image.
  name: Kong API Image API
  slug: kong-api-image-api
- description: The API Implementation API from Kong — 3 operation(s) for api implementation.
  name: Kong API Implementation API
  slug: kong-api-implementation-api
- description: The API-keys API from Kong — 6 operation(s) for api-keys.
  name: Kong API-keys API
  slug: kong-api-keys-api
- description: The API Operations API from Kong — 2 operation(s) for api operations.
  name: Kong API Operations API
  slug: kong-api-operations-api
- description: The API Package Documentation API from Kong — 3 operation(s) for api package documentation.
  name: Kong API Package Documentation API
  slug: kong-api-package-documentation-api
- description: The API Package Image API from Kong — 2 operation(s) for api package image.
  name: Kong API Package Image API
  slug: kong-api-package-image-api
- description: The API Package Operations API from Kong — 2 operation(s) for api package operations.
  name: Kong API Package Operations API
  slug: kong-api-package-operations-api
- description: The API Package Specification API from Kong — 2 operation(s) for api package specification.
  name: Kong API Package Specification API
  slug: kong-api-package-specification-api
- description: The API Packages API from Kong — 2 operation(s) for api packages.
  name: Kong API Packages API
  slug: kong-api-packages-api
- description: The API Publication API from Kong — 4 operation(s) for api publication.
  name: Kong API Publication API
  slug: kong-api-publication-api
- description: The API Specification API from Kong — 3 operation(s) for api specification.
  name: Kong API Specification API
  slug: kong-api-specification-api
- description: The API Version API from Kong — 2 operation(s) for api version.
  name: Kong API Version API
  slug: kong-api-version-api
- description: Application Auth Strategies are sets of plugin configurations that represent how the gateway will perform authentication and authorization for a Product Version. Called “Auth Strategy” for short in th
  name: Kong App Auth Strategies API
  slug: kong-app-auth-strategies-api
- description: APIs related to Konnect Developer Portal Application Registrations.
  name: Kong Application Registrations API
  slug: kong-application-registrations-api
- description: APIs related to Konnect Developer Portal Applications.
  name: Kong Applications API
  slug: kong-applications-api
- description: APIs for managing static assets for Konnect Developer Portals.
  name: Kong Assets API
  slug: kong-assets-api
- description: The Auth Settings API from Kong — 8 operation(s) for auth settings.
  name: Kong Auth Settings API
  slug: kong-auth-settings-api
- description: The Authentication API from Kong — 1 operation(s) for authentication.
  name: Kong Authentication API
  slug: kong-authentication-api
- description: The Basic-auth credentials API from Kong — 6 operation(s) for basic-auth credentials.
  name: Kong Basic-auth credentials API
  slug: kong-basic-auth-credentials-api
- description: A CA certificate object represents a trusted certificate authority. These objects are used by Kong Gateway to verify the validity of a client or server certificate.
  name: Kong CA Certificates API
  slug: kong-ca-certificates-api
- description: Integrations are applications, either Konnect-internal or external, which extend the functionality of the Service Catalog. Install and authorize an integration to discover the resources across your or
  name: Kong Catalog Integrations API
  slug: kong-catalog-integrations-api
- description: Resource mappings represent the link between a resource and a service. Once a resource is mapped to a service, a rich view of the resource will be presented on the service page. A resource may be mapp
  name: Kong Catalog Resource Mappings API
  slug: kong-catalog-resource-mappings-api
- description: Represents all the services mapped to a specific resource.
  name: Kong Catalog Resource Services API
  slug: kong-catalog-resource-services-api
- description: Resources are entities discovered from integration instances and are intended to be mapped to the relevant services in the catalog. Once a resource has been mapped to a service, a rich view of this re
  name: Kong Catalog Resources API
  slug: kong-catalog-resources-api
- description: Service API mappings represent the link between Service and API entities. Once an API is mapped to a Service, a rich view of the linked APIs will be presented on the APIs tab of the Catalog Service. S
  name: Kong Catalog Service API Mappings API
  slug: kong-catalog-service-api-mappings-api
- description: Represents all the resources mapped to a specific service.
  name: Kong Catalog Service Resources API
  slug: kong-catalog-service-resources-api
- description: Create and maintain a centralized catalog of all services running in your organization. Add custom fields and map resources from across your organization to provide a 360-degree overview of your servi
  name: Kong Catalog Services API
  slug: kong-catalog-services-api
- description: A certificate object represents a public certificate, and can be optionally paired with the corresponding private key. These objects are used by Kong Gateway to handle SSL/TLS termination for encrypte
  name: Kong Certificates API
  slug: kong-certificates-api
- description: The Cloud Gateways Resource Quotas API from Kong — 3 operation(s) for cloud gateways resource quotas.
  name: Kong Cloud Gateways Resource Quotas API
  slug: kong-cloud-gateways-resource-quotas-api
- description: Config Store Secrets
  name: Kong Config Store Secrets API
  slug: kong-config-store-secrets-api
- description: Config Stores
  name: Kong Config Stores API
  slug: kong-config-stores-api
- description: Consumer groups enable the organization and categorization of consumers (users or applications) within an API ecosystem. By grouping consumers together, you eliminate the need to manage them individua
  name: Kong Consumer Groups API
  slug: kong-consumer-groups-api
- description: The consumer object represents a consumer - or a user - of a service. You can either rely on Kong Gateway as the primary datastore, or you can map the consumer list with your database to keep consiste
  name: Kong Consumers API
  slug: kong-consumers-api
- description: The Control Plane Groups API from Kong — 5 operation(s) for control plane groups.
  name: Kong Control Plane Groups API
  slug: kong-control-plane-groups-api
- description: The Control Planes API from Kong — 2 operation(s) for control planes.
  name: Kong Control Planes API
  slug: kong-control-planes-api
- description: Several criteria templates are provided to help ensure your services adhere to industry best practices. A criteria template is a collection of criteria grouped together to target various categories. C
  name: Kong Criteria Templates API
  slug: kong-criteria-templates-api
- description: The Custom Domains API from Kong — 3 operation(s) for custom domains.
  name: Kong Custom Domains API
  slug: kong-custom-domains-api
- description: Custom Plugin Schemas
  name: Kong Custom Plugin Schemas API
  slug: kong-custom-plugin-schemas-api
- description: The CustomPlugins API from Kong — 2 operation(s) for customplugins.
  name: Kong CustomPlugins API
  slug: kong-customplugins-api
- description: The Dashboards API from Kong — 2 operation(s) for dashboards.
  name: Kong Dashboards API
  slug: kong-dashboards-api
- description: The Data-Plane Group Configurations API from Kong — 2 operation(s) for data-plane group configurations.
  name: Kong Data-Plane Group Configurations API
  slug: kong-data-plane-group-configurations-api
- description: Dynamic Client Registration Providers are configurations representing an external Identity Provider whose clients (i.e. Applications) Konnect will be authorized to manage. For instance, they will be a
  name: Kong DCR Providers API
  slug: kong-dcr-providers-api
- description: The Degraphql_routes API from Kong — 4 operation(s) for degraphql_routes.
  name: Kong Degraphql_routes API
  slug: kong-degraphql-routes-api
- description: DP Certificates
  name: Kong DP Certificates API
  slug: kong-dp-certificates-api
- description: DP Nodes
  name: Kong DP Nodes API
  slug: kong-dp-nodes-api
- description: A backend cluster is an abstraction of a real Kafka cluster. It stores the connection and configuration details required for Kong Event Gateway to proxy traffic to Kafka. Multiple Kafka clusters can b
  name: Kong Event Gateway Backend Clusters API
  slug: kong-event-gateway-backend-clusters-api
- description: DataPlane certificates control how your running Event Gateway instances connect to the Control Plane
  name: Kong Event Gateway DataPlane Certificates API
  slug: kong-event-gateway-dataplane-certificates-api
- description: Policies control how Kafka protocol traffic is modified between the client and the backend cluster. Listener policies are routing policies that pass traffic to the virtual cluster.
  name: Kong Event Gateway Listener Policies API
  slug: kong-event-gateway-listener-policies-api
- description: A listener represents hostname-port or IP-port combinations that connect to TCP sockets. Listeners need at least as many ports as backend brokers if you use port mapping in a Forward to Virtual Cluste
  name: Kong Event Gateway Listeners API
  slug: kong-event-gateway-listeners-api
- description: The Event Gateway Nodes API from Kong — 4 operation(s) for event gateway nodes.
  name: Kong Event Gateway Nodes API
  slug: kong-event-gateway-nodes-api
- description: Configure a schema registry that can be used to validate payloads when producing/consuming messages
  name: Kong Event Gateway Schema Registries API
  slug: kong-event-gateway-schema-registries-api
- description: Static Keys are used by the Encrypt and Decrypt policies to encrypt data at rest
  name: Kong Event Gateway Static Keys API
  slug: kong-event-gateway-static-keys-api
- description: A TLS trust bundle defines a set of trusted certificate authorities (CAs) used for client certificate verification during mutual TLS (mTLS). Trust bundles are referenced by TLS listener policies to de
  name: Kong Event Gateway TLS Trust Bundles API
  slug: kong-event-gateway-tls-trust-bundles-api
- description: Consume policies operate on Kafka messages as they are read from a Kafka cluster. Transformations may be applied at consume time, but they are applied once per Consumer. Where possible, transofmration
  name: Kong Event Gateway Virtual Cluster Consume Policies API
  slug: kong-event-gateway-virtual-cluster-consume-policies-api
- description: Policies control how Kafka protocol traffic is modified between the client and the backend cluster. Cluster policies are transformation and validation policies that can be applied to Kafka messages.
  name: Kong Event Gateway Virtual Cluster Policies API
  slug: kong-event-gateway-virtual-cluster-policies-api
- description: Produce policies operate on Kafka messages before they are written to the Kafka cluster. Where possible, apply transformations to the data using produce policies rather than consume policies for maxim
  name: Kong Event Gateway Virtual Cluster Produce Policies API
  slug: kong-event-gateway-virtual-cluster-produce-policies-api
- description: Virtual clusters are the primary way clients interact with the Event Gateway proxy. They allow you to isolate clients from each other when connecting to the same backend cluster, and provide each clie
  name: Kong Event Gateway Virtual Clusters API
  slug: kong-event-gateway-virtual-clusters-api
- description: Create an Event Gateway Control Plane, used to store Event Gateway configuration
  name: Kong Event Gateways API
  slug: kong-event-gateways-api
- description: The GraphQL Cost Decorations API from Kong — 4 operation(s) for graphql cost decorations.
  name: Kong GraphQL Cost Decorations API
  slug: kong-graphql-cost-decorations-api
- description: Group routes
  name: Kong Groups API
  slug: kong-groups-api
- description: The HMAC-auth credentials API from Kong — 6 operation(s) for hmac-auth credentials.
  name: Kong HMAC-auth credentials API
  slug: kong-hmac-auth-credentials-api
- description: The Impersonation Settings API from Kong — 1 operation(s) for impersonation settings.
  name: Kong Impersonation Settings API
  slug: kong-impersonation-settings-api
- description: A integration instance may need to be provided with an auth config before authorizing the instance. Typically an auth config will be required when authorizing against a integration which is hosted wit
  name: Kong Integration Instance Auth Config API
  slug: kong-integration-instance-auth-config-api
- description: 'Represents the credentials use to authorize an integration instance. You will want to configure the integration instance settings and authorization configuration before authorizing the instance. This '
  name: Kong Integration Instance Auth Credentials API
  slug: kong-integration-instance-auth-credentials-api
- description: An integration instance represents a specific account of the integration which contains the resources used to manage and support your services. Some integrations provide configuration options to custo
  name: Kong Integration Instances API
  slug: kong-integration-instances-api
- description: The Invites API from Kong — 1 operation(s) for invites.
  name: Kong Invites API
  slug: kong-invites-api
- description: The JWTs API from Kong — 6 operation(s) for jwts.
  name: Kong JWTs API
  slug: kong-jwts-api
- description: A key object holds a representation of asymmetric keys in various formats. When Kong Gateway or a Kong plugin requires a specific public or private key to perform certain operations, it can use this e
  name: Kong Keys API
  slug: kong-keys-api
- description: A JSON Web key set. Key sets are the preferred way to expose keys to plugins because they tell the plugin where to look for keys or have a scoping mechanism to restrict plugins to specific keys.
  name: Kong KeySets API
  slug: kong-keysets-api
- description: The MCP Servers API from Kong — 9 operation(s) for mcp servers.
  name: Kong MCP Servers API
  slug: kong-mcp-servers-api
- description: The Me API from Kong — 2 operation(s) for me.
  name: Kong Me API
  slug: kong-me-api
- description: Metering events are used to track usage of your product or service. Events are processed asynchronously by the meters, so they may not be immediately available for querying.
  name: Kong Metering Events API
  slug: kong-metering-events-api
- description: Meters specify how to aggregate events for billing and analytics purposes. Meters can be configured with multiple aggregation methods and groupings. Multiple meters can be created for the same event t
  name: Kong Meters API
  slug: kong-meters-api
- description: The MTLS-auth credentials API from Kong — 6 operation(s) for mtls-auth credentials.
  name: Kong MTLS-auth credentials API
  slug: kong-mtls-auth-credentials-api
- description: The Networks API from Kong — 3 operation(s) for networks.
  name: Kong Networks API
  slug: kong-networks-api
- description: Operations related to notifications
  name: Kong Notifications API
  slug: kong-notifications-api
- description: Apps enable you to extend and customize billing and usage workflows by integrating with external systems and services. Apps can automate and enhance your billing ecosystem by supporting capabilities s
  name: Kong OpenMeter Apps API
  slug: kong-openmeter-apps-api
- description: Billing manages the billing profiles, currencies, cost bases, and invoices for customers.
  name: Kong OpenMeter Billing API
  slug: kong-openmeter-billing-api
- description: Customers are used to track usage of your product or service. Customers can be individuals or organizations that can subscribe to plans and have access to features.
  name: Kong OpenMeter Customers API
  slug: kong-openmeter-customers-api
- description: Entitlements are used to control access to features for customers.
  name: Kong OpenMeter Entitlements API
  slug: kong-openmeter-entitlements-api
- description: Subscriptions are used to track usage of your product or service. Subscriptions can be individuals or organizations that can subscribe to plans and have access to features.
  name: Kong OpenMeter Subscriptions API
  slug: kong-openmeter-subscriptions-api
- description: APIs related to Konnect Developer Portal Custom Pages.
  name: Kong Pages API
  slug: kong-pages-api
- description: The Partial Links API from Kong — 1 operation(s) for partial links.
  name: Kong Partial Links API
  slug: kong-partial-links-api
- description: 'Some entities in Kong Gateway share common configuration settings that often need to be repeated. For example, multiple plugins that connect to Redis may require the same connection settings. Without '
  name: Kong Partials API
  slug: kong-partials-api
- description: The Personal Access Tokens API from Kong — 3 operation(s) for personal access tokens.
  name: Kong Personal Access Tokens API
  slug: kong-personal-access-tokens-api
- description: A plugin entity represents a plugin configuration that will be executed during the HTTP request/response lifecycle. Plugins let you add functionality to services that run behind a Kong Gateway instanc
  name: Kong Plugins API
  slug: kong-plugins-api
- description: The Portal Audit Logs API from Kong — 3 operation(s) for portal audit logs.
  name: Kong Portal Audit Logs API
  slug: kong-portal-audit-logs-api
- description: APIs related to configuration of Konnect Developer Portal auth settings.
  name: Kong Portal Auth Settings API
  slug: kong-portal-auth-settings-api
- description: APIs related to configuration of Konnect Developer Portals custom domains.
  name: Kong Portal Custom Domains API
  slug: kong-portal-custom-domains-api
- description: APIs related to customization of Konnect Developer Portals.
  name: Kong Portal Customization API
  slug: kong-portal-customization-api
- description: APIs related to Konnect Developer Portal developers.
  name: Kong Portal Developers API
  slug: kong-portal-developers-api
- description: APIs related to Konnect Developer Portal Emails.
  name: Kong Portal Emails API
  slug: kong-portal-emails-api
- description: APIs to configure Konnect Developer Portal integrations.
  name: Kong Portal Integrations API
  slug: kong-portal-integrations-api
- description: APIs related to Konnect Developer Portal developer team membership.
  name: Kong Portal Team Membership API
  slug: kong-portal-team-membership-api
- description: APIs related to Konnect Developer Portal developer team roles.
  name: Kong Portal Team Roles API
  slug: kong-portal-team-roles-api
- description: APIs related to configuration of Konnect Developer Portal developer teams.
  name: Kong Portal Teams API
  slug: kong-portal-teams-api
- description: APIs related to configuration of Konnect Developer Portals.
  name: Kong Portals API
  slug: kong-portals-api
- description: APIs related to Konnect Portal IP Allow List.
  name: Kong Portals IP Allow List API
  slug: kong-portals-ip-allow-list-api
- description: The Private DNS API from Kong — 2 operation(s) for private dns.
  name: Kong Private DNS API
  slug: kong-private-dns-api
- description: The Provider Accounts API from Kong — 2 operation(s) for provider accounts.
  name: Kong Provider Accounts API
  slug: kong-provider-accounts-api
- description: The RBACRoleEndpoints API from Kong — 2 operation(s) for rbacroleendpoints.
  name: Kong RBACRoleEndpoints API
  slug: kong-rbacroleendpoints-api
- description: The RBACRoleEntities API from Kong — 2 operation(s) for rbacroleentities.
  name: Kong RBACRoleEntities API
  slug: kong-rbacroleentities-api
- description: The RBACRoles API from Kong — 2 operation(s) for rbacroles.
  name: Kong RBACRoles API
  slug: kong-rbacroles-api
- description: The RBACUserGroups API from Kong — 2 operation(s) for rbacusergroups.
  name: Kong RBACUserGroups API
  slug: kong-rbacusergroups-api
- description: The RBACUserRoles API from Kong — 1 operation(s) for rbacuserroles.
  name: Kong RBACUserRoles API
  slug: kong-rbacuserroles-api
- description: The RBACUsers API from Kong — 2 operation(s) for rbacusers.
  name: Kong RBACUsers API
  slug: kong-rbacusers-api
- description: The Resource Availability API from Kong — 1 operation(s) for resource availability.
  name: Kong Resource Availability API
  slug: kong-resource-availability-api
- description: The Resource Configurations API from Kong — 3 operation(s) for resource configurations.
  name: Kong Resource Configurations API
  slug: kong-resource-configurations-api
- description: The Roles API from Kong — 5 operation(s) for roles.
  name: Kong Roles API
  slug: kong-roles-api
- description: Route entities define rules to match client requests. Each route is associated with a service, and a service may have multiple routes associated to it. Every request matching a given route will be pro
  name: Kong Routes API
  slug: kong-routes-api
- description: The Schemas API from Kong — 2 operation(s) for schemas.
  name: Kong Schemas API
  slug: kong-schemas-api
- description: A scorecard helps you evaluate services based on its criteria. Scorecards help you detect issues, like whether there are services in the catalog that don't have an on-call engineer assigned, or if you
  name: Kong Scorecards API
  slug: kong-scorecards-api
- description: 'Service entities are abstractions of your microservice interfaces or formal APIs. For example, a service could be a data transformation microservice or a billing API. <br><br> The main attribute of a '
  name: Kong Services API
  slug: kong-services-api
- description: APIs related to Konnect Developer Portal Custom Snippets.
  name: Kong Snippets API
  slug: kong-snippets-api
- description: An SNI object represents a many-to-one mapping of hostnames to a certificate. <br><br> A certificate object can have many hostnames associated with it. When Kong Gateway receives an SSL request, it us
  name: Kong SNIs API
  slug: kong-snis-api
- description: The System Accounts - Access Tokens API from Kong — 2 operation(s) for system accounts - access tokens.
  name: Kong System Accounts - Access Tokens API
  slug: kong-system-accounts-access-tokens-api
- description: The System Accounts API from Kong — 2 operation(s) for system accounts.
  name: Kong System Accounts API
  slug: kong-system-accounts-api
- description: The System Accounts - Roles API from Kong — 2 operation(s) for system accounts - roles.
  name: Kong System Accounts - Roles API
  slug: kong-system-accounts-roles-api
- description: The System Accounts - Team Membership API from Kong — 3 operation(s) for system accounts - team membership.
  name: Kong System Accounts - Team Membership API
  slug: kong-system-accounts-team-membership-api
- description: A target is an IP address or hostname with a port that identifies an instance of a backend service. Every upstream can have many targets, and the targets can be dynamically added, modified, or deleted
  name: Kong Targets API
  slug: kong-targets-api
- description: The Team Membership API from Kong — 3 operation(s) for team membership.
  name: Kong Team Membership API
  slug: kong-team-membership-api
- description: The Teams API from Kong — 2 operation(s) for teams.
  name: Kong Teams API
  slug: kong-teams-api
- description: The Transit Gateways API from Kong — 2 operation(s) for transit gateways.
  name: Kong Transit Gateways API
  slug: kong-transit-gateways-api
- description: The upstream object represents a virtual hostname and can be used to load balance incoming requests over multiple services (targets). <br><br> An upstream also includes a [health checker](https://deve
  name: Kong Upstreams API
  slug: kong-upstreams-api
- description: The Users API from Kong — 2 operation(s) for users.
  name: Kong Users API
  slug: kong-users-api
- description: Vault objects are used to configure different vault connectors for [managing secrets](https://developer.konghq.com/gateway/secrets-management/). Configuring a vault lets you reference secrets from oth
  name: Kong Vaults API
  slug: kong-vaults-api
- description: 'The workspace object describes the workspace entity, which has an ID and a name. <br><br> Workspaces provide a way to segment Kong Gateway entities. Entities in a workspace are isolated from those in '
  name: Kong Workspaces API
  slug: kong-workspaces-api
artifact_total: 1651
collections:
- collection_type: postman
  name: Kong Enterprise Admin ACLs API
  slug: postman-kong-acls-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Add-Ons API
  slug: postman-kong-add-ons-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs API API
  slug: postman-kong-api-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs API Attributes API
  slug: postman-kong-api-attributes-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs API Documentation API
  slug: postman-kong-api-documentation-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs API Image API
  slug: postman-kong-api-image-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs API Implementation API
  slug: postman-kong-api-implementation-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs API-keys API
  slug: postman-kong-api-keys-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs API Operations API
  slug: postman-kong-api-operations-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs API Package Documentation API
  slug: postman-kong-api-package-documentation-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs API Package Image API
  slug: postman-kong-api-package-image-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs API Package Operations API
  slug: postman-kong-api-package-operations-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs API Package Specification API
  slug: postman-kong-api-package-specification-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs API Packages API
  slug: postman-kong-api-packages-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs API Publication API
  slug: postman-kong-api-publication-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs API Specification API
  slug: postman-kong-api-specification-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs API Version API
  slug: postman-kong-api-version-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs App Auth Strategies API
  slug: postman-kong-app-auth-strategies-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Application Registrations API
  slug: postman-kong-application-registrations-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Applications API
  slug: postman-kong-applications-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Assets API
  slug: postman-kong-assets-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Auth Settings API
  slug: postman-kong-auth-settings-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Authentication API
  slug: postman-kong-authentication-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Basic-auth credentials API
  slug: postman-kong-basic-auth-credentials-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs CA Certificates API
  slug: postman-kong-ca-certificates-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Catalog Integrations API
  slug: postman-kong-catalog-integrations-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Catalog Resource Mappings API
  slug: postman-kong-catalog-resource-mappings-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Catalog Resource Services API
  slug: postman-kong-catalog-resource-services-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Catalog Resources API
  slug: postman-kong-catalog-resources-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Catalog Service API Mappings API
  slug: postman-kong-catalog-service-api-mappings-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Catalog Service Resources API
  slug: postman-kong-catalog-service-resources-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Catalog Services API
  slug: postman-kong-catalog-services-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Certificates API
  slug: postman-kong-certificates-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Cloud Gateways Resource Quotas API
  slug: postman-kong-cloud-gateways-resource-quotas-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Config Store Secrets API
  slug: postman-kong-config-store-secrets-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Config Stores API
  slug: postman-kong-config-stores-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Consumer Groups API
  slug: postman-kong-consumer-groups-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Consumers API
  slug: postman-kong-consumers-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Control Plane Groups API
  slug: postman-kong-control-plane-groups-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Control Planes API
  slug: postman-kong-control-planes-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Criteria Templates API
  slug: postman-kong-criteria-templates-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Custom Domains API
  slug: postman-kong-custom-domains-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Custom Plugin Schemas API
  slug: postman-kong-custom-plugin-schemas-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs CustomPlugins API
  slug: postman-kong-customplugins-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Dashboards API
  slug: postman-kong-dashboards-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Data-Plane Group Configurations API
  slug: postman-kong-data-plane-group-configurations-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs DCR Providers API
  slug: postman-kong-dcr-providers-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Degraphql_routes API
  slug: postman-kong-degraphql-routes-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs DP Certificates API
  slug: postman-kong-dp-certificates-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs DP Nodes API
  slug: postman-kong-dp-nodes-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Event Gateway Backend Clusters API
  slug: postman-kong-event-gateway-backend-clusters-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Event Gateway DataPlane Certificates API
  slug: postman-kong-event-gateway-dataplane-certificates-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Event Gateway Listener Policies API
  slug: postman-kong-event-gateway-listener-policies-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Event Gateway Listeners API
  slug: postman-kong-event-gateway-listeners-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Event Gateway Nodes API
  slug: postman-kong-event-gateway-nodes-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Event Gateway Schema Registries API
  slug: postman-kong-event-gateway-schema-registries-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Event Gateway Static Keys API
  slug: postman-kong-event-gateway-static-keys-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Event Gateway TLS Trust Bundles API
  slug: postman-kong-event-gateway-tls-trust-bundles-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Event Gateway Virtual Cluster Consume Policies API
  slug: postman-kong-event-gateway-virtual-cluster-consume-policies-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Event Gateway Virtual Cluster Policies API
  slug: postman-kong-event-gateway-virtual-cluster-policies-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Event Gateway Virtual Cluster Produce Policies API
  slug: postman-kong-event-gateway-virtual-cluster-produce-policies-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Event Gateway Virtual Clusters API
  slug: postman-kong-event-gateway-virtual-clusters-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Event Gateways API
  slug: postman-kong-event-gateways-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs GraphQL Cost Decorations API
  slug: postman-kong-graphql-cost-decorations-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Groups API
  slug: postman-kong-groups-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs HMAC-auth credentials API
  slug: postman-kong-hmac-auth-credentials-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Impersonation Settings API
  slug: postman-kong-impersonation-settings-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Integration Instance Auth Config API
  slug: postman-kong-integration-instance-auth-config-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Integration Instance Auth Credentials API
  slug: postman-kong-integration-instance-auth-credentials-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Integration Instances API
  slug: postman-kong-integration-instances-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Invites API
  slug: postman-kong-invites-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs JWTs API
  slug: postman-kong-jwts-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Keys API
  slug: postman-kong-keys-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs KeySets API
  slug: postman-kong-keysets-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs MCP Servers API
  slug: postman-kong-mcp-servers-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Me API
  slug: postman-kong-me-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Metering Events API
  slug: postman-kong-metering-events-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Meters API
  slug: postman-kong-meters-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs MTLS-auth credentials API
  slug: postman-kong-mtls-auth-credentials-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Networks API
  slug: postman-kong-networks-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Notifications API
  slug: postman-kong-notifications-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs OpenMeter Apps API
  slug: postman-kong-openmeter-apps-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs OpenMeter Billing API
  slug: postman-kong-openmeter-billing-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs OpenMeter Customers API
  slug: postman-kong-openmeter-customers-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs OpenMeter Entitlements API
  slug: postman-kong-openmeter-entitlements-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs OpenMeter Subscriptions API
  slug: postman-kong-openmeter-subscriptions-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Pages API
  slug: postman-kong-pages-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Partial Links API
  slug: postman-kong-partial-links-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Partials API
  slug: postman-kong-partials-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Personal Access Tokens API
  slug: postman-kong-personal-access-tokens-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Plugins API
  slug: postman-kong-plugins-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Portal Audit Logs API
  slug: postman-kong-portal-audit-logs-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Portal Auth Settings API
  slug: postman-kong-portal-auth-settings-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Portal Custom Domains API
  slug: postman-kong-portal-custom-domains-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Portal Customization API
  slug: postman-kong-portal-customization-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Portal Developers API
  slug: postman-kong-portal-developers-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Portal Emails API
  slug: postman-kong-portal-emails-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Portal Integrations API
  slug: postman-kong-portal-integrations-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Portal Team Membership API
  slug: postman-kong-portal-team-membership-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Portal Team Roles API
  slug: postman-kong-portal-team-roles-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Portal Teams API
  slug: postman-kong-portal-teams-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Portals API
  slug: postman-kong-portals-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Portals IP Allow List API
  slug: postman-kong-portals-ip-allow-list-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Private DNS API
  slug: postman-kong-private-dns-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Provider Accounts API
  slug: postman-kong-provider-accounts-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs RBACRoleEndpoints API
  slug: postman-kong-rbacroleendpoints-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs RBACRoleEntities API
  slug: postman-kong-rbacroleentities-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs RBACRoles API
  slug: postman-kong-rbacroles-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs RBACUserGroups API
  slug: postman-kong-rbacusergroups-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs RBACUserRoles API
  slug: postman-kong-rbacuserroles-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs RBACUsers API
  slug: postman-kong-rbacusers-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Resource Availability API
  slug: postman-kong-resource-availability-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Resource Configurations API
  slug: postman-kong-resource-configurations-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Roles API
  slug: postman-kong-roles-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Routes API
  slug: postman-kong-routes-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Schemas API
  slug: postman-kong-schemas-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Scorecards API
  slug: postman-kong-scorecards-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Services API
  slug: postman-kong-services-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Snippets API
  slug: postman-kong-snippets-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs SNIs API
  slug: postman-kong-snis-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs System Accounts - Access Tokens API
  slug: postman-kong-system-accounts-access-tokens-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs System Accounts API
  slug: postman-kong-system-accounts-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs System Accounts - Roles API
  slug: postman-kong-system-accounts-roles-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs System Accounts - Team Membership API
  slug: postman-kong-system-accounts-team-membership-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Targets API
  slug: postman-kong-targets-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Team Membership API
  slug: postman-kong-team-membership-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Teams API
  slug: postman-kong-teams-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Transit Gateways API
  slug: postman-kong-transit-gateways-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Upstreams API
  slug: postman-kong-upstreams-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Users API
  slug: postman-kong-users-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Vaults API
  slug: postman-kong-vaults-api
- collection_type: postman
  name: Kong Enterprise Admin ACLs Workspaces API
  slug: postman-kong-workspaces-api
- collection_type: open
  name: Kong Enterprise Admin API
  slug: open-kong-gateway-admin-api
- collection_type: open
  name: Konnect API - Go SDK
  slug: open-kong-konnect-platform-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/kong/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kong-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kong-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kong-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/konghq
- group: docs
  title: ''
  type: Documentation
  url: https://developer.konghq.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.konghq.com/gateway/install/
- group: company
  title: ''
  type: Blog
  url: https://konghq.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.konghq.com/gateway/changelog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Kong
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Kong/kong
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Kong/sdk-konnect-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Kong/sdk-portal-js
- group: build
  title: ''
  type: CLI
  url: https://github.com/Kong/kongctl
- group: operate
  title: ''
  type: Support
  url: https://discuss.konghq.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://konghq.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/kong-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kong-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/kong-finops.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/kong-service-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/kong-context.jsonld
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/Kong/mcp-konnect
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.konghq.com/llms.txt
created: '2026-03-18'
description: Kong is the AI Connectivity Company. Its platform spans Kong Gateway (the open-source API gateway built on NGINX and Lua), Kong Konnect (the SaaS control plane), Kong AI Gateway (LLM, MCP, and agent-to-agent traffic governance with semantic caching, token budgeting, and prompt firewalls), Kong Agent Gateway, Kong Event Gateway (Kafka-native governance), Kong Mesh (service mesh on Kuma and Envoy), Kong MCP Registry (centralized directory of MCP servers and tools for AI agents), Kong Context Mesh, and Kong Insomnia (API design and testing). Together they unify governance across APIs, real-time event streams, LLM calls, MCP tools, and agent-to-agent communication for the agentic era.
examples:
- key_count: 9
  name: Kong Gateway Admin Certificate Example
  slug: kong-gateway-admin-certificate-example
- key_count: 6
  name: Kong Gateway Admin Certificate Input Example
  slug: kong-gateway-admin-certificate-input-example
- key_count: 3
  name: Kong Gateway Admin Certificate List Example
  slug: kong-gateway-admin-certificate-list-example
- key_count: 6
  name: Kong Gateway Admin Consumer Example
  slug: kong-gateway-admin-consumer-example
- key_count: 3
  name: Kong Gateway Admin Consumer Input Example
  slug: kong-gateway-admin-consumer-input-example
- key_count: 3
  name: Kong Gateway Admin Consumer List Example
  slug: kong-gateway-admin-consumer-list-example
- key_count: 4
  name: Kong Gateway Admin Error Example
  slug: kong-gateway-admin-error-example
- key_count: 3
  name: Kong Gateway Admin Healthchecks Example
  slug: kong-gateway-admin-healthchecks-example
- key_count: 8
  name: Kong Gateway Admin Node Info Example
  slug: kong-gateway-admin-node-info-example
- key_count: 4
  name: Kong Gateway Admin Node Status Example
  slug: kong-gateway-admin-node-status-example
- key_count: 14
  name: Kong Gateway Admin Plugin Example
  slug: kong-gateway-admin-plugin-example
- key_count: 11
  name: Kong Gateway Admin Plugin Input Example
  slug: kong-gateway-admin-plugin-input-example
- key_count: 3
  name: Kong Gateway Admin Plugin List Example
  slug: kong-gateway-admin-plugin-list-example
- key_count: 23
  name: Kong Gateway Admin Route Example
  slug: kong-gateway-admin-route-example
- key_count: 20
  name: Kong Gateway Admin Route Input Example
  slug: kong-gateway-admin-route-input-example
- key_count: 3
  name: Kong Gateway Admin Route List Example
  slug: kong-gateway-admin-route-list-example
- key_count: 19
  name: Kong Gateway Admin Service Example
  slug: kong-gateway-admin-service-example
- key_count: 16
  name: Kong Gateway Admin Service Input Example
  slug: kong-gateway-admin-service-input-example
- key_count: 3
  name: Kong Gateway Admin Service List Example
  slug: kong-gateway-admin-service-list-example
- key_count: 7
  name: Kong Gateway Admin Target Example
  slug: kong-gateway-admin-target-example
- key_count: 3
  name: Kong Gateway Admin Target Input Example
  slug: kong-gateway-admin-target-input-example
- key_count: 3
  name: Kong Gateway Admin Target List Example
  slug: kong-gateway-admin-target-list-example
- key_count: 19
  name: Kong Gateway Admin Upstream Example
  slug: kong-gateway-admin-upstream-example
- key_count: 16
  name: Kong Gateway Admin Upstream Input Example
  slug: kong-gateway-admin-upstream-input-example
- key_count: 3
  name: Kong Gateway Admin Upstream List Example
  slug: kong-gateway-admin-upstream-list-example
features:
- description: Extensible plugin architecture for authentication, rate limiting, logging, transformations, and custom business logic on data-plane Kong Gateway.
  name: Plugin Ecosystem
- description: Define upstream services and routing rules to direct client requests to the correct backend services.
  name: Service and Route Management
- description: Create and manage API consumers with per-consumer authentication credentials and plugin configurations.
  name: Consumer Management
- description: Built-in upstream load balancing with health checks, circuit breaking, and weighted target distribution.
  name: Load Balancing
- description: Manage TLS certificates and SNI mappings for secure HTTPS traffic termination at the gateway.
  name: TLS Certificate Management
- description: Configure Kong Gateway declaratively using decK or the Admin API for infrastructure-as-code workflows.
  name: Declarative Configuration
- description: Centralized cloud control plane for managing multiple Kong Gateway instances, teams, API products, and Dev Portals.
  name: Kong Konnect Cloud Platform
- description: Provider-agnostic LLM proxy across OpenAI, Anthropic, Gemini, Bedrock, Azure AI, Databricks, Mistral, HuggingFace and more, with semantic caching and token-level governance.
  name: Universal LLM API
- description: Centralized directory of MCP servers and tools that AI agents can discover, with enforcement of approved resources only.
  name: MCP Registry and Tool Governance
- description: Kong Agent Gateway provides identity, policy, and observability for A2A traffic patterns inside AI Gateway 3.14+.
  name: Agent-to-Agent Governance
- description: Kong Event Gateway proxies native Kafka protocol traffic with virtual clusters, identity-aware ACLs, and quotas.
  name: Kafka-Native Event Governance
- description: Enterprise service mesh built on Kuma and Envoy for mTLS, traffic policies, and multi-zone deployments.
  name: Service Mesh with Kong Mesh
finops:
- name: Kong Finops
  service_category: API Management
  slug: kong-finops
graphqls:
- description: ''
  name: Kong GraphQL API
  slug: kong-graphql
image: /assets/icons/kong.png
integrations:
- description: Deploy Kong Gateway as a Kubernetes Ingress Controller or via the Kong Operator, with CRD-based configuration for cloud-native environments.
  name: Kubernetes
- description: Export gateway metrics to Prometheus and visualize API performance and health in Grafana dashboards.
  name: Prometheus and Grafana
- description: Distributed tracing integration with OpenTelemetry for end-to-end request visibility across services, LLM calls, and A2A traffic.
  name: OpenTelemetry
- description: Secrets management integration for storing and retrieving API keys, certificates, and credentials.
  name: HashiCorp Vault
- description: Send gateway logs, metrics, and traces to Datadog for comprehensive API and AI monitoring and alerting.
  name: Datadog
- description: Reference architecture for combining Kong AI Gateway with Akamai distributed compute for edge-terminated LLM traffic.
  name: Akamai
json_schemas:
- name: AcePlugin
  property_count: 0
  slug: kong-aceplugin
- name: AcePluginConfig
  property_count: 5
  slug: kong-acepluginconfig
- name: ACL
  property_count: 5
  slug: kong-acl
- name: ACLPlugin
  property_count: 0
  slug: kong-aclplugin
- name: ACLPluginConfig
  property_count: 5
  slug: kong-aclpluginconfig
- name: ACLWithoutParents
  property_count: 5
  slug: kong-aclwithoutparents
- name: AcmePlugin
  property_count: 0
  slug: kong-acmeplugin
- name: AcmePluginConfig
  property_count: 3
  slug: kong-acmepluginconfig
- name: AddDeveloperToTeamRequest
  property_count: 1
  slug: kong-adddevelopertoteamrequest
- name: Add-On Config Kind
  property_count: 0
  slug: kong-addonconfigkind
- name: AddOnConfigKindFieldEqualsComparison
  property_count: 1
  slug: kong-addonconfigkindfieldequalscomparison
- name: Add-On Config Kind Field Equals Filter
  property_count: 0
  slug: kong-addonconfigkindfieldequalsfilter
- name: Add-On Config Kind Field Filter
  property_count: 0
  slug: kong-addonconfigkindfieldfilter
- name: Add-On Config Kind Field Not Equals Filter
  property_count: 1
  slug: kong-addonconfigkindfieldnotequalsfilter
- name: Add-On Config Kind Field Or Equality Filter
  property_count: 1
  slug: kong-addonconfigkindfieldorequalityfilter
- name: AddOnConfigResponse
  property_count: 0
  slug: kong-addonconfigresponse
- name: AddOnId
  property_count: 0
  slug: kong-addonid
- name: AddOnName
  property_count: 0
  slug: kong-addonname
- name: AddOnOwner
  property_count: 0
  slug: kong-addonowner
- name: AddOnResponse
  property_count: 8
  slug: kong-addonresponse
- name: Add-Ons Filter Parameters
  property_count: 7
  slug: kong-addonsfilterparameters
- name: Add-On State
  property_count: 0
  slug: kong-addonstate
- name: AddOnStateFieldEqualsComparison
  property_count: 1
  slug: kong-addonstatefieldequalscomparison
- name: AddOnStateFieldEqualsFilter
  property_count: 0
  slug: kong-addonstatefieldequalsfilter
- name: AddOnStateFieldFilter
  property_count: 0
  slug: kong-addonstatefieldfilter
- name: AddOnStateFieldNotEqualsFilter
  property_count: 1
  slug: kong-addonstatefieldnotequalsfilter
- name: AddOnStateFieldOrEqualityFilter
  property_count: 1
  slug: kong-addonstatefieldorequalityfilter
- name: Address
  property_count: 7
  slug: kong-address
- name: AdvancedFilters
  property_count: 0
  slug: kong-advancedfilters
- name: AdvancedMetrics
  property_count: 0
  slug: kong-advancedmetrics
- name: AdvancedQuery
  property_count: 6
  slug: kong-advancedquery
- name: AgenticFilters
  property_count: 0
  slug: kong-agenticfilters
- name: AgenticMetrics
  property_count: 0
  slug: kong-agenticmetrics
- name: AgenticQuery
  property_count: 6
  slug: kong-agenticquery
- name: AiA2aProxyPlugin
  property_count: 0
  slug: kong-aia2aproxyplugin
- name: AiA2aProxyPluginConfig
  property_count: 5
  slug: kong-aia2aproxypluginconfig
- name: AiAwsGuardrailsPlugin
  property_count: 0
  slug: kong-aiawsguardrailsplugin
- name: AiAwsGuardrailsPluginConfig
  property_count: 7
  slug: kong-aiawsguardrailspluginconfig
- name: AiAzureContentSafetyPlugin
  property_count: 0
  slug: kong-aiazurecontentsafetyplugin
- name: AiAzureContentSafetyPluginConfig
  property_count: 5
  slug: kong-aiazurecontentsafetypluginconfig
- name: AiCustomGuardrailPlugin
  property_count: 0
  slug: kong-aicustomguardrailplugin
- name: AiCustomGuardrailPluginConfig
  property_count: 7
  slug: kong-aicustomguardrailpluginconfig
- name: AiGcpModelArmorPlugin
  property_count: 0
  slug: kong-aigcpmodelarmorplugin
- name: AiGcpModelArmorPluginConfig
  property_count: 7
  slug: kong-aigcpmodelarmorpluginconfig
- name: AiLakeraGuardPlugin
  property_count: 0
  slug: kong-ailakeraguardplugin
- name: AiLakeraGuardPluginConfig
  property_count: 7
  slug: kong-ailakeraguardpluginconfig
- name: AiLlmAsJudgePlugin
  property_count: 0
  slug: kong-aillmasjudgeplugin
- name: AiLlmAsJudgePluginConfig
  property_count: 7
  slug: kong-aillmasjudgepluginconfig
- name: AiMcpOauth2Plugin
  property_count: 0
  slug: kong-aimcpoauth2plugin
- name: AiMcpOauth2PluginConfig
  property_count: 5
  slug: kong-aimcpoauth2pluginconfig
- name: AiMcpProxyPlugin
  property_count: 0
  slug: kong-aimcpproxyplugin
- name: AiMcpProxyPluginConfig
  property_count: 5
  slug: kong-aimcpproxypluginconfig
- name: AiPromptCompressorPlugin
  property_count: 0
  slug: kong-aipromptcompressorplugin
- name: AiPromptCompressorPluginConfig
  property_count: 7
  slug: kong-aipromptcompressorpluginconfig
- name: AiPromptDecoratorPlugin
  property_count: 0
  slug: kong-aipromptdecoratorplugin
- name: AiPromptDecoratorPluginConfig
  property_count: 7
  slug: kong-aipromptdecoratorpluginconfig
- name: AiPromptGuardPlugin
  property_count: 0
  slug: kong-aipromptguardplugin
- name: AiPromptGuardPluginConfig
  property_count: 7
  slug: kong-aipromptguardpluginconfig
- name: AiPromptTemplatePlugin
  property_count: 0
  slug: kong-aiprompttemplateplugin
- name: AiPromptTemplatePluginConfig
  property_count: 7
  slug: kong-aiprompttemplatepluginconfig
- name: AiProxyAdvancedPlugin
  property_count: 0
  slug: kong-aiproxyadvancedplugin
- name: AiProxyAdvancedPluginConfig
  property_count: 7
  slug: kong-aiproxyadvancedpluginconfig
- name: AiProxyPlugin
  property_count: 0
  slug: kong-aiproxyplugin
- name: AiProxyPluginConfig
  property_count: 7
  slug: kong-aiproxypluginconfig
- name: AiRagInjectorPlugin
  property_count: 0
  slug: kong-airaginjectorplugin
- name: AiRagInjectorPluginConfig
  property_count: 7
  slug: kong-airaginjectorpluginconfig
- name: AiRateLimitingAdvancedPlugin
  property_count: 0
  slug: kong-airatelimitingadvancedplugin
- name: AiRateLimitingAdvancedPluginConfig
  property_count: 7
  slug: kong-airatelimitingadvancedpluginconfig
- name: AiRequestTransformerPlugin
  property_count: 0
  slug: kong-airequesttransformerplugin
- name: AiRequestTransformerPluginConfig
  property_count: 6
  slug: kong-airequesttransformerpluginconfig
- name: AiResponseTransformerPlugin
  property_count: 0
  slug: kong-airesponsetransformerplugin
- name: AiResponseTransformerPluginConfig
  property_count: 7
  slug: kong-airesponsetransformerpluginconfig
- name: AiSanitizerPlugin
  property_count: 0
  slug: kong-aisanitizerplugin
- name: AiSanitizerPluginConfig
  property_count: 7
  slug: kong-aisanitizerpluginconfig
- name: AiSemanticCachePlugin
  property_count: 0
  slug: kong-aisemanticcacheplugin
- name: AiSemanticCachePluginConfig
  property_count: 7
  slug: kong-aisemanticcachepluginconfig
- name: AiSemanticPromptGuardPlugin
  property_count: 0
  slug: kong-aisemanticpromptguardplugin
- name: AiSemanticPromptGuardPluginConfig
  property_count: 7
  slug: kong-aisemanticpromptguardpluginconfig
- name: AiSemanticResponseGuardPlugin
  property_count: 0
  slug: kong-aisemanticresponseguardplugin
- name: AiSemanticResponseGuardPluginConfig
  property_count: 7
  slug: kong-aisemanticresponseguardpluginconfig
- name: AllEntitiesSelector
  property_count: 2
  slug: kong-allentitiesselector
- name: AllFilterItems
  property_count: 3
  slug: kong-allfilteritems
- name: ApiAccess
  property_count: 0
  slug: kong-apiaccess
- name: API Attribute Filter Parameters
  property_count: 4
  slug: kong-apiattributefilterparameters
- name: API Attribute List Item
  property_count: 5
  slug: kong-apiattributelistitem
- name: API Attributes
  property_count: 0
  slug: kong-apiattributes
- name: API Document
  property_count: 8
  slug: kong-apidocument
- name: API Document Content
  property_count: 0
  slug: kong-apidocumentcontent
- name: API Document Filter Parameters
  property_count: 1
  slug: kong-apidocumentfilterparameters
- name: API Document ID
  property_count: 0
  slug: kong-apidocumentid
- name: API Document Parent Document ID
  property_count: 0
  slug: kong-apidocumentparentdocumentid
- name: API Document Slug
  property_count: 0
  slug: kong-apidocumentslug
- name: ApiDocumentStatus
  property_count: 0
  slug: kong-apidocumentstatus
- name: API Document Summary
  property_count: 8
  slug: kong-apidocumentsummarywithchildren
- name: API Document Title
  property_count: 0
  slug: kong-apidocumenttitle
- name: API Filter Parameters
  property_count: 8
  slug: kong-apifilterparameters
- name: Image Status
  property_count: 6
  slug: kong-apiimage
- name: API Implementation
  property_count: 0
  slug: kong-apiimplementation
- name: API Implementation Control Plane
  property_count: 2
  slug: kong-apiimplementationcontrolplane
- name: ApiImplementationControlPlaneEntity
  property_count: 4
  slug: kong-apiimplementationcontrolplaneentity
- name: API Implementation Filter Parameters
  property_count: 6
  slug: kong-apiimplementationfilterparameters
- name: ApiImplementationGatewayServiceEntity
  property_count: 4
  slug: kong-apiimplementationgatewayserviceentity
- name: API Implementation List Item
  property_count: 0
  slug: kong-apiimplementationlistitem
- name: ApiImplementationListItemControlPlaneEntity
  property_count: 5
  slug: kong-apiimplementationlistitemcontrolplaneentity
- name: ApiImplementationListItemGatewayServiceEntity
  property_count: 5
  slug: kong-apiimplementationlistitemgatewayserviceentity
- name: API Implementation Service
  property_count: 3
  slug: kong-apiimplementationservice
- name: ApiKeyCredentialListItem
  property_count: 6
  slug: kong-apikeycredentiallistitem
- name: API Operation
  property_count: 4
  slug: kong-apioperation
- name: API Operation Filter Parameters
  property_count: 2
  slug: kong-apioperationfilterparameters
- name: API Operation Implementation Status
  property_count: 3
  slug: kong-apioperationimplementationstatus
- name: API Package Filter Parameters
  property_count: 7
  slug: kong-apipackagefilterparameters
- name: Image Status
  property_count: 6
  slug: kong-apipackageimage
- name: APIPackageJSONPatchItem
  property_count: 3
  slug: kong-apipackagejsonpatchitem
- name: JSON Patch Operation
  property_count: 0
  slug: kong-apipackagejsonpatchoperation
- name: API Package Operation Response
  property_count: 8
  slug: kong-apipackageoperationresponseschema
- name: API Package Operations Filter Parameters
  property_count: 5
  slug: kong-apipackageoperationsfilterparameters
- name: API Package Publication
  property_count: 6
  slug: kong-apipackagepublication
- name: API Package
  property_count: 10
  slug: kong-apipackageresponseschema
- name: API Publication
  property_count: 6
  slug: kong-apipublication
- name: API Publication Auth Strategy IDs
  property_count: 0
  slug: kong-apipublicationauthstrategyids
- name: API Publication Filter Parameters
  property_count: 6
  slug: kong-apipublicationfilterparameters
- name: API Publication List Item
  property_count: 9
  slug: kong-apipublicationlistitem
- name: API Publication Visibility
  property_count: 0
  slug: kong-apipublicationvisibility
- name: API
  property_count: 13
  slug: kong-apiresponseschema
- name: API Specification
  property_count: 6
  slug: kong-apispec
- name: API Spec Filter Parameters
  property_count: 1
  slug: kong-apispecfilterparameters
- name: API Spec Type
  property_count: 0
  slug: kong-apispectype
- name: API Spec Filter Parameters
  property_count: 2
  slug: kong-apiversionfilterparameters
- name: API Version Request
  property_count: 2
  slug: kong-apiversionrequest
- name: API Version Summary
  property_count: 5
  slug: kong-apiversionsummary
- name: AppAuthStrategy
  property_count: 0
  slug: kong-appauthstrategy
- name: AppAuthStrategyConfigKeyAuth
  property_count: 2
  slug: kong-appauthstrategyconfigkeyauth
- name: AppAuthStrategyConfigOpenIDConnect
  property_count: 4
  slug: kong-appauthstrategyconfigopenidconnect
- name: AppAuthStrategyKeyAuthRequest
  property_count: 5
  slug: kong-appauthstrategykeyauthrequest
- name: AppAuthStrategyKeyAuthResponse
  property_count: 11
  slug: kong-appauthstrategykeyauthresponse
- name: AppAuthStrategyOpenIDConnectRequest
  property_count: 6
  slug: kong-appauthstrategyopenidconnectrequest
- name: AppAuthStrategyOpenIDConnectResponse
  property_count: 11
  slug: kong-appauthstrategyopenidconnectresponse
- name: AppDynamicsPlugin
  property_count: 0
  slug: kong-appdynamicsplugin
- name: AppDynamicsPluginConfig
  property_count: 6
  slug: kong-appdynamicspluginconfig
- name: Application
  property_count: 0
  slug: kong-application
- name: ApplicationDeveloperDetailed
  property_count: 3
  slug: kong-applicationdeveloperdetailed
- name: ApplicationOwner
  property_count: 2
  slug: kong-applicationowner
- name: ApplicationOwnerId
  property_count: 0
  slug: kong-applicationownerid
- name: ApplicationOwnerType
  property_count: 0
  slug: kong-applicationownertype
- name: ApplicationRegistration
  property_count: 6
  slug: kong-applicationregistration
- name: ApplicationRegistrationStatus
  property_count: 0
  slug: kong-applicationregistrationstatus
- name: AppPagePaginatedResponse
  property_count: 2
  slug: kong-apppagepaginatedresponse
- name: AssignedPortalRoleCollectionResponse
  property_count: 2
  slug: kong-assignedportalrolecollectionresponse
- name: AssignedRole
  property_count: 5
  slug: kong-assignedrole
- name: AttributesFieldFilter
  property_count: 0
  slug: kong-attributesfieldfilter
- name: AuthMethods
  property_count: 0
  slug: kong-authmethods
- name: AuthStrategyApiSyncError
  property_count: 3
  slug: kong-authstrategyapisyncerror
- name: AuthStrategyClientCredentials
  property_count: 5
  slug: kong-authstrategyclientcredentials
- name: AuthStrategyDisplayName
  property_count: 0
  slug: kong-authstrategydisplayname
- name: AuthStrategyKeyAuth
  property_count: 5
  slug: kong-authstrategykeyauth
- name: AuthStrategyName
  property_count: 0
  slug: kong-authstrategyname
- name: Auto Approve Registrations
  property_count: 0
  slug: kong-autoapproveregistrations
- name: Availability Document
  property_count: 4
  slug: kong-availabilitydocument
- name: AvailableScopes
  property_count: 0
  slug: kong-availablescopes
- name: AwsLambdaPlugin
  property_count: 0
  slug: kong-awslambdaplugin
- name: AwsLambdaPluginConfig
  property_count: 6
  slug: kong-awslambdapluginconfig
- name: AWS Private DNS Resolver Attachment Config
  property_count: 2
  slug: kong-awsprivatednsresolverattachmentconfig
- name: AwsPrivateDnsResolverResponse
  property_count: 8
  slug: kong-awsprivatednsresolverresponse
- name: AWS Private Hosted Zone Attachment Config
  property_count: 2
  slug: kong-awsprivatehostedzoneattachmentconfig
- name: AwsPrivateHostedZoneResponse
  property_count: 8
  slug: kong-awsprivatehostedzoneresponse
- name: AWS Resource Endpoint Attachment Config
  property_count: 3
  slug: kong-awsresourceendpointattachmentconfig
- name: AWS Resource Endpoint Attachment Config Response
  property_count: 3
  slug: kong-awsresourceendpointattachmentconfigresponse
- name: AWS Resource Endpoint Config
  property_count: 0
  slug: kong-awsresourceendpointconfig
- name: AWS Resource Endpoint Config Response
  property_count: 0
  slug: kong-awsresourceendpointconfigresponse
- name: AWS Resource Endpoint Config State
  property_count: 0
  slug: kong-awsresourceendpointconfigstate
- name: AWS Resource Endpoint Gateway
  property_count: 9
  slug: kong-awsresourceendpointgatewayresponse
- name: AWSRoleDelegationAuthCredential
  property_count: 8
  slug: kong-awsroledelegationauthcredential
- name: AWS Transit Gateway Attachment Config
  property_count: 3
  slug: kong-awstransitgatewayattachmentconfig
- name: AWS Transit Gateway Attachment Config
  property_count: 4
  slug: kong-awstransitgatewayattachmentconfigforresponse
- name: AWS Transit Gateway
  property_count: 10
  slug: kong-awstransitgatewayresponse
- name: AWS VPC Peering Attachment Config
  property_count: 4
  slug: kong-awsvpcpeeringgatewayattachmentconfig
- name: AWS VPC Peering Attachment Config
  property_count: 5
  slug: kong-awsvpcpeeringgatewayattachmentconfigforresponse
- name: AWS VPC Peering Gateway
  property_count: 10
  slug: kong-awsvpcpeeringgatewayresponse
- name: AzureFunctionsPlugin
  property_count: 0
  slug: kong-azurefunctionsplugin
- name: AzureFunctionsPluginConfig
  property_count: 6
  slug: kong-azurefunctionspluginconfig
- name: Azure Private DNS Resolver Attachment Config
  property_count: 2
  slug: kong-azureprivatednsresolverattachmentconfig
- name: AzurePrivateDnsResolverResponse
  property_count: 8
  slug: kong-azureprivatednsresolverresponse
- name: Azure Private Hosted Zone Attachment Config
  property_count: 6
  slug: kong-azureprivatehostedzoneattachmentconfig
- name: AzurePrivateHostedZoneResponse
  property_count: 8
  slug: kong-azureprivatehostedzoneresponse
- name: Azure Transit Gateway
  property_count: 9
  slug: kong-azuretransitgatewayresponse
- name: Azure Virtual Hub Peering Attachment Config
  property_count: 5
  slug: kong-azurevhubpeeringattachmentconfig
- name: Azure Virtual Hub Peering Gateway
  property_count: 9
  slug: kong-azurevhubpeeringgatewayresponse
- name: Azure VNET Peering Attachment Config
  property_count: 5
  slug: kong-azurevnetpeeringattachmentconfig
- name: BackendCluster
  property_count: 11
  slug: kong-backendcluster
- name: BackendClusterAuthenticationAnonymous
  property_count: 1
  slug: kong-backendclusterauthenticationanonymous
- name: BackendClusterAuthenticationSaslPlain
  property_count: 3
  slug: kong-backendclusterauthenticationsaslplain
- name: BackendClusterAuthenticationSaslPlainSensitiveDataAware
  property_count: 3
  slug: kong-backendclusterauthenticationsaslplainsensitivedataaware
- name: BackendClusterAuthenticationSaslScram
  property_count: 4
  slug: kong-backendclusterauthenticationsaslscram
- name: BackendClusterAuthenticationSaslScramSensitiveDataAware
  property_count: 4
  slug: kong-backendclusterauthenticationsaslscramsensitivedataaware
- name: BackendClusterAuthenticationScheme
  property_count: 0
  slug: kong-backendclusterauthenticationscheme
- name: BackendClusterAuthenticationSensitiveDataAwareScheme
  property_count: 0
  slug: kong-backendclusterauthenticationsensitivedataawarescheme
- name: BackendClusterName
  property_count: 0
  slug: kong-backendclustername
- name: BackendClusterReference
  property_count: 2
  slug: kong-backendclusterreference
- name: BackendClusterReferenceById
  property_count: 1
  slug: kong-backendclusterreferencebyid
- name: BackendClusterReferenceByName
  property_count: 1
  slug: kong-backendclusterreferencebyname
- name: BackendClusterReferenceModify
  property_count: 0
  slug: kong-backendclusterreferencemodify
- name: BackendClusterTLS
  property_count: 5
  slug: kong-backendclustertls
- name: BackendMetadataUpdateIntervalSeconds
  property_count: 0
  slug: kong-backendmetadataupdateintervalseconds
- name: BadRequestError
  property_count: 0
  slug: kong-badrequesterror
- name: Bar chart
  property_count: 3
  slug: kong-barchart
- name: Error
  property_count: 5
  slug: kong-baseerror
- name: BasicAuth
  property_count: 6
  slug: kong-basicauth
- name: BasicAuthPlugin
  property_count: 0
  slug: kong-basicauthplugin
- name: BasicAuthPluginConfig
  property_count: 5
  slug: kong-basicauthpluginconfig
- name: BasicAuthWithoutParents
  property_count: 6
  slug: kong-basicauthwithoutparents
- name: BasicDeveloper
  property_count: 6
  slug: kong-basicdeveloper
- name: BillingApp
  property_count: 0
  slug: kong-billingapp
- name: BillingAppCustomerData
  property_count: 2
  slug: kong-billingappcustomerdata
- name: BillingAppExternalInvoicing
  property_count: 12
  slug: kong-billingappexternalinvoicing
- name: BillingAppReference
  property_count: 1
  slug: kong-billingappreference
- name: BillingAppSandbox
  property_count: 10
  slug: kong-billingappsandbox
- name: BillingAppStripe
  property_count: 13
  slug: kong-billingappstripe
- name: BillingAppStripeCreateCheckoutSessionConsentCollectionPaymentMethodReuseAgreementPosition
  property_count: 0
  slug: kong-billingappstripecreatecheckoutsessionconsentcollectionpaymen
- name: BillingAppStripeCreateCheckoutSessionResult
  property_count: 17
  slug: kong-billingappstripecreatecheckoutsessionresult
- name: BillingAppStripeCreateCheckoutSessionTaxIdCollectionRequired
  property_count: 0
  slug: kong-billingappstripecreatecheckoutsessiontaxidcollectionrequired
- name: BillingAppStripeCreateCustomerPortalSessionResult
  property_count: 8
  slug: kong-billingappstripecreatecustomerportalsessionresult
- name: BillingCustomer
  property_count: 12
  slug: kong-billingcustomer
- name: BillingCustomerData
  property_count: 2
  slug: kong-billingcustomerdata
- name: BillingCustomerStripeCreateCheckoutSessionRequest
  property_count: 1
  slug: kong-billingcustomerstripecreatecheckoutsessionrequest
- name: BillingCustomerStripeCreateCustomerPortalSessionRequest
  property_count: 1
  slug: kong-billingcustomerstripecreatecustomerportalsessionrequest
- name: BillingEntitlementAccessResult
  property_count: 4
  slug: kong-billingentitlementaccessresult
- name: BillingProfile
  property_count: 11
  slug: kong-billingprofile
- name: BillingProfilePagePaginatedResponse
  property_count: 2
  slug: kong-billingprofilepagepaginatedresponse
- name: BillingSubscription
  property_count: 9
  slug: kong-billingsubscription
- name: BillingSubscriptionCancel
  property_count: 1
  slug: kong-billingsubscriptioncancel
- name: BillingSubscriptionChange
  property_count: 5
  slug: kong-billingsubscriptionchange
- name: BillingSubscriptionChangeResponse
  property_count: 2
  slug: kong-billingsubscriptionchangeresponse
- name: BillingSubscriptionCreate
  property_count: 4
  slug: kong-billingsubscriptioncreate
- name: BillingSubscriptionEditTimingEnum
  property_count: 0
  slug: kong-billingsubscriptionedittimingenum
- name: BillingTaxConfig
  property_count: 5
  slug: kong-billingtaxconfig
- name: BillingTaxIdentificationCode
  property_count: 0
  slug: kong-billingtaxidentificationcode
- name: BillingWorkflowCollectionAlignment
  property_count: 0
  slug: kong-billingworkflowcollectionalignment
- name: BillingWorkflowCollectionAlignmentAnchored
  property_count: 2
  slug: kong-billingworkflowcollectionalignmentanchored
- name: BillingWorkflowCollectionAlignmentSubscription
  property_count: 1
  slug: kong-billingworkflowcollectionalignmentsubscription
- name: Workflow collection settings
  property_count: 2
  slug: kong-billingworkflowcollectionsettings
- name: Workflow invoice settings
  property_count: 3
  slug: kong-billingworkflowinvoicingsettings
- name: BillingWorkflowPaymentChargeAutomaticallySettings
  property_count: 1
  slug: kong-billingworkflowpaymentchargeautomaticallysettings
- name: BillingWorkflowPaymentSendInvoiceSettings
  property_count: 2
  slug: kong-billingworkflowpaymentsendinvoicesettings
- name: BillingWorkflowPaymentSettings
  property_count: 0
  slug: kong-billingworkflowpaymentsettings
- name: Workflow tax settings
  property_count: 3
  slug: kong-billingworkflowtaxsettings
- name: BooleanConfigFieldSchema
  property_count: 6
  slug: kong-booleanconfigfieldschema
- name: BooleanCustomField
  property_count: 0
  slug: kong-booleancustomfield
- name: BooleanFieldFilter
  property_count: 0
  slug: kong-booleanfieldfilter
- name: BooleanSelectorOperator
  property_count: 0
  slug: kong-booleanselectoroperator
- name: BootstrapServers
  property_count: 0
  slug: kong-bootstrapservers
- name: BotDetectionPlugin
  property_count: 0
  slug: kong-botdetectionplugin
- name: BotDetectionPluginConfig
  property_count: 5
  slug: kong-botdetectionpluginconfig
- name: BulkPayload
  property_count: 2
  slug: kong-bulkpayload
- name: ByCustomFieldSelector
  property_count: 2
  slug: kong-bycustomfieldselector
- name: ByDisplayNameSelector
  property_count: 2
  slug: kong-bydisplaynameselector
- name: ByIDsSelector
  property_count: 2
  slug: kong-byidsselector
- name: ByLabelSelector
  property_count: 2
  slug: kong-bylabelselector
- name: ByNameSelector
  property_count: 2
  slug: kong-bynameselector
- name: CACertificate
  property_count: 6
  slug: kong-cacertificate
- name: CanaryPlugin
  property_count: 0
  slug: kong-canaryplugin
- name: CanaryPluginConfig
  property_count: 5
  slug: kong-canarypluginconfig
- name: CatalogApiServiceMappingFilterParameters
  property_count: 1
  slug: kong-catalogapiservicemappingfilterparameters
- name: CatalogIntegration
  property_count: 12
  slug: kong-catalogintegration
- name: CatalogIntegrationApiSpecProvider
  property_count: 5
  slug: kong-catalogintegrationapispecprovider
- name: CatalogIntegrationAuthorization
  property_count: 0
  slug: kong-catalogintegrationauthorization
- name: CatalogIntegrationConfigSchema
  property_count: 0
  slug: kong-catalogintegrationconfigschema
- name: CatalogIntegrationDiscovery
  property_count: 1
  slug: kong-catalogintegrationdiscovery
- name: CatalogIntegrationEvents
  property_count: 0
  slug: kong-catalogintegrationevents
- name: CatalogIntegrationFilterParameters
  property_count: 2
  slug: kong-catalogintegrationfilterparameters
- name: CatalogIntegrationResourceTypes
  property_count: 0
  slug: kong-catalogintegrationresourcetypes
- name: CatalogResource
  property_count: 10
  slug: kong-catalogresource
- name: CatalogResourceConfig
  property_count: 0
  slug: kong-catalogresourceconfig
- name: CatalogResourceConfigFieldFilter
  property_count: 5
  slug: kong-catalogresourceconfigfieldfilter
- name: CatalogResourceFilterParameters
  property_count: 14
  slug: kong-catalogresourcefilterparameters
- name: CatalogResourceId
  property_count: 0
  slug: kong-catalogresourceid
- name: CatalogResourceIntegrationDataFieldFilter
  property_count: 5
  slug: kong-catalogresourceintegrationdatafieldfilter
- name: CatalogResourceMapping
  property_count: 4
  slug: kong-catalogresourcemapping
- name: CatalogResourceMappingFilterParameters
  property_count: 13
  slug: kong-catalogresourcemappingfilterparameters
- name: CatalogResourceRef
  property_count: 5
  slug: kong-catalogresourceref
- name: CatalogResourceRefFilterParameters
  property_count: 13
  slug: kong-catalogresourcereffilterparameters
- name: CatalogResourceType
  property_count: 0
  slug: kong-catalogresourcetype
- name: CatalogService
  property_count: 8
  slug: kong-catalogservice
- name: CatalogServiceApiMapping
  property_count: 5
  slug: kong-catalogserviceapimapping
- name: CatalogServiceApiMappingFilterParameters
  property_count: 1
  slug: kong-catalogserviceapimappingfilterparameters
- name: CatalogServiceFilterParameters
  property_count: 7
  slug: kong-catalogservicefilterparameters
- name: CatalogServiceRef
  property_count: 3
  slug: kong-catalogserviceref
- name: CatalogServiceScorecard
  property_count: 9
  slug: kong-catalogservicescorecard
- name: CatalogServiceScorecardCriteria
  property_count: 11
  slug: kong-catalogservicescorecardcriteria
- name: Certificate
  property_count: 9
  slug: kong-certificate
- name: CertificateMetadata
  property_count: 10
  slug: kong-certificatemetadata
- name: Chart
  property_count: 0
  slug: kong-chart
- name: ChartTile
  property_count: 3
  slug: kong-charttile
- name: Choropleth map chart
  property_count: 2
  slug: kong-choroplethmapchart
- name: Client Credentials Application
  property_count: 13
  slug: kong-clientcredentialsapplication
- name: ClientSecretCredentialListItem
  property_count: 6
  slug: kong-clientsecretcredentiallistitem
- name: CloudGatewaysStringFieldFilterOverride
  property_count: 5
  slug: kong-cloudgatewaysstringfieldfilteroverride
- name: ConfigStore
  property_count: 4
  slug: kong-configstore
- name: ConfigStoreSecret
  property_count: 4
  slug: kong-configstoresecret
- name: Cloud Gateway Configuration Data-Plane Group
  property_count: 12
  slug: kong-configurationdataplanegroup
- name: ConfigurationDataPlaneGroupAutoscale
  property_count: 0
  slug: kong-configurationdataplanegroupautoscale
- name: Configuration Autoscale Autopilot
  property_count: 3
  slug: kong-configurationdataplanegroupautoscaleautopilot
- name: Configuration Autoscale Static
  property_count: 3
  slug: kong-configurationdataplanegroupautoscalestatic
- name: Configuration Data-Plane Group Config Item
  property_count: 5
  slug: kong-configurationdataplanegroupconfig
- name: Configuration Data-Plane Group Environment
  property_count: 0
  slug: kong-configurationdataplanegroupenvironment
- name: Configuration Data-Plane Group Environment Field
  property_count: 2
  slug: kong-configurationdataplanegroupenvironmentfield
- name: ConfigurationFilterParameters
  property_count: 4
  slug: kong-configurationfilterparameters
- name: ConfigurationId
  property_count: 0
  slug: kong-configurationid
- name: ConfigurationKind
  property_count: 0
  slug: kong-configurationkind
- name: Configuration
  property_count: 11
  slug: kong-configurationmanifest
- name: ConfigurationsFilterParameters
  property_count: 2
  slug: kong-configurationsfilterparameters
- name: ConflictError
  property_count: 0
  slug: kong-conflicterror
- name: ConfluentConsumePlugin
  property_count: 0
  slug: kong-confluentconsumeplugin
- name: ConfluentConsumePluginConfig
  property_count: 6
  slug: kong-confluentconsumepluginconfig
- name: ConfluentPlugin
  property_count: 0
  slug: kong-confluentplugin
- name: ConfluentPluginConfig
  property_count: 6
  slug: kong-confluentpluginconfig
- name: ConsumeFailureMode
  property_count: 0
  slug: kong-consumefailuremode
- name: ConsumeKeyValidationAction
  property_count: 0
  slug: kong-consumekeyvalidationaction
- name: Consumer
  property_count: 6
  slug: kong-consumer
- name: ConsumerGroup
  property_count: 5
  slug: kong-consumergroup
- name: ConsumerGroupInsideWrapper
  property_count: 1
  slug: kong-consumergroupinsidewrapper
- name: ConsumeValueValidationAction
  property_count: 0
  slug: kong-consumevaluevalidationaction
- name: ContainerSpec
  property_count: 1
  slug: kong-containerspec
- name: ControlPlane
  property_count: 7
  slug: kong-controlplane
- name: ControlPlaneAddOnOwner
  property_count: 3
  slug: kong-controlplaneaddonowner
- name: ControlPlaneFilterParameters
  property_count: 4
  slug: kong-controlplanefilterparameters
- name: Control-Plane Geo
  property_count: 0
  slug: kong-controlplanegeo
- name: ControlPlaneGeoFieldEqualsFilter
  property_count: 0
  slug: kong-controlplanegeofieldequalsfilter
- name: ControlPlaneGeoFieldFilter
  property_count: 0
  slug: kong-controlplanegeofieldfilter
- name: ControlPlaneGeoFieldNotEqualsFilter
  property_count: 1
  slug: kong-controlplanegeofieldnotequalsfilter
- name: ControlPlaneGeoFieldOrEqualityFilter
  property_count: 1
  slug: kong-controlplanegeofieldorequalityfilter
- name: ControlPlaneGroupAddOnOwner
  property_count: 3
  slug: kong-controlplanegroupaddonowner
- name: ControlPlaneId
  property_count: 0
  slug: kong-controlplaneid
- name: CorrelationIdPlugin
  property_count: 0
  slug: kong-correlationidplugin
- name: CorrelationIdPluginConfig
  property_count: 6
  slug: kong-correlationidpluginconfig
- name: CorsPlugin
  property_count: 0
  slug: kong-corsplugin
- name: CorsPluginConfig
  property_count: 5
  slug: kong-corspluginconfig
- name: CreateAddOnConfig
  property_count: 0
  slug: kong-createaddonconfig
- name: CreateAddOnRequest
  property_count: 3
  slug: kong-createaddonrequest
- name: CreateAppAuthStrategyRequest
  property_count: 0
  slug: kong-createappauthstrategyrequest
- name: CreateAppAuthStrategyResponse
  property_count: 0
  slug: kong-createappauthstrategyresponse
- name: AWS Resource Endpoint Gateway
  property_count: 3
  slug: kong-createawsresourceendpointgateway
- name: CreateAWSRoleDelegationAuthCredential
  property_count: 2
  slug: kong-createawsroledelegationauthcredential
- name: AWS Transit Gateway
  property_count: 4
  slug: kong-createawstransitgateway
- name: AWS VPC Peering Gateway
  property_count: 4
  slug: kong-createawsvpcpeeringgateway
- name: Azure Transit Gateway
  property_count: 3
  slug: kong-createazuretransitgateway
- name: Azure Virtual Hub Peering Gateway
  property_count: 3
  slug: kong-createazurevhubpeeringgateway
- name: CreateBillingProfileRequest
  property_count: 7
  slug: kong-createbillingprofilerequest
- name: CreateCatalogResourceMapping
  property_count: 2
  slug: kong-createcatalogresourcemapping
- name: CreateCatalogResourceMappingResourceByConfig
  property_count: 3
  slug: kong-createcatalogresourcemappingresourcebyconfig
- name: CreateCatalogService
  property_count: 5
  slug: kong-createcatalogservice
- name: Create Config Store Request
  property_count: 1
  slug: kong-createconfigstore
- name: CreateConfigStoreSecret
  property_count: 2
  slug: kong-createconfigstoresecret
- name: CreateConfigurationDataPlaneGroup
  property_count: 5
  slug: kong-createconfigurationdataplanegroup
- name: CreateConfigurationRequest
  property_count: 6
  slug: kong-createconfigurationrequest
- name: CreateControlPlaneRequest
  property_count: 7
  slug: kong-createcontrolplanerequest
- name: CreateCustomDomainRequest
  property_count: 4
  slug: kong-createcustomdomainrequest
- name: CreateCustomerRequest
  property_count: 8
  slug: kong-createcustomerrequest
- name: CreatedAt
  property_count: 0
  slug: kong-createdat
- name: DcrConfigAuth0InRequest
  property_count: 4
  slug: kong-createdcrconfigauth0inrequest
- name: DcrConfigAzureAdInRequest
  property_count: 2
  slug: kong-createdcrconfigazureadinrequest
- name: DcrConfigCurityInRequest
  property_count: 2
  slug: kong-createdcrconfigcurityinrequest
- name: CreateDcrConfigHttpInRequest
  property_count: 5
  slug: kong-createdcrconfighttpinrequest
- name: DcrConfigOktaInRequest
  property_count: 1
  slug: kong-createdcrconfigoktainrequest
- name: CreateDcrProviderRequest
  property_count: 0
  slug: kong-createdcrproviderrequest
- name: CreateDcrProviderRequestAuth0
  property_count: 6
  slug: kong-createdcrproviderrequestauth0
- name: CreateDcrProviderRequestAzureAd
  property_count: 6
  slug: kong-createdcrproviderrequestazuread
- name: CreateDcrProviderRequestCurity
  property_count: 6
  slug: kong-createdcrproviderrequestcurity
- name: CreateDcrProviderRequestHttp
  property_count: 6
  slug: kong-createdcrproviderrequesthttp
- name: CreateDcrProviderRequestOkta
  property_count: 6
  slug: kong-createdcrproviderrequestokta
- name: CreateDcrProviderResponse
  property_count: 0
  slug: kong-createdcrproviderresponse
- name: CreateGatewayRequest
  property_count: 4
  slug: kong-creategatewayrequest
- name: GCP VPC Peering Transit Gateway
  property_count: 3
  slug: kong-creategcpvpcpeeringtransitgateway
- name: CreateGitHubAppInstallationCredential
  property_count: 2
  slug: kong-creategithubappinstallationcredential
- name: Identity Provider
  property_count: 4
  slug: kong-createidentityprovider
- name: CreateIntegrationInstance
  property_count: 6
  slug: kong-createintegrationinstance
- name: CreateIntegrationInstanceAuthCredential
  property_count: 0
  slug: kong-createintegrationinstanceauthcredential
- name: CreateManagedCacheAddOnConfig
  property_count: 2
  slug: kong-createmanagedcacheaddonconfig
- name: CreateMCPServerRequest
  property_count: 5
  slug: kong-createmcpserverrequest
- name: CreateMeterRequest
  property_count: 9
  slug: kong-createmeterrequest
- name: CreateMultiKeyAuthCredential
  property_count: 2
  slug: kong-createmultikeyauthcredential
- name: CreateNetworkRequest
  property_count: 6
  slug: kong-createnetworkrequest
- name: CreateOAuthCredential
  property_count: 2
  slug: kong-createoauthcredential
- name: CreatePortalCustomDomainRequest
  property_count: 3
  slug: kong-createportalcustomdomainrequest
- name: CreatePortalCustomDomainSSL
  property_count: 0
  slug: kong-createportalcustomdomainssl
- name: http
  property_count: 1
  slug: kong-createportalcustomdomainsslstandard
- name: custom_certificate
  property_count: 4
  slug: kong-createportalcustomdomainsslwithcustomcertificate
- name: CreatePortalIdpTeamGroupMappingRequest
  property_count: 2
  slug: kong-createportalidpteamgroupmappingrequest
- name: CreatePortalPageRequest
  property_count: 7
  slug: kong-createportalpagerequest
- name: CreatePortalSnippetRequest
  property_count: 6
  slug: kong-createportalsnippetrequest
- name: CreatePrivateDnsRequest
  property_count: 2
  slug: kong-createprivatednsrequest
- name: CreateScorecard
  property_count: 5
  slug: kong-createscorecard
- name: CreateScorecardCriteria
  property_count: 5
  slug: kong-createscorecardcriteria
- name: CreateTransitGatewayRequest
  property_count: 0
  slug: kong-createtransitgatewayrequest
- name: CredentialListItem
  property_count: 0
  slug: kong-credentiallistitem
- name: CriteriaEvaluationErrorResult
  property_count: 2
  slug: kong-criteriaevaluationerrorresult
- name: CriteriaEvaluationRelationMap
  property_count: 3
  slug: kong-criteriaevaluationrelationmap
- name: CriteriaEvaluationRelationResult
  property_count: 3
  slug: kong-criteriaevaluationrelationresult
- name: CriteriaEvaluationResultDetails
  property_count: 2
  slug: kong-criteriaevaluationresultdetails
- name: CriteriaParameters
  property_count: 0
  slug: kong-criteriaparameters
- name: CriteriaTemplate
  property_count: 8
  slug: kong-criteriatemplate
- name: CriteriaTemplateFilterParameters
  property_count: 4
  slug: kong-criteriatemplatefilterparameters
- name: CriteriaTemplateName
  property_count: 0
  slug: kong-criteriatemplatename
- name: CriteriaTemplateSchema
  property_count: 0
  slug: kong-criteriatemplateschema
- name: CursorMeta
  property_count: 1
  slug: kong-cursormeta
- name: CursorMetaPage
  property_count: 5
  slug: kong-cursormetapage
- name: CursorMetaWithSizeAndTotal
  property_count: 3
  slug: kong-cursormetawithsizeandtotal
- name: CursorPageParameters
  property_count: 3
  slug: kong-cursorpageparameters
- name: CursorPaginatedMetaWithSizeAndTotal
  property_count: 1
  slug: kong-cursorpaginatedmetawithsizeandtotal
- name: Custom Domain
  property_count: 12
  slug: kong-customdomain
- name: CustomDomainId
  property_count: 0
  slug: kong-customdomainid
- name: CustomDomainKind
  property_count: 0
  slug: kong-customdomainkind
- name: Custom Domain Name
  property_count: 0
  slug: kong-customdomainname
- name: Custom Domain Online Property Status
  property_count: 0
  slug: kong-customdomainonlinepropertystatus
- name: Custom Domain Online Status
  property_count: 2
  slug: kong-customdomainonlinestatus
- name: CustomDomainsFilterParameters
  property_count: 4
  slug: kong-customdomainsfilterparameters
- name: Custom Domain State
  property_count: 0
  slug: kong-customdomainstate
- name: CustomDomainStateFieldEqualsFilter
  property_count: 0
  slug: kong-customdomainstatefieldequalsfilter
- name: CustomDomainStateFieldFilter
  property_count: 0
  slug: kong-customdomainstatefieldfilter
- name: CustomDomainStateFieldNotEqualsFilter
  property_count: 1
  slug: kong-customdomainstatefieldnotequalsfilter
- name: CustomDomainStateFieldOrEqualityFilter
  property_count: 1
  slug: kong-customdomainstatefieldorequalityfilter
- name: CustomerPagePaginatedResponse
  property_count: 2
  slug: kong-customerpagepaginatedresponse
- name: CustomFields
  property_count: 0
  slug: kong-customfields
- name: CustomPlugin
  property_count: 7
  slug: kong-customplugin
- name: Dashboard
  property_count: 2
  slug: kong-dashboard
- name: Dashboard Filter Parameters
  property_count: 5
  slug: kong-dashboardfilterparameters
- name: Dashboard Request
  property_count: 7
  slug: kong-dashboardresponse
- name: Dashboard Request
  property_count: 3
  slug: kong-dashboardupdaterequest
- name: DatadogPlugin
  property_count: 0
  slug: kong-datadogplugin
- name: DatadogPluginConfig
  property_count: 6
  slug: kong-datadogpluginconfig
- name: DatakitPlugin
  property_count: 0
  slug: kong-datakitplugin
- name: DatakitPluginConfig
  property_count: 7
  slug: kong-datakitpluginconfig
- name: DataPlaneClientCertificate
  property_count: 5
  slug: kong-dataplaneclientcertificate
- name: DataPlaneGroupId
  property_count: 0
  slug: kong-dataplanegroupid
- name: RFC3339 Date-Time
  property_count: 0
  slug: kong-datetime
- name: DateTimeFieldFilter
  property_count: 0
  slug: kong-datetimefieldfilter
- name: DcrBaseUrl
  property_count: 0
  slug: kong-dcrbaseurl
- name: DcrConfigAuth0InResponse
  property_count: 3
  slug: kong-dcrconfigauth0inresponse
- name: DcrConfigAzureAdInResponse
  property_count: 1
  slug: kong-dcrconfigazureadinresponse
- name: DcrConfigCurityInResponse
  property_count: 1
  slug: kong-dcrconfigcurityinresponse
- name: DcrConfigHttpInResponse
  property_count: 4
  slug: kong-dcrconfighttpinresponse
- name: DcrConfigOktaInResponse
  property_count: 0
  slug: kong-dcrconfigoktainresponse
- name: DcrConfigPropertyAllowMultipleCredentials
  property_count: 0
  slug: kong-dcrconfigpropertyallowmultiplecredentials
- name: DcrConfigPropertyApiKey
  property_count: 0
  slug: kong-dcrconfigpropertyapikey
- name: DcrConfigPropertyInitialDcrToken
  property_count: 0
  slug: kong-dcrconfigpropertydcrtoken
- name: DcrConfigPropertyDisableEventHooks
  property_count: 0
  slug: kong-dcrconfigpropertydisableeventhooks
- name: DcrConfigPropertyDisableRefreshSecret
  property_count: 0
  slug: kong-dcrconfigpropertydisablerefreshsecret
- name: DcrConfigPropertyInitialClientAudience
  property_count: 0
  slug: kong-dcrconfigpropertyinitialclientaudience
- name: DcrConfigPropertyInitialClientId
  property_count: 0
  slug: kong-dcrconfigpropertyinitialclientid
- name: DcrConfigPropertyInitialClientSecret
  property_count: 0
  slug: kong-dcrconfigpropertyinitialclientsecret
- name: DCR provider - Auth0
  property_count: 2
  slug: kong-dcrproviderauth0
- name: DCR provider - Azure AD
  property_count: 2
  slug: kong-dcrproviderazuread
- name: DcrProviderBase
  property_count: 10
  slug: kong-dcrproviderbase
- name: DCR provider - Curity
  property_count: 2
  slug: kong-dcrprovidercurity
- name: DcrProviderDisplayName
  property_count: 0
  slug: kong-dcrproviderdisplayname
- name: DCR provider - HTTP
  property_count: 2
  slug: kong-dcrproviderhttp
- name: DcrProviderName
  property_count: 0
  slug: kong-dcrprovidername
- name: DCR provider - OKTA
  property_count: 2
  slug: kong-dcrproviderokta
- name: DcrProviderResponse
  property_count: 0
  slug: kong-dcrproviderresponse
- name: DecryptionRecordPart
  property_count: 0
  slug: kong-decryptionrecordpart
- name: DefaultContent
  property_count: 2
  slug: kong-defaultcontent
- name: DefaultEmailTemplate
  property_count: 4
  slug: kong-defaultemailtemplate
- name: DefaultEmailTemplateContent
  property_count: 4
  slug: kong-defaultemailtemplatecontent
- name: Default Resource Configuration
  property_count: 8
  slug: kong-defaultresourceconfiguration
- name: DefaultResourceConfigurationId
  property_count: 0
  slug: kong-defaultresourceconfigurationid
- name: Default Resource Quota
  property_count: 8
  slug: kong-defaultresourcequota
- name: DefaultResourceQuotaId
  property_count: 0
  slug: kong-defaultresourcequotaid
- name: DefaultSubscription
  property_count: 2
  slug: kong-defaultsubscription
- name: Degraphql_route
  property_count: 7
  slug: kong-degraphql-route
- name: Degraphql_routeWithoutParents
  property_count: 7
  slug: kong-degraphql-routewithoutparents
- name: DegraphqlPlugin
  property_count: 0
  slug: kong-degraphqlplugin
- name: DegraphqlPluginConfig
  property_count: 5
  slug: kong-degraphqlpluginconfig
- name: ResourceDescription
  property_count: 0
  slug: kong-description
- name: DeveloperStatus
  property_count: 0
  slug: kong-developerstatus
- name: DNSRecord
  property_count: 3
  slug: kong-dnsrecord
- name: Donut chart
  property_count: 2
  slug: kong-donutchart
- name: EmailDelivery
  property_count: 5
  slug: kong-emaildelivery
- name: EmailDeliveryUpdatePayload
  property_count: 3
  slug: kong-emaildeliveryupdatepayload
- name: EmailDomain
  property_count: 5
  slug: kong-emaildomain
- name: EmailDomainFilterParameters
  property_count: 2
  slug: kong-emaildomainfilterparameters
- name: EmailDomainPayload
  property_count: 1
  slug: kong-emaildomainpayload
- name: EmailDomainVerification
  property_count: 3
  slug: kong-emaildomainverification
- name: EmailTemplate
  property_count: 8
  slug: kong-emailtemplate
- name: EmailTemplateContent
  property_count: 4
  slug: kong-emailtemplatecontent
- name: EmailTemplateName
  property_count: 0
  slug: kong-emailtemplatename
- name: EmailTemplateVariable
  property_count: 4
  slug: kong-emailtemplatevariable
- name: EmailTemplateVariableName
  property_count: 0
  slug: kong-emailtemplatevariablename
- name: EmailTemplateVariablesList
  property_count: 1
  slug: kong-emailtemplatevariableslist
- name: EmailVerificationStatus
  property_count: 0
  slug: kong-emailverificationstatus
- name: EncryptionFailureMode
  property_count: 0
  slug: kong-encryptionfailuremode
- name: EncryptionKey
  property_count: 0
  slug: kong-encryptionkey
- name: EncryptionKeyAWS
  property_count: 2
  slug: kong-encryptionkeyaws
- name: EncryptionKeyStatic
  property_count: 2
  slug: kong-encryptionkeystatic
- name: EncryptionKeyStaticReference
  property_count: 0
  slug: kong-encryptionkeystaticreference
- name: EncryptionKeyStaticReferenceById
  property_count: 1
  slug: kong-encryptionkeystaticreferencebyid
- name: EncryptionKeyStaticReferenceByName
  property_count: 1
  slug: kong-encryptionkeystaticreferencebyname
- name: EncryptionRecordPart
  property_count: 0
  slug: kong-encryptionrecordpart
- name: Entity Type
  property_count: 0
  slug: kong-entitytype
- name: EntityTypes
  property_count: 0
  slug: kong-entitytypes
- name: EnumConfigFieldSchema
  property_count: 7
  slug: kong-enumconfigfieldschema
- name: EventGatewayACLOperation
  property_count: 1
  slug: kong-eventgatewayacloperation
- name: EventGatewayACLPolicyConfig
  property_count: 1
  slug: kong-eventgatewayaclpolicyconfig
- name: EventGatewayACLResourceName
  property_count: 1
  slug: kong-eventgatewayaclresourcename
- name: EventGatewayACLRule
  property_count: 4
  slug: kong-eventgatewayaclrule
- name: EventGatewayACLRuleResourceNamesDynamicArray
  property_count: 0
  slug: kong-eventgatewayaclruleresourcenamesdynamicarray
- name: EventGatewayACLRuleResourceNamesStaticArray
  property_count: 0
  slug: kong-eventgatewayaclruleresourcenamesstaticarray
- name: ACL
  property_count: 7
  slug: kong-eventgatewayaclspolicy
- name: EventGatewayAWSKeySource
  property_count: 1
  slug: kong-eventgatewayawskeysource
- name: EventGatewayClusterPolicyModify
  property_count: 0
  slug: kong-eventgatewayclusterpolicymodify
- name: EventGatewayConsumePolicyCreate
  property_count: 0
  slug: kong-eventgatewayconsumepolicycreate
- name: EventGatewayConsumePolicyUpdate
  property_count: 0
  slug: kong-eventgatewayconsumepolicyupdate
- name: Schema Validation
  property_count: 7
  slug: kong-eventgatewayconsumeschemavalidationpolicy
- name: EventGatewayDataPlaneCertificate
  property_count: 7
  slug: kong-eventgatewaydataplanecertificate
- name: Decrypt
  property_count: 7
  slug: kong-eventgatewaydecryptpolicy
- name: EventGatewayDecryptPolicyConfig
  property_count: 3
  slug: kong-eventgatewaydecryptpolicyconfig
- name: EventGatewayEncryptConfig
  property_count: 3
  slug: kong-eventgatewayencryptconfig
- name: Encrypt
  property_count: 7
  slug: kong-eventgatewayencryptpolicy
- name: EventGatewayInfo
  property_count: 10
  slug: kong-eventgatewayinfo
- name: EventGatewayKeySource
  property_count: 0
  slug: kong-eventgatewaykeysource
- name: EventGatewayListener
  property_count: 8
  slug: kong-eventgatewaylistener
- name: EventGatewayListenerAddresses
  property_count: 0
  slug: kong-eventgatewaylisteneraddresses
- name: EventGatewayListenerPolicy
  property_count: 10
  slug: kong-eventgatewaylistenerpolicy
- name: EventGatewayListenerPolicyCreate
  property_count: 0
  slug: kong-eventgatewaylistenerpolicycreate
- name: EventGatewayListenerPolicyPatch
  property_count: 4
  slug: kong-eventgatewaylistenerpolicypatch
- name: EventGatewayListenerPolicyUpdate
  property_count: 0
  slug: kong-eventgatewaylistenerpolicyupdate
- name: EventGatewayListenerPort
  property_count: 0
  slug: kong-eventgatewaylistenerport
- name: EventGatewayListenerPorts
  property_count: 0
  slug: kong-eventgatewaylistenerports
- name: EventGatewayModifyHeaderAction
  property_count: 0
  slug: kong-eventgatewaymodifyheaderaction
- name: EventGatewayModifyHeaderRemoveAction
  property_count: 2
  slug: kong-eventgatewaymodifyheaderremoveaction
- name: EventGatewayModifyHeaderSetAction
  property_count: 3
  slug: kong-eventgatewaymodifyheadersetaction
- name: Modify Headers
  property_count: 7
  slug: kong-eventgatewaymodifyheaderspolicy
- name: Modify headers
  property_count: 8
  slug: kong-eventgatewaymodifyheaderspolicycreate
- name: EventGatewayNodeError
  property_count: 2
  slug: kong-eventgatewaynodeerror
- name: EventGatewayParsedRecordDecryptFieldsConfig
  property_count: 3
  slug: kong-eventgatewayparsedrecorddecryptfieldsconfig
- name: Decrypt Parsed Record Fields
  property_count: 7
  slug: kong-eventgatewayparsedrecorddecryptfieldspolicy
- name: Decrypt Parsed Record Fields
  property_count: 8
  slug: kong-eventgatewayparsedrecorddecryptfieldspolicycreate
- name: EventGatewayParsedRecordDecryptionSelector
  property_count: 1
  slug: kong-eventgatewayparsedrecorddecryptionselector
- name: EventGatewayParsedRecordEncryptFieldsConfig
  property_count: 2
  slug: kong-eventgatewayparsedrecordencryptfieldsconfig
- name: Encrypt Parsed Record
  property_count: 7
  slug: kong-eventgatewayparsedrecordencryptfieldspolicy
- name: Encrypt Parsed Record Fields
  property_count: 8
  slug: kong-eventgatewayparsedrecordencryptfieldspolicycreate
- name: EventGatewayParsedRecordEncryptionSelector
  property_count: 2
  slug: kong-eventgatewayparsedrecordencryptionselector
- name: EventGatewayPolicy
  property_count: 11
  slug: kong-eventgatewaypolicy
- name: EventGatewayPolicyPatch
  property_count: 5
  slug: kong-eventgatewaypolicypatch
- name: EventGatewayPolicyReference
  property_count: 0
  slug: kong-eventgatewaypolicyreference
- name: EventGatewayProducePolicyCreate
  property_count: 0
  slug: kong-eventgatewayproducepolicycreate
- name: EventGatewayProducePolicyUpdate
  property_count: 0
  slug: kong-eventgatewayproducepolicyupdate
- name: Schema Validation
  property_count: 7
  slug: kong-eventgatewayproduceschemavalidationpolicy
- name: EventGatewayProduceSchemaValidationPolicyConfig
  property_count: 0
  slug: kong-eventgatewayproduceschemavalidationpolicyconfig
- name: EventGatewayProduceSchemaValidationPolicyJsonConfig
  property_count: 4
  slug: kong-eventgatewayproduceschemavalidationpolicyjsonconfig
- name: EventGatewayProduceSchemaValidationPolicySchemaRegistryConfig
  property_count: 4
  slug: kong-eventgatewayproduceschemavalidationpolicyschemaregistryconfi
- name: EventGatewaySkipRecordPolicy
  property_count: 6
  slug: kong-eventgatewayskiprecordpolicy
- name: Skip Record
  property_count: 7
  slug: kong-eventgatewayskiprecordpolicycreate
- name: EventGatewayStaticKey
  property_count: 7
  slug: kong-eventgatewaystatickey
- name: EventGatewayStaticKeyCreate
  property_count: 4
  slug: kong-eventgatewaystatickeycreate
- name: EventGatewayStaticKeySource
  property_count: 1
  slug: kong-eventgatewaystatickeysource
- name: TLS Listener
  property_count: 6
  slug: kong-eventgatewaytlslistenerpolicy
- name: EventGatewayTLSListenerPolicyConfig
  property_count: 4
  slug: kong-eventgatewaytlslistenerpolicyconfig
- name: EventGatewayTLSListenerPolicyConfigSensitiveDataAware
  property_count: 4
  slug: kong-eventgatewaytlslistenerpolicyconfigsensitivedataaware
- name: EventGatewayTLSListenerSensitiveDataAwarePolicy
  property_count: 6
  slug: kong-eventgatewaytlslistenersensitivedataawarepolicy
- name: EventSubscription
  property_count: 5
  slug: kong-eventsubscription
- name: EventSubscriptionResponse
  property_count: 9
  slug: kong-eventsubscriptionresponse
- name: ExitTransformerPlugin
  property_count: 0
  slug: kong-exittransformerplugin
- name: ExitTransformerPluginConfig
  property_count: 6
  slug: kong-exittransformerpluginconfig
- name: ExpiresAt
  property_count: 0
  slug: kong-expiresat
- name: External Resource Key
  property_count: 0
  slug: kong-externalresourcekey
- name: FileLogPlugin
  property_count: 0
  slug: kong-filelogplugin
- name: FileLogPluginConfig
  property_count: 6
  slug: kong-filelogpluginconfig
- name: FilterApplications
  property_count: 3
  slug: kong-filterapplications
- name: ForbiddenError
  property_count: 0
  slug: kong-forbiddenerror
- name: ForwardProxyPlugin
  property_count: 0
  slug: kong-forwardproxyplugin
- name: ForwardProxyPluginConfig
  property_count: 6
  slug: kong-forwardproxypluginconfig
- name: ForwardToClusterByPortMappingConfig
  property_count: 5
  slug: kong-forwardtoclusterbyportmappingconfig
- name: ForwardToClusterBySNIConfig
  property_count: 4
  slug: kong-forwardtoclusterbysniconfig
- name: Forward to Virtual Cluster
  property_count: 6
  slug: kong-forwardtovirtualclusterpolicy
- name: CertificateInput
  property_count: 6
  slug: kong-gateway-admin-certificate-input
- name: CertificateList
  property_count: 3
  slug: kong-gateway-admin-certificate-list
- name: Certificate
  property_count: 9
  slug: kong-gateway-admin-certificate
- name: ConsumerInput
  property_count: 3
  slug: kong-gateway-admin-consumer-input
- name: ConsumerList
  property_count: 3
  slug: kong-gateway-admin-consumer-list
- name: Consumer
  property_count: 6
  slug: kong-gateway-admin-consumer
- name: Error
  property_count: 4
  slug: kong-gateway-admin-error
- name: Healthchecks
  property_count: 3
  slug: kong-gateway-admin-healthchecks
- name: NodeInfo
  property_count: 8
  slug: kong-gateway-admin-node-info
- name: NodeStatus
  property_count: 4
  slug: kong-gateway-admin-node-status
- name: PluginInput
  property_count: 11
  slug: kong-gateway-admin-plugin-input
- name: PluginList
  property_count: 3
  slug: kong-gateway-admin-plugin-list
- name: Plugin
  property_count: 14
  slug: kong-gateway-admin-plugin
- name: RouteInput
  property_count: 20
  slug: kong-gateway-admin-route-input
- name: RouteList
  property_count: 3
  slug: kong-gateway-admin-route-list
- name: Route
  property_count: 23
  slug: kong-gateway-admin-route
- name: ServiceInput
  property_count: 16
  slug: kong-gateway-admin-service-input
- name: ServiceList
  property_count: 3
  slug: kong-gateway-admin-service-list
- name: Service
  property_count: 19
  slug: kong-gateway-admin-service
- name: TargetInput
  property_count: 3
  slug: kong-gateway-admin-target-input
- name: TargetList
  property_count: 3
  slug: kong-gateway-admin-target-list
- name: Target
  property_count: 7
  slug: kong-gateway-admin-target
- name: UpstreamInput
  property_count: 16
  slug: kong-gateway-admin-upstream-input
- name: UpstreamList
  property_count: 3
  slug: kong-gateway-admin-upstream-list
- name: Upstream
  property_count: 19
  slug: kong-gateway-admin-upstream
- name: GatewayDescription
  property_count: 0
  slug: kong-gatewaydescription
- name: GatewayName
  property_count: 0
  slug: kong-gatewayname
- name: GatewayNode
  property_count: 7
  slug: kong-gatewaynode
- name: GatewaySecret
  property_count: 0
  slug: kong-gatewaysecret
- name: GatewaySecretReferenceOrLiteral
  property_count: 0
  slug: kong-gatewaysecretreferenceorliteral
- name: GatewayUnauthorizedError
  property_count: 2
  slug: kong-gatewayunauthorizederror
- name: Gateway Version
  property_count: 0
  slug: kong-gatewayversion
- name: GCP Private Hosted Zone Attachment Config
  property_count: 4
  slug: kong-gcpprivatehostedzoneattachmentconfig
- name: GcpPrivateHostedZoneResponse
  property_count: 8
  slug: kong-gcpprivatehostedzoneresponse
- name: GCP VPC Peering Attachment Config
  property_count: 3
  slug: kong-gcpvpcpeeringattachmentconfig
- name: GCP VPC Peering Transit Gateway
  property_count: 9
  slug: kong-gcpvpcpeeringgatewayresponse
- name: GetAppAuthStrategyResponse
  property_count: 0
  slug: kong-getappauthstrategyresponse
- name: GetApplicationRegistrationResponse
  property_count: 0
  slug: kong-getapplicationregistrationresponse
- name: GetApplicationResponse
  property_count: 0
  slug: kong-getapplicationresponse
- name: GitHubAppInstallationAuth
  property_count: 2
  slug: kong-githubappinstallationauth
- name: GitHubAppInstallationCredential
  property_count: 8
  slug: kong-githubappinstallationcredential
- name: GoneError
  property_count: 0
  slug: kong-goneerror
- name: GoogleAnalytics4Integration
  property_count: 3
  slug: kong-googleanalytics4integration
- name: GoogleAnalytics4IntegrationConfigProperties
  property_count: 2
  slug: kong-googleanalytics4integrationconfigproperties
- name: GoogleTagManagerIntegration
  property_count: 3
  slug: kong-googletagmanagerintegration
- name: GoogleTagManagerIntegrationConfigProperties
  property_count: 9
  slug: kong-googletagmanagerintegrationconfigproperties
- name: Granularity
  property_count: 0
  slug: kong-granularity
- name: GraphQLCostDecoration
  property_count: 8
  slug: kong-graphqlcostdecoration
- name: GraphQLCostDecorationWithoutParents
  property_count: 8
  slug: kong-graphqlcostdecorationwithoutparents
- name: GraphqlProxyCacheAdvancedPlugin
  property_count: 0
  slug: kong-graphqlproxycacheadvancedplugin
- name: GraphqlProxyCacheAdvancedPluginConfig
  property_count: 6
  slug: kong-graphqlproxycacheadvancedpluginconfig
- name: GraphqlRateLimitingAdvancedPlugin
  property_count: 0
  slug: kong-graphqlratelimitingadvancedplugin
- name: GraphqlRateLimitingAdvancedPluginConfig
  property_count: 6
  slug: kong-graphqlratelimitingadvancedpluginconfig
- name: Group
  property_count: 5
  slug: kong-group
- name: GroupConflict
  property_count: 3
  slug: kong-groupconflict
- name: GroupConflictResource
  property_count: 2
  slug: kong-groupconflictresource
- name: GroupMembership
  property_count: 1
  slug: kong-groupmembership
- name: GroupMemberStatus
  property_count: 1
  slug: kong-groupmemberstatus
- name: GroupRole
  property_count: 5
  slug: kong-grouprole
- name: GroupStatus
  property_count: 5
  slug: kong-groupstatus
- name: GrpcGatewayPlugin
  property_count: 0
  slug: kong-grpcgatewayplugin
- name: GrpcGatewayPluginConfig
  property_count: 6
  slug: kong-grpcgatewaypluginconfig
- name: GrpcWebPlugin
  property_count: 0
  slug: kong-grpcwebplugin
- name: GrpcWebPluginConfig
  property_count: 6
  slug: kong-grpcwebpluginconfig
- name: HasApisSelector
  property_count: 2
  slug: kong-hasapisselector
- name: HasDocsSelector
  property_count: 2
  slug: kong-hasdocsselector
- name: HasLabelKeySelector
  property_count: 2
  slug: kong-haslabelkeyselector
- name: HasRelationshipSelectorOperator
  property_count: 0
  slug: kong-hasrelationshipselectoroperator
- name: HasResourcesSelector
  property_count: 2
  slug: kong-hasresourcesselector
- name: HasSelectorParams
  property_count: 2
  slug: kong-hasselectorparams
- name: HeaderCertAuthPlugin
  property_count: 0
  slug: kong-headercertauthplugin
- name: HeaderCertAuthPluginConfig
  property_count: 5
  slug: kong-headercertauthpluginconfig
- name: HMACAuth
  property_count: 6
  slug: kong-hmacauth
- name: HmacAuthPlugin
  property_count: 0
  slug: kong-hmacauthplugin
- name: HmacAuthPluginConfig
  property_count: 5
  slug: kong-hmacauthpluginconfig
- name: HMACAuthWithoutParents
  property_count: 6
  slug: kong-hmacauthwithoutparents
- name: HttpLogPlugin
  property_count: 0
  slug: kong-httplogplugin
- name: HttpLogPluginConfig
  property_count: 6
  slug: kong-httplogpluginconfig
- name: Identity Provider
  property_count: 7
  slug: kong-identityprovider
- name: Identity Provider Enabled Property
  property_count: 0
  slug: kong-identityproviderenabled
- name: Identity Provider Login Path Property
  property_count: 0
  slug: kong-identityproviderloginpath
- name: IdentityProviderType
  property_count: 0
  slug: kong-identityprovidertype
- name: IDFieldFilter
  property_count: 3
  slug: kong-idfieldfilter
- name: IdP Configuration
  property_count: 5
  slug: kong-idp
- name: IDPMappingEnabled
  property_count: 0
  slug: kong-idpmappingenabled
- name: IdpTeamGroupMapping
  property_count: 5
  slug: kong-idpteamgroupmapping
- name: ImageDataUri
  property_count: 0
  slug: kong-imagedatauri
- name: ImageGIFDataUri
  property_count: 0
  slug: kong-imagegifdatauri
- name: ImageICODataUri
  property_count: 0
  slug: kong-imageicodatauri
- name: ImageJPGDataUri
  property_count: 0
  slug: kong-imagejpgdatauri
- name: ImagePNGDataUri
  property_count: 0
  slug: kong-imagepngdatauri
- name: ImageSVGDataUri
  property_count: 0
  slug: kong-imagesvgdatauri
- name: ImageTypeSchema
  property_count: 0
  slug: kong-imagetypeschema
- name: InjectionProtectionPlugin
  property_count: 0
  slug: kong-injectionprotectionplugin
- name: InjectionProtectionPluginConfig
  property_count: 5
  slug: kong-injectionprotectionpluginconfig
- name: Instance Type
  property_count: 4
  slug: kong-instancetype
- name: InstanceTypeName
  property_count: 0
  slug: kong-instancetypename
- name: Instance Types
  property_count: 0
  slug: kong-instancetypes
- name: IntegrationInstance
  property_count: 10
  slug: kong-integrationinstance
- name: IntegrationInstanceAuthConfig
  property_count: 0
  slug: kong-integrationinstanceauthconfig
- name: IntegrationInstanceAuthCredential
  property_count: 0
  slug: kong-integrationinstanceauthcredential
- name: IntegrationInstanceConfig
  property_count: 0
  slug: kong-integrationinstanceconfig
- name: IntegrationInstanceFilterParameters
  property_count: 8
  slug: kong-integrationinstancefilterparameters
- name: IntegrationInstanceRef
  property_count: 3
  slug: kong-integrationinstanceref
- name: IntegrationRef
  property_count: 3
  slug: kong-integrationref
- name: IntegrationRefWithoutInstance
  property_count: 2
  slug: kong-integrationrefwithoutinstance
- name: IntegrationResourceEvent
  property_count: 3
  slug: kong-integrationresourceevent
- name: IntegrationResourceEvents
  property_count: 0
  slug: kong-integrationresourceevents
- name: InvalidParameterChoiceItem
  property_count: 5
  slug: kong-invalidparameterchoiceitem
- name: InvalidParameterDependentItem
  property_count: 5
  slug: kong-invalidparameterdependentitem
- name: InvalidParameterMaximumLength
  property_count: 5
  slug: kong-invalidparametermaximumlength
- name: InvalidParameterMinimumLength
  property_count: 5
  slug: kong-invalidparameterminimumlength
- name: InvalidParameters
  property_count: 0
  slug: kong-invalidparameters
- name: InvalidParameterStandard
  property_count: 4
  slug: kong-invalidparameterstandard
- name: InvalidRules
  property_count: 0
  slug: kong-invalidrules
- name: IPEntries
  property_count: 0
  slug: kong-ipentries
- name: IPEntry
  property_count: 2
  slug: kong-ipentry
- name: IpRestrictionPlugin
  property_count: 0
  slug: kong-iprestrictionplugin
- name: IpRestrictionPluginConfig
  property_count: 7
  slug: kong-iprestrictionpluginconfig
- name: ISO 8601 Duration
  property_count: 0
  slug: kong-iso8601duration
- name: JqPlugin
  property_count: 0
  slug: kong-jqplugin
- name: JqPluginConfig
  property_count: 6
  slug: kong-jqpluginconfig
- name: JsonThreatProtectionPlugin
  property_count: 0
  slug: kong-jsonthreatprotectionplugin
- name: JsonThreatProtectionPluginConfig
  property_count: 5
  slug: kong-jsonthreatprotectionpluginconfig
- name: JweDecryptPlugin
  property_count: 0
  slug: kong-jwedecryptplugin
- name: JweDecryptPluginConfig
  property_count: 5
  slug: kong-jwedecryptpluginconfig
- name: JWT
  property_count: 8
  slug: kong-jwt
- name: JwtPlugin
  property_count: 0
  slug: kong-jwtplugin
- name: JwtPluginConfig
  property_count: 5
  slug: kong-jwtpluginconfig
- name: JwtSignerPlugin
  property_count: 0
  slug: kong-jwtsignerplugin
- name: JwtSignerPluginConfig
  property_count: 5
  slug: kong-jwtsignerpluginconfig
- name: JWTWithoutParents
  property_count: 8
  slug: kong-jwtwithoutparents
- name: KafkaConsumePlugin
  property_count: 0
  slug: kong-kafkaconsumeplugin
- name: KafkaConsumePluginConfig
  property_count: 5
  slug: kong-kafkaconsumepluginconfig
- name: KafkaLogPlugin
  property_count: 0
  slug: kong-kafkalogplugin
- name: KafkaLogPluginConfig
  property_count: 6
  slug: kong-kafkalogpluginconfig
- name: KafkaUpstreamPlugin
  property_count: 0
  slug: kong-kafkaupstreamplugin
- name: KafkaUpstreamPluginConfig
  property_count: 6
  slug: kong-kafkaupstreampluginconfig
- name: Key
  property_count: 10
  slug: kong-key
- name: KeyAuth
  property_count: 6
  slug: kong-keyauth
- name: Key Auth Application
  property_count: 10
  slug: kong-keyauthapplication
- name: KeyAuthEncPlugin
  property_count: 0
  slug: kong-keyauthencplugin
- name: KeyAuthEncPluginConfig
  property_count: 5
  slug: kong-keyauthencpluginconfig
- name: KeyAuthPlugin
  property_count: 0
  slug: kong-keyauthplugin
- name: KeyAuthPluginConfig
  property_count: 5
  slug: kong-keyauthpluginconfig
- name: KeyAuthWithoutParents
  property_count: 6
  slug: kong-keyauthwithoutparents
- name: KeySet
  property_count: 5
  slug: kong-keyset
- name: KeyWithoutParents
  property_count: 10
  slug: kong-keywithoutparents
- name: KongEntitiesResponse
  property_count: 2
  slug: kong-kongentitiesresponse
- name: KongRoute
  property_count: 5
  slug: kong-kongroute
- name: KongService
  property_count: 6
  slug: kong-kongservice
- name: KonnectCPLegacyBadRequestError
  property_count: 0
  slug: kong-konnectcplegacybadrequesterror
- name: Error
  property_count: 1
  slug: kong-konnectcplegacybaseerror
- name: KonnectCPLegacyConflictError
  property_count: 0
  slug: kong-konnectcplegacyconflicterror
- name: KonnectCPLegacyForbiddenError
  property_count: 0
  slug: kong-konnectcplegacyforbiddenerror
- name: KonnectCPLegacyNotFoundError
  property_count: 0
  slug: kong-konnectcplegacynotfounderror
- name: KonnectCPLegacyUnauthorizedError
  property_count: 0
  slug: kong-konnectcplegacyunauthorizederror
- name: Labels
  property_count: 0
  slug: kong-labels
- name: LabelsFieldFilter
  property_count: 0
  slug: kong-labelsfieldfilter
- name: LabelsUpdate
  property_count: 0
  slug: kong-labelsupdate
- name: LastUsedAt
  property_count: 0
  slug: kong-lastusedat
- name: LdapAuthAdvancedPlugin
  property_count: 0
  slug: kong-ldapauthadvancedplugin
- name: LdapAuthAdvancedPluginConfig
  property_count: 5
  slug: kong-ldapauthadvancedpluginconfig
- name: LdapAuthPlugin
  property_count: 0
  slug: kong-ldapauthplugin
- name: LdapAuthPluginConfig
  property_count: 5
  slug: kong-ldapauthpluginconfig
- name: LegacyStringFieldFilter
  property_count: 2
  slug: kong-legacystringfieldfilter
- name: ListAppAuthStrategiesResponse
  property_count: 2
  slug: kong-listappauthstrategiesresponse
- name: ListApplicationDevelopersResponse
  property_count: 2
  slug: kong-listapplicationdevelopersresponse
- name: ListApplicationRegistrationsResponse
  property_count: 2
  slug: kong-listapplicationregistrationsresponse
- name: ListApplicationsResponse
  property_count: 2
  slug: kong-listapplicationsresponse
- name: ListBasicDevelopersResponse
  property_count: 2
  slug: kong-listbasicdevelopersresponse
- name: ListCredentialsResponse
  property_count: 2
  slug: kong-listcredentialsresponse
- name: ListCursorMeta
  property_count: 0
  slug: kong-listcursormeta
- name: ListCustomerEntitlementAccessResponseData
  property_count: 1
  slug: kong-listcustomerentitlementaccessresponsedata
- name: ListCustomersParamsFilter
  property_count: 3
  slug: kong-listcustomersparamsfilter
- name: ListDcrProvidersResponse
  property_count: 2
  slug: kong-listdcrprovidersresponse
- name: ListDevelopersResponse
  property_count: 2
  slug: kong-listdevelopersresponse
- name: ListDomains
  property_count: 2
  slug: kong-listdomains
- name: ListMCPServersCPInfoResponse
  property_count: 2
  slug: kong-listmcpserverscpinforesponse
- name: ListMCPServersResponse
  property_count: 2
  slug: kong-listmcpserversresponse
- name: ListMetersParamsFilter
  property_count: 2
  slug: kong-listmetersparamsfilter
- name: ListPortalPagesResponse
  property_count: 1
  slug: kong-listportalpagesresponse
- name: ListPortalSnippetsResponse
  property_count: 2
  slug: kong-listportalsnippetsresponse
- name: ListPortalTeamsResponse
  property_count: 2
  slug: kong-listportalteamsresponse
- name: ListRolesResponse
  property_count: 1
  slug: kong-listrolesresponse
- name: LLMFilters
  property_count: 0
  slug: kong-llmfilters
- name: LLMMetrics
  property_count: 0
  slug: kong-llmmetrics
- name: LLMQuery
  property_count: 6
  slug: kong-llmquery
- name: LogglyPlugin
  property_count: 0
  slug: kong-logglyplugin
- name: LogglyPluginConfig
  property_count: 6
  slug: kong-logglypluginconfig
- name: ManagedCacheAddOnConfigResponse
  property_count: 4
  slug: kong-managedcacheaddonconfigresponse
- name: ManagedCacheAddOnDataPlaneGroup
  property_count: 6
  slug: kong-managedcacheaddondataplanegroup
- name: ManagedCacheCapacityConfig
  property_count: 0
  slug: kong-managedcachecapacityconfig
- name: MCPCapabilitiesMap
  property_count: 1
  slug: kong-mcpcapabilitiesmap
- name: MCPCapabilityRequest
  property_count: 2
  slug: kong-mcpcapabilityrequest
- name: MCPServerCodeResponse
  property_count: 1
  slug: kong-mcpservercoderesponse
- name: MCPServerCPInfo
  property_count: 0
  slug: kong-mcpservercpinfo
- name: MCPServerInfo
  property_count: 10
  slug: kong-mcpserverinfo
- name: MCPServerPodsStatus
  property_count: 3
  slug: kong-mcpserverpodsstatus
- name: MCPServerSignal
  property_count: 0
  slug: kong-mcpserversignal
- name: MCPServerSignals
  property_count: 1
  slug: kong-mcpserversignals
- name: MCPServerSignalV1
  property_count: 3
  slug: kong-mcpserversignalv1
- name: MCPServerStatusRequest
  property_count: 0
  slug: kong-mcpserverstatusrequest
- name: MCPServerStatusResponse
  property_count: 1
  slug: kong-mcpserverstatusresponse
- name: MCPServerVersionStatus
  property_count: 4
  slug: kong-mcpserverversionstatus
- name: Meter
  property_count: 13
  slug: kong-meter
- name: MeteringAndBillingPlugin
  property_count: 0
  slug: kong-meteringandbillingplugin
- name: MeteringAndBillingPluginConfig
  property_count: 6
  slug: kong-meteringandbillingpluginconfig
- name: Metering Event
  property_count: 9
  slug: kong-meteringevent
- name: MeterPagePaginatedResponse
  property_count: 2
  slug: kong-meterpagepaginatedresponse
- name: Method
  property_count: 0
  slug: kong-method
- name: Filter by a2a_context_id
  property_count: 0
  slug: kong-metricsa2acontextidfilterbyfield
- name: Filter by a2a_error
  property_count: 0
  slug: kong-metricsa2aerrorfilterbyfield
- name: Filter by a2a_method
  property_count: 0
  slug: kong-metricsa2amethodfilterbyfield
- name: Filter by a2a_task_id
  property_count: 0
  slug: kong-metricsa2ataskidfilterbyfield
- name: Absolute time range
  property_count: 4
  slug: kong-metricsabsolutetimerangedtov2
- name: Filter by ai_plugin
  property_count: 0
  slug: kong-metricsaipluginfilterbyfield
- name: Filter by ai_provider
  property_count: 0
  slug: kong-metricsaiproviderfilterbyfield
- name: Filter by ai_request_model
  property_count: 0
  slug: kong-metricsairequestmodelfilterbyfield
- name: Filter by ai_response_model
  property_count: 0
  slug: kong-metricsairesponsemodelfilterbyfield
- name: Filter by api
  property_count: 0
  slug: kong-metricsapifilterbyfield
- name: Filter by api_package
  property_count: 0
  slug: kong-metricsapipackagefilterbyfield
- name: Filter by api_product
  property_count: 0
  slug: kong-metricsapiproductfilterbyfield
- name: Filter by api_product_version
  property_count: 0
  slug: kong-metricsapiproductversionfilterbyfield
- name: Filter by application
  property_count: 0
  slug: kong-metricsapplicationfilterbyfield
- name: Filter by consumer
  property_count: 0
  slug: kong-metricsconsumerfilterbyfield
- name: Filter by control_plane
  property_count: 0
  slug: kong-metricscontrolplanefilterbyfield
- name: Filter by control_plane_group
  property_count: 0
  slug: kong-metricscontrolplanegroupfilterbyfield
- name: Filter by country_code
  property_count: 0
  slug: kong-metricscountrycodefilterbyfield
- name: Filter by data_plane_node
  property_count: 0
  slug: kong-metricsdataplanenodefilterbyfield
- name: Filter by data_plane_node_version
  property_count: 0
  slug: kong-metricsdataplanenodeversionfilterbyfield
- name: Filter by gateway_service
  property_count: 0
  slug: kong-metricsgatewayservicefilterbyfield
- name: Filter by llm_cache_status
  property_count: 0
  slug: kong-metricsllmcachestatusfilterbyfield
- name: Filter by llm_embeddings_model
  property_count: 0
  slug: kong-metricsllmembeddingsmodelfilterbyfield
- name: Filter by llm_embeddings_provider
  property_count: 0
  slug: kong-metricsllmembeddingsproviderfilterbyfield
- name: Filter by mcp_error
  property_count: 0
  slug: kong-metricsmcperrorfilterbyfield
- name: Filter by mcp_method
  property_count: 0
  slug: kong-metricsmcpmethodfilterbyfield
- name: Filter by mcp_session_id
  property_count: 0
  slug: kong-metricsmcpsessionidfilterbyfield
- name: Filter by mcp_tool_name
  property_count: 0
  slug: kong-metricsmcptoolnamefilterbyfield
- name: Filter by portal
  property_count: 0
  slug: kong-metricsportalfilterbyfield
- name: Filter by realm
  property_count: 0
  slug: kong-metricsrealmfilterbyfield
- name: Relative time range
  property_count: 3
  slug: kong-metricsrelativetimerangedtov2
- name: Filter by response_source
  property_count: 0
  slug: kong-metricsresponsesourcefilterbyfield
- name: Filter by route
  property_count: 0
  slug: kong-metricsroutefilterbyfield
- name: Filter by status_code
  property_count: 0
  slug: kong-metricsstatuscodefilterbyfield
- name: Filter by status_code_grouped
  property_count: 0
  slug: kong-metricsstatuscodegroupedfilterbyfield
- name: Filter by upstream_status_code
  property_count: 0
  slug: kong-metricsupstreamstatuscodefilterbyfield
- name: Filter by upstream_status_code_grouped
  property_count: 0
  slug: kong-metricsupstreamstatuscodegroupedfilterbyfield
- name: MinRuntimeVersion
  property_count: 0
  slug: kong-minruntimeversion
- name: MinRuntimeVersionUpdate
  property_count: 0
  slug: kong-minruntimeversionupdate
- name: MissingPermission
  property_count: 2
  slug: kong-missingpermission
- name: MockingPlugin
  property_count: 0
  slug: kong-mockingplugin
- name: MockingPluginConfig
  property_count: 6
  slug: kong-mockingpluginconfig
- name: Move document
  property_count: 2
  slug: kong-movedocumentrequestpayload
- name: MoveEventGatewayPolicy
  property_count: 1
  slug: kong-moveeventgatewaypolicy
- name: MovePage
  property_count: 2
  slug: kong-movepagerequestpayload
- name: MTLSAuth
  property_count: 6
  slug: kong-mtlsauth
- name: MtlsAuthPlugin
  property_count: 0
  slug: kong-mtlsauthplugin
- name: MtlsAuthPluginConfig
  property_count: 5
  slug: kong-mtlsauthpluginconfig
- name: MTLSAuthWithoutParents
  property_count: 6
  slug: kong-mtlsauthwithoutparents
- name: MultiKeyAuth
  property_count: 2
  slug: kong-multikeyauth
- name: MultiKeyAuthCredential
  property_count: 7
  slug: kong-multikeyauthcredential
- name: MutableCondition
  property_count: 0
  slug: kong-mutablecondition
- name: NamespaceExactAllowListItem
  property_count: 1
  slug: kong-namespaceexactallowlistitem
- name: Network
  property_count: 15
  slug: kong-network
- name: NetworkAvailabilityZones
  property_count: 0
  slug: kong-networkavailabilityzones
- name: Network CIDR Block
  property_count: 0
  slug: kong-networkcidrblock
- name: NetworkConfigurationReference
  property_count: 0
  slug: kong-networkconfigurationreference
- name: Network Create State
  property_count: 0
  slug: kong-networkcreatestate
- name: NetworkId
  property_count: 0
  slug: kong-networkid
- name: Network Name
  property_count: 0
  slug: kong-networkname
- name: Network Provider Metadata
  property_count: 2
  slug: kong-networkprovidermetadata
- name: NetworksFilterParameters
  property_count: 2
  slug: kong-networksfilterparameters
- name: Network State
  property_count: 0
  slug: kong-networkstate
- name: NetworkStateFieldFilter
  property_count: 3
  slug: kong-networkstatefieldfilter
- name: Network State Metadata
  property_count: 2
  slug: kong-networkstatemetadata
- name: NodeCompatibilityIssue
  property_count: 6
  slug: kong-nodecompatibilityissue
- name: NodeCompatibilityIssueAffectedResource
  property_count: 4
  slug: kong-nodecompatibilityissueaffectedresource
- name: NotFoundError
  property_count: 0
  slug: kong-notfounderror
- name: Notification
  property_count: 10
  slug: kong-notification
- name: NotificationChannel
  property_count: 2
  slug: kong-notificationchannel
- name: NotificationChannelType
  property_count: 0
  slug: kong-notificationchanneltype
- name: NotificationFilterParameters
  property_count: 5
  slug: kong-notificationfilterparameters
- name: NotificationNamespace
  property_count: 0
  slug: kong-notificationnamespace
- name: NotificationRegion
  property_count: 0
  slug: kong-notificationregion
- name: NotificationStatus
  property_count: 0
  slug: kong-notificationstatus
- name: NotificationUpdatePayload
  property_count: 1
  slug: kong-notificationupdatepayload
- name: NumberSelectorOperator
  property_count: 0
  slug: kong-numberselectoroperator
- name: NumericCustomField
  property_count: 0
  slug: kong-numericcustomfield
- name: NumericFieldFilter
  property_count: 0
  slug: kong-numericfieldfilter
- name: OasValidationPlugin
  property_count: 0
  slug: kong-oasvalidationplugin
- name: OasValidationPluginConfig
  property_count: 6
  slug: kong-oasvalidationpluginconfig
- name: OAuth
  property_count: 3
  slug: kong-oauth
- name: Oauth2IntrospectionPlugin
  property_count: 0
  slug: kong-oauth2introspectionplugin
- name: Oauth2IntrospectionPluginConfig
  property_count: 5
  slug: kong-oauth2introspectionpluginconfig
- name: Oauth2Plugin
  property_count: 0
  slug: kong-oauth2plugin
- name: Oauth2PluginConfig
  property_count: 5
  slug: kong-oauth2pluginconfig
- name: OAuthAuthConfig
  property_count: 4
  slug: kong-oauthauthconfig
- name: OAuthCredential
  property_count: 7
  slug: kong-oauthcredential
- name: OIDCAuthEnabled
  property_count: 0
  slug: kong-oidcauthenabled
- name: OIDC Claim Mappings
  property_count: 3
  slug: kong-oidcidentityproviderclaimmappings
- name: OIDC Identity Provider Login Client Id Property
  property_count: 0
  slug: kong-oidcidentityproviderclientid
- name: OIDC Identity Provider Login Client Secret Property
  property_count: 0
  slug: kong-oidcidentityproviderclientsecret
- name: OIDC Identity Provider Config
  property_count: 5
  slug: kong-oidcidentityproviderconfig
- name: OIDC Identity Provider Issuer Property
  property_count: 0
  slug: kong-oidcidentityproviderissuer
- name: OIDC Identity Provider Scopes Property
  property_count: 0
  slug: kong-oidcidentityproviderscopes
- name: OIDCIdpMappingEnabled
  property_count: 0
  slug: kong-oidcidpmappingenabled
- name: OpaPlugin
  property_count: 0
  slug: kong-opaplugin
- name: OpaPluginConfig
  property_count: 5
  slug: kong-opapluginconfig
- name: OpenidConnectPlugin
  property_count: 0
  slug: kong-openidconnectplugin
- name: OpenidConnectPluginConfig
  property_count: 5
  slug: kong-openidconnectpluginconfig
- name: OpentelemetryPlugin
  property_count: 0
  slug: kong-opentelemetryplugin
- name: OpentelemetryPluginConfig
  property_count: 6
  slug: kong-opentelemetrypluginconfig
- name: PageContent
  property_count: 0
  slug: kong-pagecontent
- name: PageMeta
  property_count: 3
  slug: kong-pagemeta
- name: PageSlug
  property_count: 0
  slug: kong-pageslug
- name: PageTitle
  property_count: 0
  slug: kong-pagetitle
- name: PageVisibilityStatus
  property_count: 0
  slug: kong-pagevisibilitystatus
- name: PaginatedMeta
  property_count: 1
  slug: kong-paginatedmeta
- name: PaginationNextResponse
  property_count: 0
  slug: kong-paginationnextresponse
- name: PaginationOffsetResponse
  property_count: 0
  slug: kong-paginationoffsetresponse
- name: ParentPageId
  property_count: 0
  slug: kong-parentpageid
- name: Partial
  property_count: 0
  slug: kong-partial
- name: PartialAppAuthStrategyConfigKeyAuth
  property_count: 2
  slug: kong-partialappauthstrategyconfigkeyauth
- name: PartialAppAuthStrategyConfigOpenIDConnect
  property_count: 4
  slug: kong-partialappauthstrategyconfigopenidconnect
- name: PartialEmbeddings
  property_count: 7
  slug: kong-partialembeddings
- name: PartialLink
  property_count: 3
  slug: kong-partiallink
- name: PartialModel
  property_count: 7
  slug: kong-partialmodel
- name: PartialRedisCe
  property_count: 7
  slug: kong-partialredisce
- name: PartialRedisEe
  property_count: 7
  slug: kong-partialredisee
- name: PartialVectordb
  property_count: 7
  slug: kong-partialvectordb
- name: PatchAwsPrivateDnsResolver
  property_count: 2
  slug: kong-patchawsprivatednsresolver
- name: PatchAwsResourceEndpointGateway
  property_count: 1
  slug: kong-patchawsresourceendpointgateway
- name: PatchAwsTransitGateway
  property_count: 1
  slug: kong-patchawstransitgateway
- name: PatchAzurePrivateDnsResolver
  property_count: 2
  slug: kong-patchazureprivatednsresolver
- name: PatchGatewayRequest
  property_count: 4
  slug: kong-patchgatewayrequest
- name: PatchMCPServerRequest
  property_count: 6
  slug: kong-patchmcpserverrequest
- name: PatchNetworkRequest
  property_count: 1
  slug: kong-patchnetworkrequest
- name: PatchPortalEmailConfig
  property_count: 4
  slug: kong-patchportalemailconfig
- name: PatchPrivateDnsRequest
  property_count: 0
  slug: kong-patchprivatednsrequest
- name: PatchTransitGatewayRequest
  property_count: 0
  slug: kong-patchtransitgatewayrequest
- name: PATName
  property_count: 0
  slug: kong-patname
- name: PersonalAccessToken
  property_count: 10
  slug: kong-personalaccesstoken
- name: PersonalAccessTokenCreateRequestWithExpiresAt
  property_count: 2
  slug: kong-personalaccesstokencreaterequestwithexpiresat
- name: PersonalAccessTokenCreateRequestWithTTL
  property_count: 2
  slug: kong-personalaccesstokencreaterequestwithttl
- name: PersonalAccessTokenCreateResponse
  property_count: 11
  slug: kong-personalaccesstokencreateresponse
- name: PersonalAccessTokenState
  property_count: 0
  slug: kong-personalaccesstokenstate
- name: Plugin
  property_count: 16
  slug: kong-plugin
- name: PluginBase
  property_count: 10
  slug: kong-pluginbase
- name: PluginWithoutParents
  property_count: 16
  slug: kong-pluginwithoutparents
- name: PortalAllowedIPs
  property_count: 0
  slug: kong-portalallowedips
- name: Portal API Publication Filter Parameters
  property_count: 4
  slug: kong-portalapipublicationfilterparameters
- name: PortalAssignedRoleResponse
  property_count: 5
  slug: kong-portalassignedroleresponse
- name: PortalAssignRoleRequest
  property_count: 4
  slug: kong-portalassignrolerequest
- name: PortalAuthenticationSettingsResponse
  property_count: 7
  slug: kong-portalauthenticationsettingsresponse
- name: PortalAuthenticationSettingsUpdateRequest
  property_count: 11
  slug: kong-portalauthenticationsettingsupdaterequest
- name: PortalClaimMappings
  property_count: 3
  slug: kong-portalclaimmappings
- name: PortalCreateTeamRequest
  property_count: 3
  slug: kong-portalcreateteamrequest
- name: PortalCustomDomain
  property_count: 6
  slug: kong-portalcustomdomain
- name: PortalCustomDomainCnameStatus
  property_count: 0
  slug: kong-portalcustomdomaincnamestatus
- name: PortalCustomDomainSSL
  property_count: 6
  slug: kong-portalcustomdomainssl
- name: PortalCustomDomainValidationErrors
  property_count: 0
  slug: kong-portalcustomdomainvalidationerrors
- name: PortalCustomDomainVerificationMethod
  property_count: 0
  slug: kong-portalcustomdomainverificationmethod
- name: PortalCustomDomainVerificationStatus
  property_count: 0
  slug: kong-portalcustomdomainverificationstatus
- name: PortalCustomization
  property_count: 6
  slug: kong-portalcustomization
- name: PortalDeveloper
  property_count: 6
  slug: kong-portaldeveloper
- name: PortalEmailConfig
  property_count: 7
  slug: kong-portalemailconfig
- name: PortalFilterParameters
  property_count: 12
  slug: kong-portalfilterparameters
- name: PortalFooterMenuSection
  property_count: 2
  slug: kong-portalfootermenusection
- name: PortalIdpTeamGroupMapping
  property_count: 5
  slug: kong-portalidpteamgroupmapping
- name: PortalIdpTeamGroupMappingCollectionResponse
  property_count: 2
  slug: kong-portalidpteamgroupmappingcollectionresponse
- name: PortalImageAsset
  property_count: 0
  slug: kong-portalimageassetblob
- name: PortalImageDataUri
  property_count: 0
  slug: kong-portalimagedatauri
- name: Portal Integrations
  property_count: 2
  slug: kong-portalintegrations
- name: PortalMenuItem
  property_count: 4
  slug: kong-portalmenuitem
- name: PortalPageInfo
  property_count: 10
  slug: kong-portalpageinfo
- name: PortalPageResponse
  property_count: 10
  slug: kong-portalpageresponse
- name: PortalPagesFilterParameters
  property_count: 6
  slug: kong-portalpagesfilterparameters
- name: PortalSnippetInfo
  property_count: 8
  slug: kong-portalsnippetinfo
- name: PortalSnippetResponse
  property_count: 9
  slug: kong-portalsnippetresponse
- name: PortalSnippetsFilterParameters
  property_count: 6
  slug: kong-portalsnippetsfilterparameters
- name: PortalTeamGroupMapping
  property_count: 2
  slug: kong-portalteamgroupmapping
- name: PortalTeamGroupMappingResponse
  property_count: 2
  slug: kong-portalteamgroupmappingresponse
- name: PortalTeamGroupMappingsUpdateRequest
  property_count: 1
  slug: kong-portalteamgroupmappingsupdaterequest
- name: PortalTeamResponse
  property_count: 6
  slug: kong-portalteamresponse
- name: PortalUpdateTeamRequest
  property_count: 3
  slug: kong-portalupdateteamrequest
- name: PostFunctionPlugin
  property_count: 0
  slug: kong-postfunctionplugin
- name: PostFunctionPluginConfig
  property_count: 5
  slug: kong-postfunctionpluginconfig
- name: PostPortalEmailConfig
  property_count: 4
  slug: kong-postportalemailconfig
- name: PreFunctionPlugin
  property_count: 0
  slug: kong-prefunctionplugin
- name: PreFunctionPluginConfig
  property_count: 5
  slug: kong-prefunctionpluginconfig
- name: PrivateDnsFilterParameters
  property_count: 2
  slug: kong-privatednsfilterparameters
- name: PrivateDnsId
  property_count: 0
  slug: kong-privatednsid
- name: Private DNS Name
  property_count: 0
  slug: kong-privatednsname
- name: Private DNS Resolver Config Item
  property_count: 0
  slug: kong-privatednsresolverconfig
- name: PrivateDnsResolverConfigObject
  property_count: 1
  slug: kong-privatednsresolverconfigobject
- name: PrivateDnsResponse
  property_count: 0
  slug: kong-privatednsresponse
- name: Private DNS State
  property_count: 0
  slug: kong-privatednsstate
- name: PrivateDnsStateFieldEqualsFilter
  property_count: 0
  slug: kong-privatednsstatefieldequalsfilter
- name: PrivateDnsStateFieldFilter
  property_count: 0
  slug: kong-privatednsstatefieldfilter
- name: PrivateDnsStateFieldNotEqualsFilter
  property_count: 1
  slug: kong-privatednsstatefieldnotequalsfilter
- name: PrivateDnsStateFieldOrEqualityFilter
  property_count: 1
  slug: kong-privatednsstatefieldorequalityfilter
- name: ProduceFailureMode
  property_count: 0
  slug: kong-producefailuremode
- name: ProduceKeyValidationAction
  property_count: 0
  slug: kong-producekeyvalidationaction
- name: ProduceValueValidationAction
  property_count: 0
  slug: kong-producevaluevalidationaction
- name: PrometheusPlugin
  property_count: 0
  slug: kong-prometheusplugin
- name: PrometheusPluginConfig
  property_count: 6
  slug: kong-prometheuspluginconfig
- name: Provider
  property_count: 2
  slug: kong-provider
- name: Cloud Gateway Provider Account
  property_count: 5
  slug: kong-provideraccount
- name: ProviderAccountId
  property_count: 0
  slug: kong-provideraccountid
- name: ProviderAccountsFilterParameters
  property_count: 1
  slug: kong-provideraccountsfilterparameters
- name: Provider Name
  property_count: 0
  slug: kong-providername
- name: Provider Region
  property_count: 5
  slug: kong-providerregion
- name: Provider Region ID
  property_count: 0
  slug: kong-providerregionid
- name: Provider Region Name
  property_count: 0
  slug: kong-providerregionname
- name: Provider Regions
  property_count: 0
  slug: kong-providerregions
- name: Providers
  property_count: 0
  slug: kong-providers
- name: ProxyCacheAdvancedPlugin
  property_count: 0
  slug: kong-proxycacheadvancedplugin
- name: ProxyCacheAdvancedPluginConfig
  property_count: 7
  slug: kong-proxycacheadvancedpluginconfig
- name: ProxyCachePlugin
  property_count: 0
  slug: kong-proxycacheplugin
- name: ProxyCachePluginConfig
  property_count: 7
  slug: kong-proxycachepluginconfig
- name: ProxyURL
  property_count: 3
  slug: kong-proxyurl
- name: ProxyURLs
  property_count: 0
  slug: kong-proxyurls
- name: Publication List Item
  property_count: 9
  slug: kong-publicationlistitem
- name: PublishedStatus
  property_count: 0
  slug: kong-publishedstatus
- name: RateLimitingAdvancedPlugin
  property_count: 0
  slug: kong-ratelimitingadvancedplugin
- name: RateLimitingAdvancedPluginConfig
  property_count: 7
  slug: kong-ratelimitingadvancedpluginconfig
- name: Rate Limiting configuration
  property_count: 2
  slug: kong-ratelimitingconfig
- name: RateLimitingPlugin
  property_count: 0
  slug: kong-ratelimitingplugin
- name: RateLimitingPluginConfig
  property_count: 7
  slug: kong-ratelimitingpluginconfig
- name: RBACRole
  property_count: 6
  slug: kong-rbacrole
- name: RBACRoleEndpoint
  property_count: 9
  slug: kong-rbacroleendpoint
- name: RBACRoleEntity
  property_count: 9
  slug: kong-rbacroleentity
- name: RBACUser
  property_count: 8
  slug: kong-rbacuser
- name: RBACUserGroup
  property_count: 4
  slug: kong-rbacusergroup
- name: RBACUserRole
  property_count: 4
  slug: kong-rbacuserrole
- name: RedirectPlugin
  property_count: 0
  slug: kong-redirectplugin
- name: RedirectPluginConfig
  property_count: 7
  slug: kong-redirectpluginconfig
- name: Replace Image Payload
  property_count: 1
  slug: kong-replaceimagerequestschema
- name: ReplacePortalImageAsset
  property_count: 1
  slug: kong-replaceportalimageasset
- name: RequestCalloutPlugin
  property_count: 0
  slug: kong-requestcalloutplugin
- name: RequestCalloutPluginConfig
  property_count: 7
  slug: kong-requestcalloutpluginconfig
- name: RequestsFilterType
  property_count: 0
  slug: kong-requestsfiltertype
- name: RequestsFilterTypeEmpty
  property_count: 0
  slug: kong-requestsfiltertypeempty
- name: RequestSizeLimitingPlugin
  property_count: 0
  slug: kong-requestsizelimitingplugin
- name: RequestSizeLimitingPluginConfig
  property_count: 6
  slug: kong-requestsizelimitingpluginconfig
- name: RequestTerminationPlugin
  property_count: 0
  slug: kong-requestterminationplugin
- name: RequestTerminationPluginConfig
  property_count: 7
  slug: kong-requestterminationpluginconfig
- name: RequestTransformerAdvancedPlugin
  property_count: 0
  slug: kong-requesttransformeradvancedplugin
- name: RequestTransformerAdvancedPluginConfig
  property_count: 7
  slug: kong-requesttransformeradvancedpluginconfig
- name: RequestTransformerPlugin
  property_count: 0
  slug: kong-requesttransformerplugin
- name: RequestTransformerPluginConfig
  property_count: 7
  slug: kong-requesttransformerpluginconfig
- name: RequestValidatorPlugin
  property_count: 0
  slug: kong-requestvalidatorplugin
- name: RequestValidatorPluginConfig
  property_count: 6
  slug: kong-requestvalidatorpluginconfig
- name: Resource Configuration
  property_count: 3
  slug: kong-resourceconfiguration
- name: ResourceConfigurationDescription
  property_count: 0
  slug: kong-resourceconfigurationdescription
- name: ResourceConfigurationId
  property_count: 0
  slug: kong-resourceconfigurationid
- name: ResourceConfigurationName
  property_count: 0
  slug: kong-resourceconfigurationname
- name: ResourceConfigurationQualifier
  property_count: 0
  slug: kong-resourceconfigurationqualifier
- name: ResourceConfigurationValue
  property_count: 0
  slug: kong-resourceconfigurationvalue
- name: Resource Key
  property_count: 0
  slug: kong-resourcekey
- name: Resource Quota
  property_count: 7
  slug: kong-resourcequota
- name: ResourceQuotaDescription
  property_count: 0
  slug: kong-resourcequotadescription
- name: ResourceQuotaId
  property_count: 0
  slug: kong-resourcequotaid
- name: ResourceQuotaName
  property_count: 0
  slug: kong-resourcequotaname
- name: ResourceQuotaQualifier
  property_count: 0
  slug: kong-resourcequotaqualifier
- name: ResourceQuotaValue
  property_count: 0
  slug: kong-resourcequotavalue
- name: ResponseRatelimitingPlugin
  property_count: 0
  slug: kong-responseratelimitingplugin
- name: ResponseRatelimitingPluginConfig
  property_count: 6
  slug: kong-responseratelimitingpluginconfig
- name: ResponseTransformerAdvancedPlugin
  property_count: 0
  slug: kong-responsetransformeradvancedplugin
- name: ResponseTransformerAdvancedPluginConfig
  property_count: 7
  slug: kong-responsetransformeradvancedpluginconfig
- name: ResponseTransformerPlugin
  property_count: 0
  slug: kong-responsetransformerplugin
- name: ResponseTransformerPluginConfig
  property_count: 7
  slug: kong-responsetransformerpluginconfig
- name: RevokedAt
  property_count: 0
  slug: kong-revokedat
- name: RevokedBy
  property_count: 0
  slug: kong-revokedby
- name: Kong Gateway Route
  property_count: 23
  slug: kong-route
- name: RouteByHeaderPlugin
  property_count: 0
  slug: kong-routebyheaderplugin
- name: RouteByHeaderPluginConfig
  property_count: 6
  slug: kong-routebyheaderpluginconfig
- name: RouteExpression
  property_count: 15
  slug: kong-routeexpression
- name: RouteJson
  property_count: 21
  slug: kong-routejson
- name: RouteTransformerAdvancedPlugin
  property_count: 0
  slug: kong-routetransformeradvancedplugin
- name: RouteTransformerAdvancedPluginConfig
  property_count: 6
  slug: kong-routetransformeradvancedpluginconfig
- name: RouteWithoutParents
  property_count: 0
  slug: kong-routewithoutparents
- name: SAMLAuthEnabled
  property_count: 0
  slug: kong-samlauthenabled
- name: SAML Identity Provider Config
  property_count: 6
  slug: kong-samlidentityproviderconfig
- name: SAML Identity Provider Metadata
  property_count: 0
  slug: kong-samlidentityprovidermetadata
- name: SAML Identity Provider Metadata URL
  property_count: 0
  slug: kong-samlidentityprovidermetadataurl
- name: SamlPlugin
  property_count: 0
  slug: kong-samlplugin
- name: SamlPluginConfig
  property_count: 5
  slug: kong-samlpluginconfig
- name: SchemaRegistry
  property_count: 8
  slug: kong-schemaregistry
- name: SchemaRegistryAuthenticationBasic
  property_count: 3
  slug: kong-schemaregistryauthenticationbasic
- name: SchemaRegistryAuthenticationBasicSensitiveDataAware
  property_count: 3
  slug: kong-schemaregistryauthenticationbasicsensitivedataaware
- name: SchemaRegistryAuthenticationScheme
  property_count: 0
  slug: kong-schemaregistryauthenticationscheme
- name: SchemaRegistryAuthenticationSensitiveDataAwareScheme
  property_count: 0
  slug: kong-schemaregistryauthenticationsensitivedataawarescheme
- name: SchemaRegistryConfluent
  property_count: 5
  slug: kong-schemaregistryconfluent
- name: SchemaRegistryConfluentConfig
  property_count: 4
  slug: kong-schemaregistryconfluentconfig
- name: SchemaRegistryConfluentConfigSensitiveDataAware
  property_count: 4
  slug: kong-schemaregistryconfluentconfigsensitivedataaware
- name: SchemaRegistryConfluentSensitiveDataAware
  property_count: 5
  slug: kong-schemaregistryconfluentsensitivedataaware
- name: SchemaRegistryCreate
  property_count: 0
  slug: kong-schemaregistrycreate
- name: SchemaRegistryReference
  property_count: 0
  slug: kong-schemaregistryreference
- name: SchemaRegistryReferenceById
  property_count: 1
  slug: kong-schemaregistryreferencebyid
- name: SchemaRegistryReferenceByName
  property_count: 1
  slug: kong-schemaregistryreferencebyname
- name: SchemaRegistryUpdate
  property_count: 0
  slug: kong-schemaregistryupdate
- name: SchemaValidationType
  property_count: 0
  slug: kong-schemavalidationtype
- name: ScopedUuid
  property_count: 0
  slug: kong-scopeduuid
- name: Scorecard
  property_count: 8
  slug: kong-scorecard
- name: ScorecardCriteria
  property_count: 10
  slug: kong-scorecardcriteria
- name: ScorecardCriteriaEvaluation
  property_count: 1
  slug: kong-scorecardcriteriaevaluation
- name: ScorecardCriteriaFilterParameters
  property_count: 1
  slug: kong-scorecardcriteriafilterparameters
- name: ScorecardService
  property_count: 9
  slug: kong-scorecardcriteriaservice
- name: ScorecardCriteriaServiceEvaluation
  property_count: 6
  slug: kong-scorecardcriteriaserviceevaluation
- name: ScorecardCriteriaServiceFilterParameters
  property_count: 10
  slug: kong-scorecardcriteriaservicefilterparameters
- name: ScorecardCriteriaWithEvaluation
  property_count: 11
  slug: kong-scorecardcriteriawithevaluation
- name: ScorecardEntitySelector
  property_count: 0
  slug: kong-scorecardentityselector
- name: ScorecardFilterParameters
  property_count: 3
  slug: kong-scorecardfilterparameters
- name: ScorecardScore
  property_count: 2
  slug: kong-scorecardscore
- name: ScorecardService
  property_count: 9
  slug: kong-scorecardservice
- name: ScorecardServiceFilterParameters
  property_count: 9
  slug: kong-scorecardservicefilterparameters
- name: ScorecardTemplate
  property_count: 4
  slug: kong-scorecardtemplate
- name: ScorecardTemplateCriteria
  property_count: 4
  slug: kong-scorecardtemplatecriteria
- name: ScorecardTemplateFilterParameters
  property_count: 2
  slug: kong-scorecardtemplatefilterparameters
- name: ScorecardTemplateName
  property_count: 0
  slug: kong-scorecardtemplatename
- name: ScorecardWithCriteria
  property_count: 9
  slug: kong-scorecardwithcriteria
- name: SendTestEmailTemplateContent
  property_count: 4
  slug: kong-sendtestemailtemplatecontent
- name: Serverless V1 Provider
  property_count: 2
  slug: kong-serverlessv1provider
- name: ServerlessV1ProviderName
  property_count: 0
  slug: kong-serverlessv1providername
- name: Serverless V1 Provider Region
  property_count: 1
  slug: kong-serverlessv1providerregion
- name: Serverless V1 Provider Region ID
  property_count: 0
  slug: kong-serverlessv1providerregionid
- name: Serverless V1 Provider Regions
  property_count: 0
  slug: kong-serverlessv1providerregions
- name: Serverless V1 Providers
  property_count: 0
  slug: kong-serverlessv1providers
- name: Kong Gateway Service
  property_count: 19
  slug: kong-service
- name: ServiceProtectionPlugin
  property_count: 0
  slug: kong-serviceprotectionplugin
- name: ServiceProtectionPluginConfig
  property_count: 4
  slug: kong-serviceprotectionpluginconfig
- name: ServiceSelector
  property_count: 0
  slug: kong-serviceselector
- name: SessionPlugin
  property_count: 0
  slug: kong-sessionplugin
- name: SessionPluginConfig
  property_count: 5
  slug: kong-sessionpluginconfig
- name: SimpleSchema
  property_count: 2
  slug: kong-simpleschema
- name: Single value chart
  property_count: 3
  slug: kong-singlevaluechart
- name: SNI
  property_count: 6
  slug: kong-sni
- name: SnippetContent
  property_count: 0
  slug: kong-snippetcontent
- name: SnippetName
  property_count: 0
  slug: kong-snippetname
- name: SnippetTitle
  property_count: 0
  slug: kong-snippettitle
- name: PageVisibilityStatus
  property_count: 0
  slug: kong-snippetvisibilitystatus
- name: SNIWithoutParents
  property_count: 6
  slug: kong-sniwithoutparents
- name: SolaceConsumePlugin
  property_count: 0
  slug: kong-solaceconsumeplugin
- name: SolaceConsumePluginConfig
  property_count: 5
  slug: kong-solaceconsumepluginconfig
- name: SolaceLogPlugin
  property_count: 0
  slug: kong-solacelogplugin
- name: SolaceLogPluginConfig
  property_count: 5
  slug: kong-solacelogpluginconfig
- name: SolaceUpstreamPlugin
  property_count: 0
  slug: kong-solaceupstreamplugin
- name: SolaceUpstreamPluginConfig
  property_count: 5
  slug: kong-solaceupstreampluginconfig
- name: SortQuery
  property_count: 0
  slug: kong-sortquery
- name: SourceIPEnabled
  property_count: 0
  slug: kong-sourceipenabled
- name: StandardWebhooksPlugin
  property_count: 0
  slug: kong-standardwebhooksplugin
- name: StandardWebhooksPluginConfig
  property_count: 6
  slug: kong-standardwebhookspluginconfig
- name: StatsdAdvancedPlugin
  property_count: 0
  slug: kong-statsdadvancedplugin
- name: StatsdAdvancedPluginConfig
  property_count: 6
  slug: kong-statsdadvancedpluginconfig
- name: StatsdPlugin
  property_count: 0
  slug: kong-statsdplugin
- name: StatsdPluginConfig
  property_count: 6
  slug: kong-statsdpluginconfig
- name: StringConfigFieldSchema
  property_count: 6
  slug: kong-stringconfigfieldschema
- name: StringFieldContainsFilter
  property_count: 1
  slug: kong-stringfieldcontainsfilter
- name: StringFieldEqualsFilter
  property_count: 1
  slug: kong-stringfieldequalsfilter
- name: StringFieldFilter
  property_count: 5
  slug: kong-stringfieldfilter
- name: StringFieldFilterExact
  property_count: 3
  slug: kong-stringfieldfilterexact
- name: StringFieldSelectorParams
  property_count: 2
  slug: kong-stringfieldselectorparams
- name: StringSelectorOperator
  property_count: 0
  slug: kong-stringselectoroperator
- name: SubscriptionPagePaginatedResponse
  property_count: 2
  slug: kong-subscriptionpagepaginatedresponse
- name: SyslogPlugin
  property_count: 0
  slug: kong-syslogplugin
- name: SyslogPluginConfig
  property_count: 6
  slug: kong-syslogpluginconfig
- name: System Account
  property_count: 6
  slug: kong-systemaccount
- name: System Account Access Token
  property_count: 6
  slug: kong-systemaccountaccesstoken
- name: Target
  property_count: 8
  slug: kong-target
- name: TargetWithoutParents
  property_count: 8
  slug: kong-targetwithoutparents
- name: TcpLogPlugin
  property_count: 0
  slug: kong-tcplogplugin
- name: TcpLogPluginConfig
  property_count: 6
  slug: kong-tcplogpluginconfig
- name: Team
  property_count: 7
  slug: kong-team
- name: TeamGroupMapping
  property_count: 2
  slug: kong-teamgroupmapping
- name: TeamMapping
  property_count: 2
  slug: kong-teammapping
- name: TextCustomField
  property_count: 0
  slug: kong-textcustomfield
- name: TieredCapacityConfig
  property_count: 2
  slug: kong-tieredcapacityconfig
- name: Tile
  property_count: 0
  slug: kong-tile
- name: TimeRange
  property_count: 0
  slug: kong-timerange
- name: Timeseries chart
  property_count: 3
  slug: kong-timeserieschart
- name: TimeValue
  property_count: 2
  slug: kong-timevalue
- name: TLSCertificate
  property_count: 2
  slug: kong-tlscertificate
- name: TLSCertificateSensitiveDataAware
  property_count: 2
  slug: kong-tlscertificatesensitivedataaware
- name: TlsHandshakeModifierPlugin
  property_count: 0
  slug: kong-tlshandshakemodifierplugin
- name: TlsHandshakeModifierPluginConfig
  property_count: 5
  slug: kong-tlshandshakemodifierpluginconfig
- name: TlsMetadataHeadersPlugin
  property_count: 0
  slug: kong-tlsmetadataheadersplugin
- name: TlsMetadataHeadersPluginConfig
  property_count: 5
  slug: kong-tlsmetadataheaderspluginconfig
- name: TLSTrustBundle
  property_count: 7
  slug: kong-tlstrustbundle
- name: TLSTrustBundleConfig
  property_count: 1
  slug: kong-tlstrustbundleconfig
- name: TLSTrustBundleName
  property_count: 0
  slug: kong-tlstrustbundlename
- name: TLSTrustBundleReference
  property_count: 0
  slug: kong-tlstrustbundlereference
- name: TLSTrustBundleReferenceById
  property_count: 1
  slug: kong-tlstrustbundlereferencebyid
- name: TLSTrustBundleReferenceByName
  property_count: 1
  slug: kong-tlstrustbundlereferencebyname
- name: TLSVersionRange
  property_count: 2
  slug: kong-tlsversionrange
- name: Transit Gateway CIDR Blocks
  property_count: 0
  slug: kong-transitgatewaycidrblocks
- name: Transit Gateway DNS Config
  property_count: 0
  slug: kong-transitgatewaydnsconfig
- name: TransitGatewayId
  property_count: 0
  slug: kong-transitgatewayid
- name: Transit Gateway Name
  property_count: 0
  slug: kong-transitgatewayname
- name: TransitGatewayResponse
  property_count: 0
  slug: kong-transitgatewayresponse
- name: TransitGatewaysFilterParameters
  property_count: 2
  slug: kong-transitgatewaysfilterparameters
- name: Transit Gateway State
  property_count: 0
  slug: kong-transitgatewaystate
- name: TransitGatewayStateFieldEqualsFilter
  property_count: 0
  slug: kong-transitgatewaystatefieldequalsfilter
- name: TransitGatewayStateFieldFilter
  property_count: 0
  slug: kong-transitgatewaystatefieldfilter
- name: TransitGatewayStateFieldNotEqualsFilter
  property_count: 1
  slug: kong-transitgatewaystatefieldnotequalsfilter
- name: TransitGatewayStateFieldOrEqualityFilter
  property_count: 1
  slug: kong-transitgatewaystatefieldorequalityfilter
- name: UdpLogPlugin
  property_count: 0
  slug: kong-udplogplugin
- name: UdpLogPluginConfig
  property_count: 6
  slug: kong-udplogpluginconfig
- name: ULID
  property_count: 0
  slug: kong-ulid
- name: UnauthorizedError
  property_count: 0
  slug: kong-unauthorizederror
- name: UnscopedUuid
  property_count: 0
  slug: kong-unscopeduuid
- name: UnsupportedMediaTypeError
  property_count: 0
  slug: kong-unsupportedmediatypeerror
- name: UpdateAddOnConfig
  property_count: 0
  slug: kong-updateaddonconfig
- name: UpdateAddOnRequest
  property_count: 1
  slug: kong-updateaddonrequest
- name: UpdateAppAuthStrategyRequest
  property_count: 5
  slug: kong-updateappauthstrategyrequest
- name: UpdateAppAuthStrategyRequestKeyAuth
  property_count: 1
  slug: kong-updateappauthstrategyrequestkeyauth
- name: UpdateAppAuthStrategyRequestOpenIdConnect
  property_count: 1
  slug: kong-updateappauthstrategyrequestopenidconnect
- name: UpdateAppAuthStrategyResponse
  property_count: 0
  slug: kong-updateappauthstrategyresponse
- name: UpdateApplicationRegistrationRequest
  property_count: 1
  slug: kong-updateapplicationregistrationrequest
- name: UpdateApplicationRegistrationResponse
  property_count: 0
  slug: kong-updateapplicationregistrationresponse
- name: UpdateApplicationRequest
  property_count: 1
  slug: kong-updateapplicationrequest
- name: UpdateCatalogResource
  property_count: 1
  slug: kong-updatecatalogresource
- name: UpdateCatalogService
  property_count: 5
  slug: kong-updatecatalogservice
- name: Update Config Store Request
  property_count: 1
  slug: kong-updateconfigstore
- name: UpdateConfigStoreSecret
  property_count: 1
  slug: kong-updateconfigstoresecret
- name: UpdateControlPlaneRequest
  property_count: 5
  slug: kong-updatecontrolplanerequest
- name: UpdatedAt
  property_count: 0
  slug: kong-updatedat
- name: DcrConfigAuth0InRequest
  property_count: 4
  slug: kong-updatedcrconfigauth0inrequest
- name: DcrConfigAzureAdInRequest
  property_count: 2
  slug: kong-updatedcrconfigazureadinrequest
- name: DcrConfigCurityInRequest
  property_count: 2
  slug: kong-updatedcrconfigcurityinrequest
- name: CreateDcrConfigHttpInRequest
  property_count: 5
  slug: kong-updatedcrconfighttpinrequest
- name: DcrConfigOktaInRequest
  property_count: 1
  slug: kong-updatedcrconfigoktainrequest
- name: UpdateDcrProviderRequest
  property_count: 5
  slug: kong-updatedcrproviderrequest
- name: UpdateDeveloperRequest
  property_count: 1
  slug: kong-updatedeveloperrequest
- name: UpdateGatewayRequest
  property_count: 4
  slug: kong-updategatewayrequest
- name: UpdateGoogleAnalytics4Integration
  property_count: 3
  slug: kong-updategoogleanalytics4integration
- name: UpdateGoogleTagManagerIntegration
  property_count: 3
  slug: kong-updategoogletagmanagerintegration
- name: Identity Provider
  property_count: 3
  slug: kong-updateidentityprovider
- name: UpdateIntegrationInstance
  property_count: 5
  slug: kong-updateintegrationinstance
- name: UpdateManagedCacheAddOnConfig
  property_count: 2
  slug: kong-updatemanagedcacheaddonconfig
- name: UpdateMCPServerRequest
  property_count: 5
  slug: kong-updatemcpserverrequest
- name: UpdatePortalCustomDomainRequest
  property_count: 2
  slug: kong-updateportalcustomdomainrequest
- name: UpdatePortalCustomDomainSSL
  property_count: 3
  slug: kong-updateportalcustomdomainssl
- name: Update Portal Integrations
  property_count: 2
  slug: kong-updateportalintegrations
- name: UpdatePortalPageRequest
  property_count: 7
  slug: kong-updateportalpagerequest
- name: UpdatePortalSnippetRequest
  property_count: 6
  slug: kong-updateportalsnippetrequest
- name: UpdateScorecard
  property_count: 5
  slug: kong-updatescorecard
- name: UpdateScorecardCriteria
  property_count: 6
  slug: kong-updatescorecardcriteria
- name: UpsertAppCustomerDataRequest
  property_count: 2
  slug: kong-upsertappcustomerdatarequest
- name: UpsertBillingProfileRequest
  property_count: 6
  slug: kong-upsertbillingprofilerequest
- name: UpsertCustomerBillingDataRequest
  property_count: 2
  slug: kong-upsertcustomerbillingdatarequest
- name: UpsertCustomerRequest
  property_count: 7
  slug: kong-upsertcustomerrequest
- name: UpsertIntegrationInstanceAuthConfig
  property_count: 0
  slug: kong-upsertintegrationinstanceauthconfig
- name: OAuth Config
  property_count: 5
  slug: kong-upsertoauthauthconfig
- name: Upstream
  property_count: 23
  slug: kong-upstream
- name: UpstreamOauthPlugin
  property_count: 0
  slug: kong-upstreamoauthplugin
- name: UpstreamOauthPluginConfig
  property_count: 7
  slug: kong-upstreamoauthpluginconfig
- name: UpstreamTimeoutPlugin
  property_count: 0
  slug: kong-upstreamtimeoutplugin
- name: UpstreamTimeoutPluginConfig
  property_count: 6
  slug: kong-upstreamtimeoutpluginconfig
- name: UrlCustomField
  property_count: 2
  slug: kong-urlcustomfield
- name: UsageAttributionSubjectKey
  property_count: 0
  slug: kong-usageattributionsubjectkey
- name: User
  property_count: 8
  slug: kong-user
- name: UserConfiguration
  property_count: 6
  slug: kong-userconfiguration
- name: UserId
  property_count: 0
  slug: kong-userid
- name: UUID
  property_count: 0
  slug: kong-uuid
- name: UuidFieldFilter
  property_count: 3
  slug: kong-uuidfieldfilter
- name: API Specification Validation Request Payload
  property_count: 1
  slug: kong-validateapispecrequestpayload
- name: API Specification Validation Success Response
  property_count: 1
  slug: kong-validateapispecsuccessresponse
- name: Vault
  property_count: 8
  slug: kong-vault
- name: VaultAuthPlugin
  property_count: 0
  slug: kong-vaultauthplugin
- name: VaultAuthPluginConfig
  property_count: 5
  slug: kong-vaultauthpluginconfig
- name: VerifyDcrProviderResponse
  property_count: 2
  slug: kong-verifydcrproviderresponse
- name: Version List
  property_count: 0
  slug: kong-versionlist
- name: VirtualCluster
  property_count: 12
  slug: kong-virtualcluster
- name: VirtualClusterACLMode
  property_count: 0
  slug: kong-virtualclusteraclmode
- name: VirtualClusterAuthenticationAnonymous
  property_count: 1
  slug: kong-virtualclusterauthenticationanonymous
- name: VirtualClusterAuthenticationAudience
  property_count: 1
  slug: kong-virtualclusterauthenticationaudience
- name: VirtualClusterAuthenticationClaimsMapping
  property_count: 2
  slug: kong-virtualclusterauthenticationclaimsmapping
- name: VirtualClusterAuthenticationClientCertificate
  property_count: 1
  slug: kong-virtualclusterauthenticationclientcertificate
- name: VirtualClusterAuthenticationJWKS
  property_count: 3
  slug: kong-virtualclusterauthenticationjwks
- name: VirtualClusterAuthenticationOauthBearer
  property_count: 5
  slug: kong-virtualclusterauthenticationoauthbearer
- name: VirtualClusterAuthenticationPrincipal
  property_count: 2
  slug: kong-virtualclusterauthenticationprincipal
- name: VirtualClusterAuthenticationPrincipalSensitiveDataAware
  property_count: 2
  slug: kong-virtualclusterauthenticationprincipalsensitivedataaware
- name: VirtualClusterAuthenticationSaslPlain
  property_count: 3
  slug: kong-virtualclusterauthenticationsaslplain
- name: VirtualClusterAuthenticationSaslPlainSensitiveDataAware
  property_count: 3
  slug: kong-virtualclusterauthenticationsaslplainsensitivedataaware
- name: VirtualClusterAuthenticationSaslScram
  property_count: 2
  slug: kong-virtualclusterauthenticationsaslscram
- name: VirtualClusterAuthenticationScheme
  property_count: 0
  slug: kong-virtualclusterauthenticationscheme
- name: VirtualClusterAuthenticationSchemes
  property_count: 0
  slug: kong-virtualclusterauthenticationschemes
- name: VirtualClusterAuthenticationSensitiveDataAwareScheme
  property_count: 0
  slug: kong-virtualclusterauthenticationsensitivedataawarescheme
- name: VirtualClusterAuthenticationSensitiveDataAwareSchemes
  property_count: 0
  slug: kong-virtualclusterauthenticationsensitivedataawareschemes
- name: VirtualClusterAuthenticationValidate
  property_count: 2
  slug: kong-virtualclusterauthenticationvalidate
- name: VirtualClusterDNSLabel
  property_count: 0
  slug: kong-virtualclusterdnslabel
- name: VirtualClusterName
  property_count: 0
  slug: kong-virtualclustername
- name: VirtualClusterNamespace
  property_count: 3
  slug: kong-virtualclusternamespace
- name: VirtualClusterNamespaceAdditionalProperties
  property_count: 2
  slug: kong-virtualclusternamespaceadditionalproperties
- name: VirtualClusterNamespaceIdSelector
  property_count: 0
  slug: kong-virtualclusternamespaceidselector
- name: VirtualClusterNamespaceIdSelectorExactList
  property_count: 2
  slug: kong-virtualclusternamespaceidselectorexactlist
- name: VirtualClusterNamespaceIdSelectorGlob
  property_count: 2
  slug: kong-virtualclusternamespaceidselectorglob
- name: VirtualClusterNamespaceTopicSelector
  property_count: 0
  slug: kong-virtualclusternamespacetopicselector
- name: VirtualClusterNamespaceTopicSelectorExactList
  property_count: 3
  slug: kong-virtualclusternamespacetopicselectorexactlist
- name: VirtualClusterNamespaceTopicSelectorGlob
  property_count: 3
  slug: kong-virtualclusternamespacetopicselectorglob
- name: VirtualClusterReference
  property_count: 0
  slug: kong-virtualclusterreference
- name: VirtualClusterReferenceById
  property_count: 1
  slug: kong-virtualclusterreferencebyid
- name: VirtualClusterReferenceByName
  property_count: 1
  slug: kong-virtualclusterreferencebyname
- name: VirtualClusterTopicAlias
  property_count: 4
  slug: kong-virtualclustertopicalias
- name: VirtualClusterTopicAliasConflict
  property_count: 0
  slug: kong-virtualclustertopicaliasconflict
- name: VisibilityStatus
  property_count: 0
  slug: kong-visibilitystatus
- name: WebsocketSizeLimitPlugin
  property_count: 0
  slug: kong-websocketsizelimitplugin
- name: WebsocketSizeLimitPluginConfig
  property_count: 6
  slug: kong-websocketsizelimitpluginconfig
- name: WebsocketValidatorPlugin
  property_count: 0
  slug: kong-websocketvalidatorplugin
- name: WebsocketValidatorPluginConfig
  property_count: 6
  slug: kong-websocketvalidatorpluginconfig
- name: Workspace
  property_count: 7
  slug: kong-workspace
- name: XmlThreatProtectionPlugin
  property_count: 0
  slug: kong-xmlthreatprotectionplugin
- name: XmlThreatProtectionPluginConfig
  property_count: 6
  slug: kong-xmlthreatprotectionpluginconfig
- name: ZipkinPlugin
  property_count: 0
  slug: kong-zipkinplugin
- name: ZipkinPluginConfig
  property_count: 6
  slug: kong-zipkinpluginconfig
json_structures:
- name: Kong Gateway Admin Certificate Input Structure
  property_count: 6
  slug: kong-gateway-admin-certificate-input-structure
- name: Kong Gateway Admin Certificate List Structure
  property_count: 3
  slug: kong-gateway-admin-certificate-list-structure
- name: Kong Gateway Admin Certificate Structure
  property_count: 9
  slug: kong-gateway-admin-certificate-structure
- name: Kong Gateway Admin Consumer Input Structure
  property_count: 3
  slug: kong-gateway-admin-consumer-input-structure
- name: Kong Gateway Admin Consumer List Structure
  property_count: 3
  slug: kong-gateway-admin-consumer-list-structure
- name: Kong Gateway Admin Consumer Structure
  property_count: 6
  slug: kong-gateway-admin-consumer-structure
- name: Kong Gateway Admin Error Structure
  property_count: 4
  slug: kong-gateway-admin-error-structure
- name: Kong Gateway Admin Healthchecks Structure
  property_count: 3
  slug: kong-gateway-admin-healthchecks-structure
- name: Kong Gateway Admin Node Info Structure
  property_count: 8
  slug: kong-gateway-admin-node-info-structure
- name: Kong Gateway Admin Node Status Structure
  property_count: 4
  slug: kong-gateway-admin-node-status-structure
- name: Kong Gateway Admin Plugin Input Structure
  property_count: 11
  slug: kong-gateway-admin-plugin-input-structure
- name: Kong Gateway Admin Plugin List Structure
  property_count: 3
  slug: kong-gateway-admin-plugin-list-structure
- name: Kong Gateway Admin Plugin Structure
  property_count: 14
  slug: kong-gateway-admin-plugin-structure
- name: Kong Gateway Admin Route Input Structure
  property_count: 20
  slug: kong-gateway-admin-route-input-structure
- name: Kong Gateway Admin Route List Structure
  property_count: 3
  slug: kong-gateway-admin-route-list-structure
- name: Kong Gateway Admin Route Structure
  property_count: 23
  slug: kong-gateway-admin-route-structure
- name: Kong Gateway Admin Service Input Structure
  property_count: 16
  slug: kong-gateway-admin-service-input-structure
- name: Kong Gateway Admin Service List Structure
  property_count: 3
  slug: kong-gateway-admin-service-list-structure
- name: Kong Gateway Admin Service Structure
  property_count: 19
  slug: kong-gateway-admin-service-structure
- name: Kong Gateway Admin Target Input Structure
  property_count: 3
  slug: kong-gateway-admin-target-input-structure
- name: Kong Gateway Admin Target List Structure
  property_count: 3
  slug: kong-gateway-admin-target-list-structure
- name: Kong Gateway Admin Target Structure
  property_count: 7
  slug: kong-gateway-admin-target-structure
- name: Kong Gateway Admin Upstream Input Structure
  property_count: 16
  slug: kong-gateway-admin-upstream-input-structure
- name: Kong Gateway Admin Upstream List Structure
  property_count: 3
  slug: kong-gateway-admin-upstream-list-structure
- name: Kong Gateway Admin Upstream Structure
  property_count: 19
  slug: kong-gateway-admin-upstream-structure
- name: Kong Structure
  property_count: 0
  slug: kong-structure
jsonld:
- class_count: 2
  name: Kong Context
  property_count: 7
  slug: kong-context
- class_count: 0
  name: Kong Gateway Admin Context
  property_count: 0
  slug: kong-gateway-admin-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Kong
nav: Providers
network: true
overview: 'Kong publishes 132 APIs on the [APIs.io](https://apis.io/) network, including ACLs API, Add-Ons API, API API, and 129 more. Tagged areas include API Gateway, AI Gateway, AI Connectivity, Agent Gateway, and Event Gateway.


  The Kong catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Kong''s developer surface includes authentication, documentation, getting-started guide, engineering blog, changelog, CLI, support, and 16 more developer resources.'
plans:
- name: Kong Plans Pricing
  plan_count: 6
  slug: kong-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 10
  name: Kong Rate Limits
  slug: kong-rate-limits
rules:
- name: Kong API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: kong-jsonschema-spectral-rules
- name: Kong API Rules
  rule_count: 17
  severity_counts:
    error: 7
    hint: 0
    info: 2
    warn: 8
  slug: kong-spectral-rules
score:
  band: strong
  composite: 58.7
  delta: -4.7
  facets:
    commercial_clarity: 50.0
    contract_quality: 65.4
    developer_ergonomics: 63.0
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 63.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 132
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kong/refs/heads/main/screenshots/kong-2026-06-20T184130.png
security:
- kind: authentication
  name: Kong Authentication
  slug: kong-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Kong Domain Security
  slug: kong-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: kong
tags:
- API Gateway
- AI Gateway
- AI Connectivity
- Agent Gateway
- Event Gateway
- MCP Registry
- Service Mesh
- LLM
- Kafka
- Konnect
- Open Source
use_cases:
- description: Route, secure, and observe traffic to microservices with authentication, rate limiting, and request transformations.
  name: API Gateway for Microservices
- description: Manage APIs across hybrid and multi-cloud environments with centralized control through Kong Konnect.
  name: Multi-Cloud API Management
- description: Implement zero-trust security with mTLS, OAuth2, JWT validation, and API key authentication at the gateway layer.
  name: Zero-Trust Security
- description: Govern LLM, MCP, and agent-to-agent traffic with prompt firewalls, semantic caching, token budgets, and per-agent cost allocation.
  name: AI and Agent Connectivity
- description: Apply per-topic identity-aware policies and quotas to Kafka traffic without rebuilding producers and consumers.
  name: Kafka Governance at Scale
- description: Manage the full API lifecycle from design with Insomnia to deployment, monetization, and monitoring with Kong Konnect.
  name: API Lifecycle Management
- description: Protect backend services with configurable rate limiting, request size limits, and traffic shaping policies.
  name: Rate Limiting and Traffic Control
---
