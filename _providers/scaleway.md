---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 257
  human_in_the_loop: 10
  name: Scaleway Agentic Access
  operation_count: 419
  slug: scaleway-agentic-access
  summary_line: 419 operations · 257 acting · 10 human-in-the-loop
api_count: 74
apis:
- description: Scaleway Generative APIs provide access to AI language models and generative AI services hosted on Scaleway's European cloud infrastructure. Compatible with the OpenAI API format for easy integration.
  name: Scaleway Generative APIs
  slug: scaleway-generative-apis
- description: Network Access Control Lists (ACLs) allow you to manage inbound network traffic by setting up ACL rules
  name: Scaleway Access Control List API
  slug: scaleway-access-control-list-api
- description: Network Access Control Lists allow you to control incoming network traffic by setting up ACL rules.
  name: Scaleway ACLs API
  slug: scaleway-acls-api
- description: The Alert Subscribers object. It represents a subscription to alerts about Scaleway incidents impacting a given Load Balancer. Use this endpoint to create subscribers (email addresses or webhooks), su
  name: Scaleway Alert Subscribers API
  slug: scaleway-alert-subscribers-api
- description: An API key is a unique identifier, used to authenticate requests made to the Scaleway API. An API key consists of an access key and a secret key. The access key is like a unique ID or username, and no
  name: Scaleway API Keys API
  slug: scaleway-api-keys-api
- description: 'An application (also known as an IAM application) is a non-human user in a Scaleway Organization. IAM applications may be used when you want to create an API key that is not linked to a user, to give '
  name: Scaleway Applications API
  slug: scaleway-applications-api
- description: The Load Balancer backend object. It represents a set of backend servers that the frontend forwards requests to using the specified configuration (port, protocol, proxy protocol etc). You can create m
  name: Scaleway Backends API
  slug: scaleway-backends-api
- description: A database backup is a dated export of a Database Instance stored on an offsite backend located in a different region than your database, by default. Once a backup is created, it can be used to restor
  name: Scaleway Backups API
  slug: scaleway-backups-api
- description: This section allows you to manage the blocklist of your emails.
  name: Scaleway Blocklist API
  slug: scaleway-blocklist-api
- description: The Load Balancer certificate object. It represents an SSL/TLS certificate for your Load Balancer which can be used by a frontend to establish secure, encrypted connections for incoming traffic. Use t
  name: Scaleway Certificate API
  slug: scaleway-certificate-api
- description: All cluster types available in a specified region A cluster type represents the different commercial types of clusters offered by Scaleway.
  name: Scaleway Cluster types API
  slug: scaleway-cluster-types-api
- description: A cluster is a fully managed Kubernetes cluster It is composed of different pools, each pool containing the same kind of nodes.
  name: Scaleway Clusters API
  slug: scaleway-clusters-api
- description: A container is a web application, packaged as an OCI image, that runs inside Scaleway infrastructure and scales automatically. A container can be composed of multiple instances, depending on the scali
  name: Scaleway Containers API
  slug: scaleway-containers-api
- description: Crons allow you to schedule the execution of functions
  name: Scaleway Crons API
  slug: scaleway-crons-api
- description: 'A Database Instance is made up of one or multiple dedicated compute nodes running a single database engine. Two node settings are available: **High-Availability (HA)**, with a main node and one replic'
  name: Scaleway Database Instances API
  slug: scaleway-database-instances-api
- description: Databases can be used to store and manage sets of structured information, or data. The interaction between the user and a database is done using a Database Engine, which provides a structured query la
  name: Scaleway Databases API
  slug: scaleway-databases-api
- description: A container is provided with an automatically generated domain through which it is accessible. Alternatively, custom domains can be assigned to containers in order to facilitate their use.
  name: Scaleway Domains API
  slug: scaleway-domains-api
- description: This section lists your emails and shows you how to manage them.
  name: Scaleway Emails API
  slug: scaleway-emails-api
- description: A point of connection to a Database Instance. The endpoint is associated with an IPv4 address and a port. It contains the information about whether the endpoint is read-write or not. The endpoints alw
  name: Scaleway Endpoints API
  slug: scaleway-endpoints-api
- description: A database engine is the software component that stores and retrieves your data from a database. Currently PostgreSQL 11, 12, 13 and 14 are available. MySQL is available in version 8.
  name: Scaleway Engines API
  slug: scaleway-engines-api
- description: The Load Balancer frontend object. It listens on a configured port and forward requests to one or several backends. You can create multiple frontends for any given Load Balancer, each listening on a d
  name: Scaleway Frontends API
  slug: scaleway-frontends-api
- description: A function defines a procedure on how to change one element into another. The function remains static, while the variables that pass through it can vary.
  name: Scaleway Functions API
  slug: scaleway-functions-api
- description: A group (also known as an IAM group) is a grouping of [users](https://www.scaleway.com/en/docs/iam/concepts/#user) and/or [applications](https://www.scaleway.com/en/docs/iam/concepts/#application). Cr
  name: Scaleway Groups API
  slug: scaleway-groups-api
- description: The Iam API from Scaleway — 8 operation(s) for iam.
  name: Scaleway Iam API
  slug: scaleway-iam-api
- description: Images are backups of your Instances. One image will contain all the volumes of your Instance and can be used to restore your Instance and its data. You can also use it to create a series of Instances
  name: Scaleway Images API
  slug: scaleway-images-api
- description: The Instance API from Scaleway — 2 operation(s) for instance.
  name: Scaleway Instance API
  slug: scaleway-instance-api
- description: Advanced Database Instance settings allow you to tune the behavior of your database engines to better fit your needs. Available settings depend on the database engine and its version. Note that some s
  name: Scaleway Instance Settings API
  slug: scaleway-instance-settings-api
- description: All Instance types available in a specified zone. Each type contains all the features of the Instance (CPU, RAM, Storage) as well as their associated pricing.
  name: Scaleway Instance Types API
  slug: scaleway-instance-types-api
- description: 'Instances are computing units providing resources to run your applications on. Scaleway offers various Instance types including **Virtual Instances** and **dedicated GPU Instances**. **Note: Instances'
  name: Scaleway Instances API
  slug: scaleway-instances-api
- description: The Load Balancer IP address object. It represents a flexible IP address which can be attached to a Load Balancer. Use this endpoint to create, list, get, update and delete your Load Balancer IP addre
  name: Scaleway IP addresses API
  slug: scaleway-ip-addresses-api
- description: A flexible IP address is an IP address which you hold independently of any Instance. You can attach it to any of your Instances and do live migration of the IP address between your Instances. Note tha
  name: Scaleway IPs API
  slug: scaleway-ips-api
- description: The JWTs API from Scaleway — 2 operation(s) for jwts.
  name: Scaleway JWTs API
  slug: scaleway-jwts-api
- description: The main Load Balancer object. A Scaleway Load Balancer is a representation of a fully-managed, highly-available Instance configured to direct traffic across multiple servers. Use the Load Balancer en
  name: Scaleway Load Balancer API
  slug: scaleway-load-balancer-api
- description: The Load Balancer offer type object. It represents the different commercial types of Load Balancer offered by Scaleway, each with different specifications and pricing. Use this endpoint to list all Lo
  name: Scaleway Load Balancer Types API
  slug: scaleway-load-balancer-types-api
- description: Logs provide a record of all events and errors that take place during the lifecycle of your IAM resources (IAM users, applications, groups, API keys, and policies). Logs represent a source of visibili
  name: Scaleway Logs API
  slug: scaleway-logs-api
- description: A namespace is a logical concept that allows you to group your containers. Containers in the same namespace can share environment variables, defined only once, at the namespace level.
  name: Scaleway Namespaces API
  slug: scaleway-namespaces-api
- description: 'A Network **A**ccess **C**ontrol **L**ist (ACL) is a set of stateless, IP-based rules used to filter packets between Private Networks in a VPC. Each VPC can have a maximum of two Network ACLs: one for'
  name: Scaleway Network ACLs API
  slug: scaleway-network-acls-api
- description: A node (short for worker node) is an abstraction for a Scaleway Instance A node is always part of a pool. Each of them has the Kubernetes software automatically installed and configured by Scaleway.
  name: Scaleway Nodes API
  slug: scaleway-nodes-api
- description: 'Two node type ranges are available: * **General Purpose:** production-grade nodes designed for scalable database infrastructures. * **Development:** sandbox environments and reliable performance for d'
  name: Scaleway NodeTypes API
  slug: scaleway-nodetypes-api
- description: This section allows you to manage and get get subscribed information about your project email offer.
  name: Scaleway offers API
  slug: scaleway-offers-api
- description: Permission sets are the main components of [IAM rules](https://www.scaleway.com/en/docs/iam/concepts/#rule). They consist of sets of one or multiple [permissions](https://www.scaleway.com/en/docs/iam/
  name: Scaleway Permission sets API
  slug: scaleway-permission-sets-api
- description: Placement groups allow the user to express a preference regarding the physical position of a group of Instances. The feature lets the user choose to either group Instances on the same physical hardwar
  name: Scaleway Placement Groups API
  slug: scaleway-placement-groups-api
- description: Policies control user rights, by defining one or more rules to apply to the attached principals (users, groups or applications). A policy rule has two parts:\ permission set and scope. For each policy
  name: Scaleway Policies API
  slug: scaleway-policies-api
- description: A pool is a set of identical nodes A pool has a name, a size (its desired number of nodes), node number limits (min, max), and a Scaleway Instance type. Changing those limits increases/decreases the s
  name: Scaleway Pools API
  slug: scaleway-pools-api
- description: 'The Private Network object. It represents Scaleway Private Networks which can be attached to/detached from a Load Balancer. Use this endpoint to list the Private Networks attached to a Load Balancer, '
  name: Scaleway Private Networks API
  slug: scaleway-private-networks-api
- description: A Private NIC is the network interface that connects an Instance to a Private Network. An Instance can have multiple private NICs at the same time, but each NIC must belong to a different Private Netw
  name: Scaleway Private NICs API
  slug: scaleway-private-nics-api
- description: Privileges are permissions that can be granted to database users. You can manage user permissions either via the console, the Scaleway APIs or SQL. Managed Database for PostgreSQL and MySQL provides a
  name: Scaleway Privileges API
  slug: scaleway-privileges-api
- description: Project consumption allow you to see your project consumption.
  name: Scaleway Project Consumption API
  slug: scaleway-project-consumption-api
- description: Project settings allow you to manage the configuration of your projects.
  name: Scaleway Project Settings API
  slug: scaleway-project-settings-api
- description: Every Scaleway Organization detains a certain number of resource quotas, which are limits on the number of Scaleway resources these Organizations can use.
  name: Scaleway Quotas API
  slug: scaleway-quotas-api
- description: A Read Replica is a live copy of a Database Instance that behaves like an Instance, but that only allows read-only connections. The replica mirrors the data of the primary Database node and any change
  name: Scaleway Read Replicas API
  slug: scaleway-read-replicas-api
- description: The Load Balancer route object. It represents a configuration on a particular frontend to direct traffic to a particular backend if certain conditions are fulfilled. Conditions must be based on SNI fo
  name: Scaleway Route API
  slug: scaleway-route-api
- description: Custom routes that will be pushed to your private networks resources.
  name: Scaleway Routes API
  slug: scaleway-routes-api
- description: A rule (also known as an IAM rule) is the part of a [policy](https://www.scaleway.com/en/docs/iam/concepts/#policy) that defines the permissions of the policy's [principal](https://www.scaleway.com/en
  name: Scaleway Rules API
  slug: scaleway-rules-api
- description: Scaleway supports Identity Federation to provide your teams with secure access to their accounts via Single Sign-On (SSO). Depending on your organization's requirements, you can use either built-in OA
  name: Scaleway SAML API
  slug: scaleway-saml-api
- description: Versions store the sensitive data contained in your secrets (API keys, passwords, or certificates)
  name: Scaleway Secret Versions API
  slug: scaleway-secret-versions-api
- description: Secrets are logical containers made up of zero or more immutable versions, that contain sensitive data
  name: Scaleway Secrets API
  slug: scaleway-secrets-api
- description: 'A security group is a set of firewall rules on a set of Instances. Security groups enable you to create rules that either drop or allow incoming traffic from certain ports of your Instances. Security '
  name: Scaleway Security Groups API
  slug: scaleway-security-groups-api
- description: Security settings are organization-wide configurations that apply to all users in an organization. These settings enforce restrictions on how users authenticate with Scaleway's services.
  name: Scaleway Security Settings API
  slug: scaleway-security-settings-api
- description: A snapshot is a consistent, instantaneous copy of the Block Storage volume of your Database Instance at a certain point in time. They are designed to recover your data in case of failure or accidental
  name: Scaleway Snapshots API
  slug: scaleway-snapshots-api
- description: An SSH Key (**S**ecure **Sh**ell Key) allows passwordless connection to an [Instance](https://www.scaleway.com/en/docs/instances/concepts/#instance). An SSH Key is [generated by creating an RSA key pa
  name: Scaleway SSH Keys API
  slug: scaleway-ssh-keys-api
- description: This section gives you information about your emails' statuses.
  name: Scaleway Statistics API
  slug: scaleway-statistics-api
- description: Load balancer statistics (deprecated).
  name: Scaleway Stats API
  slug: scaleway-stats-api
- description: CIDR subnet management for your Private Networks.
  name: Scaleway Subnets API
  slug: scaleway-subnets-api
- description: Tokens allow you to manage access control to your function.
  name: Scaleway Tokens API
  slug: scaleway-tokens-api
- description: A trigger is a way to invoke a container based on specific events, such as a periodic schedule or a message arriving in a queue. When the event occurs, the trigger invokes the container, passing relev
  name: Scaleway Triggers API
  slug: scaleway-triggers-api
- description: User data is a key/value store you can use to provide your instance with introspective data. As an example of use, Scaleway images contain the `scw-generate-ssh-keys` script, which generates the SSH s
  name: Scaleway User Data API
  slug: scaleway-user-data-api
- description: Users are profiles to which you can attribute database-level permissions. They allow you to define permissions specific to each type of database usage. For example, users with an `admin` role can crea
  name: Scaleway Users API
  slug: scaleway-users-api
- description: A version is a vanilla Kubernetes version like `x.y.z` It comprises a major version `x`, a minor version `y`, and a patch version `z`. At the minimum, Kapsule (Scaleway's managed Kubernetes), will sup
  name: Scaleway Versions API
  slug: scaleway-versions-api
- description: All volume types available in a specified zone. Each of these types will contains all the capabilities and constraints of the volume (min size, max size, snapshot).
  name: Scaleway Volume Types API
  slug: scaleway-volume-types-api
- description: A volume is where you store your data inside your Instance. It appears as a block device on Linux that you can use to create a filesystem and mount it. The Instance API only supports local (`l_ssd`) a
  name: Scaleway Volumes API
  slug: scaleway-volumes-api
- description: A VPC peering connector constitutes one side of a VPC peering connection. It represents an intent to peer with another VPC. Two matching, compatible VPC connectors create a VPC peering connection.
  name: Scaleway VPC Connectors API
  slug: scaleway-vpc-connectors-api
- description: A Virtual Private Cloud (VPC) allows you to group your regional Private Networks together. Note that a Private Network can be a part of only one VPC.
  name: Scaleway VPCs API
  slug: scaleway-vpcs-api
- description: Webhooks enable real-time communication and automation between systems by sending messages through all protocols supported by SNS, such as HTTP, HTTPS, and Serverless Functions, allowing for immediate
  name: Scaleway Webhooks API
  slug: scaleway-webhooks-api
artifact_total: 515
collections:
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List API
  slug: postman-scaleway-access-control-list-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List ACLs API
  slug: postman-scaleway-acls-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Alert Subscribers API
  slug: postman-scaleway-alert-subscribers-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List API Keys API
  slug: postman-scaleway-api-keys-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Applications API
  slug: postman-scaleway-applications-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Backends API
  slug: postman-scaleway-backends-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Backups API
  slug: postman-scaleway-backups-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Blocklist API
  slug: postman-scaleway-blocklist-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Certificate API
  slug: postman-scaleway-certificate-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Cluster types API
  slug: postman-scaleway-cluster-types-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Clusters API
  slug: postman-scaleway-clusters-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Containers API
  slug: postman-scaleway-containers-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Crons API
  slug: postman-scaleway-crons-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Database Instances API
  slug: postman-scaleway-database-instances-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Databases API
  slug: postman-scaleway-databases-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Domains API
  slug: postman-scaleway-domains-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Emails API
  slug: postman-scaleway-emails-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Endpoints API
  slug: postman-scaleway-endpoints-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Engines API
  slug: postman-scaleway-engines-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Frontends API
  slug: postman-scaleway-frontends-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Functions API
  slug: postman-scaleway-functions-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Groups API
  slug: postman-scaleway-groups-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Iam API
  slug: postman-scaleway-iam-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Images API
  slug: postman-scaleway-images-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Instance API
  slug: postman-scaleway-instance-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Instance Settings API
  slug: postman-scaleway-instance-settings-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Instance Types API
  slug: postman-scaleway-instance-types-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Instances API
  slug: postman-scaleway-instances-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List IP addresses API
  slug: postman-scaleway-ip-addresses-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List IPs API
  slug: postman-scaleway-ips-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List JWTs API
  slug: postman-scaleway-jwts-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Load Balancer API
  slug: postman-scaleway-load-balancer-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Load Balancer Types API
  slug: postman-scaleway-load-balancer-types-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Logs API
  slug: postman-scaleway-logs-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Namespaces API
  slug: postman-scaleway-namespaces-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Network ACLs API
  slug: postman-scaleway-network-acls-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Nodes API
  slug: postman-scaleway-nodes-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List NodeTypes API
  slug: postman-scaleway-nodetypes-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List offers API
  slug: postman-scaleway-offers-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Permission sets API
  slug: postman-scaleway-permission-sets-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Placement Groups API
  slug: postman-scaleway-placement-groups-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Policies API
  slug: postman-scaleway-policies-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Pools API
  slug: postman-scaleway-pools-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Private Networks API
  slug: postman-scaleway-private-networks-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Private NICs API
  slug: postman-scaleway-private-nics-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Privileges API
  slug: postman-scaleway-privileges-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Project Consumption API
  slug: postman-scaleway-project-consumption-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Project Settings API
  slug: postman-scaleway-project-settings-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Quotas API
  slug: postman-scaleway-quotas-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Read Replicas API
  slug: postman-scaleway-read-replicas-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Route API
  slug: postman-scaleway-route-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Routes API
  slug: postman-scaleway-routes-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Rules API
  slug: postman-scaleway-rules-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List SAML API
  slug: postman-scaleway-saml-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Secret Versions API
  slug: postman-scaleway-secret-versions-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Secrets API
  slug: postman-scaleway-secrets-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Security Groups API
  slug: postman-scaleway-security-groups-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Security Settings API
  slug: postman-scaleway-security-settings-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Snapshots API
  slug: postman-scaleway-snapshots-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List SSH Keys API
  slug: postman-scaleway-ssh-keys-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Statistics API
  slug: postman-scaleway-statistics-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Stats API
  slug: postman-scaleway-stats-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Subnets API
  slug: postman-scaleway-subnets-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Tokens API
  slug: postman-scaleway-tokens-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Triggers API
  slug: postman-scaleway-triggers-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List User Data API
  slug: postman-scaleway-user-data-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Users API
  slug: postman-scaleway-users-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Versions API
  slug: postman-scaleway-versions-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Volume Types API
  slug: postman-scaleway-volume-types-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Volumes API
  slug: postman-scaleway-volumes-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List VPC Connectors API
  slug: postman-scaleway-vpc-connectors-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List VPCs API
  slug: postman-scaleway-vpcs-api
- collection_type: postman
  name: Managed Database for PostgreSQL and MySQL Access Control List Webhooks API
  slug: postman-scaleway-webhooks-api
- collection_type: open
  name: Managed Database for PostgreSQL and MySQL API
  slug: open-scaleway-database
- collection_type: open
  name: IAM API
  slug: open-scaleway-iam
- collection_type: open
  name: Instance API
  slug: open-scaleway-instance
- collection_type: open
  name: Kubernetes API
  slug: open-scaleway-kubernetes
- collection_type: open
  name: Load Balancer API
  slug: open-scaleway-load-balancer
- collection_type: open
  name: Secret Manager API
  slug: open-scaleway-secret-manager
- collection_type: open
  name: Serverless Containers API
  slug: open-scaleway-serverless-containers
- collection_type: open
  name: Serverless Functions API
  slug: open-scaleway-serverless-functions
- collection_type: open
  name: Transactional Email API
  slug: open-scaleway-transactional-email
- collection_type: open
  name: VPC API
  slug: open-scaleway-vpc
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/scaleway/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/scaleway-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/scaleway-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/scaleway-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scaleway-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/scaleway-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/scaleway
- group: start
  title: ''
  type: Portal
  url: https://www.scaleway.com/en/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://www.scaleway.com/en/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.scaleway.com/en/developers/api/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/scaleway
- group: build
  title: ''
  type: SDKs
  url: https://github.com/scaleway/scaleway-sdk-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/scaleway/scaleway-sdk-js
- group: build
  title: ''
  type: SDKs
  url: https://github.com/scaleway/scaleway-sdk-python
- group: build
  title: ''
  type: CLI
  url: https://github.com/scaleway/scaleway-cli
- group: other
  title: ''
  type: Terraform Provider
  url: https://github.com/scaleway/terraform-provider-scaleway
- group: build
  title: ''
  type: Postman
  url: https://www.scaleway.com/en/docs/tutorials/postman-api/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.scaleway.com/en/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.scaleway.com/
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/scaleway/refs/heads/main/vocabulary/scaleway-vocabulary.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/scaleway/refs/heads/main/json-schema/scaleway-instance-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/scaleway/refs/heads/main/json-schema/scaleway-cluster-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/scaleway/refs/heads/main/json-schema/scaleway-secret-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/scaleway/refs/heads/main/json-ld/scaleway-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/scaleway/refs/heads/main/rules/scaleway-rules.yml
- group: company
  title: ''
  type: Blog
  url: https://www.scaleway.com/en/blog/rss.xml
created: '2026-05-02'
description: Scaleway is a European cloud provider offering a full suite of compute, storage, networking, AI, and serverless infrastructure services. Scaleway provides a comprehensive REST API for programmatic management of all cloud resources including Instances, Kubernetes clusters (Kapsule and Kosmos), managed databases, load balancers, VPC networking, object storage, secret management, serverless containers, serverless functions, IAM, generative AI inference, and more. The Scaleway API uses X-Auth-Token header authentication and provides OpenAPI specifications for every product via the developer portal.
examples:
- key_count: 2
  name: Scaleway Instance Create Server Example
  slug: scaleway-instance-create-server-example
- key_count: 2
  name: Scaleway Instance List Servers Example
  slug: scaleway-instance-list-servers-example
- key_count: 2
  name: Scaleway Kubernetes List Clusters Example
  slug: scaleway-kubernetes-list-clusters-example
- key_count: 2
  name: Scaleway Secret Manager Create Secret Example
  slug: scaleway-secret-manager-create-secret-example
finops:
- name: Scaleway Finops
  service_category: Cloud Infrastructure
  slug: scaleway-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/scaleway.png
json_schemas:
- name: Scaleway Kubernetes Cluster
  property_count: 15
  slug: scaleway-cluster
- name: google.protobuf.BoolValue
  property_count: 0
  slug: scaleway-googleprotobufboolvalue
- name: google.protobuf.Int32Value
  property_count: 0
  slug: scaleway-googleprotobufint32value
- name: google.protobuf.StringValue
  property_count: 0
  slug: scaleway-googleprotobufstringvalue
- name: google.protobuf.UInt32Value
  property_count: 0
  slug: scaleway-googleprotobufuint32value
- name: Scaleway Instance
  property_count: 17
  slug: scaleway-instance
- name: scaleway.containers.v1.Container
  property_count: 31
  slug: scaleway-scalewaycontainersv1container
- name: scaleway.containers.v1.Domain
  property_count: 8
  slug: scaleway-scalewaycontainersv1domain
- name: scaleway.containers.v1.ListContainersRequest.OrderBy
  property_count: 0
  slug: scaleway-scalewaycontainersv1listcontainersrequestorderby
- name: scaleway.containers.v1.ListContainersResponse
  property_count: 2
  slug: scaleway-scalewaycontainersv1listcontainersresponse
- name: scaleway.containers.v1.ListDomainsRequest.OrderBy
  property_count: 0
  slug: scaleway-scalewaycontainersv1listdomainsrequestorderby
- name: scaleway.containers.v1.ListDomainsResponse
  property_count: 2
  slug: scaleway-scalewaycontainersv1listdomainsresponse
- name: scaleway.containers.v1.ListNamespacesRequest.OrderBy
  property_count: 0
  slug: scaleway-scalewaycontainersv1listnamespacesrequestorderby
- name: scaleway.containers.v1.ListNamespacesResponse
  property_count: 2
  slug: scaleway-scalewaycontainersv1listnamespacesresponse
- name: scaleway.containers.v1.ListTriggersRequest.OrderBy
  property_count: 0
  slug: scaleway-scalewaycontainersv1listtriggersrequestorderby
- name: scaleway.containers.v1.ListTriggersResponse
  property_count: 2
  slug: scaleway-scalewaycontainersv1listtriggersresponse
- name: scaleway.containers.v1.Namespace
  property_count: 13
  slug: scaleway-scalewaycontainersv1namespace
- name: scaleway.containers.v1.Trigger
  property_count: 14
  slug: scaleway-scalewaycontainersv1trigger
- name: scaleway.functions.v1beta1.Cron
  property_count: 6
  slug: scaleway-scalewayfunctionsv1beta1cron
- name: scaleway.functions.v1beta1.Domain
  property_count: 6
  slug: scaleway-scalewayfunctionsv1beta1domain
- name: scaleway.functions.v1beta1.DownloadURL
  property_count: 2
  slug: scaleway-scalewayfunctionsv1beta1downloadurl
- name: scaleway.functions.v1beta1.Function
  property_count: 27
  slug: scaleway-scalewayfunctionsv1beta1function
- name: scaleway.functions.v1beta1.ListCronsResponse
  property_count: 2
  slug: scaleway-scalewayfunctionsv1beta1listcronsresponse
- name: scaleway.functions.v1beta1.ListDomainsResponse
  property_count: 2
  slug: scaleway-scalewayfunctionsv1beta1listdomainsresponse
- name: scaleway.functions.v1beta1.ListFunctionRuntimesResponse
  property_count: 2
  slug: scaleway-scalewayfunctionsv1beta1listfunctionruntimesresponse
- name: scaleway.functions.v1beta1.ListFunctionsResponse
  property_count: 2
  slug: scaleway-scalewayfunctionsv1beta1listfunctionsresponse
- name: scaleway.functions.v1beta1.ListNamespacesResponse
  property_count: 2
  slug: scaleway-scalewayfunctionsv1beta1listnamespacesresponse
- name: scaleway.functions.v1beta1.ListTokensResponse
  property_count: 2
  slug: scaleway-scalewayfunctionsv1beta1listtokensresponse
- name: scaleway.functions.v1beta1.ListTriggersResponse
  property_count: 2
  slug: scaleway-scalewayfunctionsv1beta1listtriggersresponse
- name: scaleway.functions.v1beta1.Namespace
  property_count: 16
  slug: scaleway-scalewayfunctionsv1beta1namespace
- name: scaleway.functions.v1beta1.Runtime
  property_count: 10
  slug: scaleway-scalewayfunctionsv1beta1runtime
- name: scaleway.functions.v1beta1.Runtime.Status
  property_count: 0
  slug: scaleway-scalewayfunctionsv1beta1runtimestatus
- name: scaleway.functions.v1beta1.Secret
  property_count: 2
  slug: scaleway-scalewayfunctionsv1beta1secret
- name: scaleway.functions.v1beta1.SecretHashedValue
  property_count: 2
  slug: scaleway-scalewayfunctionsv1beta1secrethashedvalue
- name: scaleway.functions.v1beta1.Token
  property_count: 8
  slug: scaleway-scalewayfunctionsv1beta1token
- name: scaleway.functions.v1beta1.Trigger
  property_count: 9
  slug: scaleway-scalewayfunctionsv1beta1trigger
- name: scaleway.functions.v1beta1.UploadURL
  property_count: 2
  slug: scaleway-scalewayfunctionsv1beta1uploadurl
- name: scaleway.iam.v1alpha1.APIKey
  property_count: 13
  slug: scaleway-scalewayiamv1alpha1apikey
- name: scaleway.iam.v1alpha1.Application
  property_count: 11
  slug: scaleway-scalewayiamv1alpha1application
- name: scaleway.iam.v1alpha1.CheckPermissionsRequest.Permission
  property_count: 5
  slug: scaleway-scalewayiamv1alpha1checkpermissionsrequestpermission
- name: scaleway.iam.v1alpha1.CheckPermissionsResponse
  property_count: 1
  slug: scaleway-scalewayiamv1alpha1checkpermissionsresponse
- name: scaleway.iam.v1alpha1.CheckPermissionsResponse.Response
  property_count: 1
  slug: scaleway-scalewayiamv1alpha1checkpermissionsresponseresponse
- name: scaleway.iam.v1alpha1.CheckPermissionsResponse.Response.Decision
  property_count: 0
  slug: scaleway-scalewayiamv1alpha1checkpermissionsresponseresponsedecision
- name: scaleway.iam.v1alpha1.Connection
  property_count: 2
  slug: scaleway-scalewayiamv1alpha1connection
- name: scaleway.iam.v1alpha1.GetUserConnectionsResponse
  property_count: 1
  slug: scaleway-scalewayiamv1alpha1getuserconnectionsresponse
- name: scaleway.iam.v1alpha1.GracePeriod
  property_count: 3
  slug: scaleway-scalewayiamv1alpha1graceperiod
- name: scaleway.iam.v1alpha1.Group
  property_count: 12
  slug: scaleway-scalewayiamv1alpha1group
- name: scaleway.iam.v1alpha1.InitiateUserConnectionResponse
  property_count: 1
  slug: scaleway-scalewayiamv1alpha1initiateuserconnectionresponse
- name: scaleway.iam.v1alpha1.JWT
  property_count: 8
  slug: scaleway-scalewayiamv1alpha1jwt
- name: scaleway.iam.v1alpha1.ListAPIKeysResponse
  property_count: 2
  slug: scaleway-scalewayiamv1alpha1listapikeysresponse
- name: scaleway.iam.v1alpha1.ListApplicationsResponse
  property_count: 2
  slug: scaleway-scalewayiamv1alpha1listapplicationsresponse
- name: scaleway.iam.v1alpha1.ListGracePeriodsResponse
  property_count: 1
  slug: scaleway-scalewayiamv1alpha1listgraceperiodsresponse
- name: scaleway.iam.v1alpha1.ListGroupsResponse
  property_count: 2
  slug: scaleway-scalewayiamv1alpha1listgroupsresponse
- name: scaleway.iam.v1alpha1.ListJWTsResponse
  property_count: 2
  slug: scaleway-scalewayiamv1alpha1listjwtsresponse
- name: scaleway.iam.v1alpha1.ListLogsResponse
  property_count: 2
  slug: scaleway-scalewayiamv1alpha1listlogsresponse
- name: scaleway.iam.v1alpha1.ListPermissionSetsResponse
  property_count: 2
  slug: scaleway-scalewayiamv1alpha1listpermissionsetsresponse
- name: scaleway.iam.v1alpha1.ListPoliciesResponse
  property_count: 2
  slug: scaleway-scalewayiamv1alpha1listpoliciesresponse
- name: scaleway.iam.v1alpha1.ListQuotaResponse
  property_count: 2
  slug: scaleway-scalewayiamv1alpha1listquotaresponse
- name: scaleway.iam.v1alpha1.ListRulesResponse
  property_count: 2
  slug: scaleway-scalewayiamv1alpha1listrulesresponse
- name: scaleway.iam.v1alpha1.ListSamlCertificatesResponse
  property_count: 1
  slug: scaleway-scalewayiamv1alpha1listsamlcertificatesresponse
- name: scaleway.iam.v1alpha1.ListSSHKeysResponse
  property_count: 2
  slug: scaleway-scalewayiamv1alpha1listsshkeysresponse
- name: scaleway.iam.v1alpha1.ListUsersResponse
  property_count: 2
  slug: scaleway-scalewayiamv1alpha1listusersresponse
- name: scaleway.iam.v1alpha1.Log
  property_count: 9
  slug: scaleway-scalewayiamv1alpha1log
- name: scaleway.iam.v1alpha1.MFAOTP
  property_count: 1
  slug: scaleway-scalewayiamv1alpha1mfaotp
- name: scaleway.iam.v1alpha1.Organization
  property_count: 7
  slug: scaleway-scalewayiamv1alpha1organization
- name: scaleway.iam.v1alpha1.OrganizationSecuritySettings
  property_count: 5
  slug: scaleway-scalewayiamv1alpha1organizationsecuritysettings
- name: scaleway.iam.v1alpha1.PermissionSet
  property_count: 5
  slug: scaleway-scalewayiamv1alpha1permissionset
- name: scaleway.iam.v1alpha1.Policy
  property_count: 17
  slug: scaleway-scalewayiamv1alpha1policy
- name: scaleway.iam.v1alpha1.Quotum
  property_count: 8
  slug: scaleway-scalewayiamv1alpha1quotum
- name: scaleway.iam.v1alpha1.Quotum.Limit
  property_count: 5
  slug: scaleway-scalewayiamv1alpha1quotumlimit
- name: scaleway.iam.v1alpha1.Rule
  property_count: 7
  slug: scaleway-scalewayiamv1alpha1rule
- name: scaleway.iam.v1alpha1.RuleSpecs
  property_count: 4
  slug: scaleway-scalewayiamv1alpha1rulespecs
- name: scaleway.iam.v1alpha1.Saml
  property_count: 5
  slug: scaleway-scalewayiamv1alpha1saml
- name: scaleway.iam.v1alpha1.SamlCertificate
  property_count: 5
  slug: scaleway-scalewayiamv1alpha1samlcertificate
- name: scaleway.iam.v1alpha1.SetRulesResponse
  property_count: 1
  slug: scaleway-scalewayiamv1alpha1setrulesresponse
- name: scaleway.iam.v1alpha1.SSHKey
  property_count: 9
  slug: scaleway-scalewayiamv1alpha1sshkey
- name: scaleway.iam.v1alpha1.User
  property_count: 19
  slug: scaleway-scalewayiamv1alpha1user
- name: scaleway.iam.v1alpha1.User.Type
  property_count: 0
  slug: scaleway-scalewayiamv1alpha1usertype
- name: scaleway.iam.v1alpha1.ValidateUserMFAOTPResponse
  property_count: 1
  slug: scaleway-scalewayiamv1alpha1validateusermfaotpresponse
- name: scaleway.instance.v1.Arch
  property_count: 0
  slug: scaleway-scalewayinstancev1arch
- name: scaleway.instance.v1.AttachServerFileSystemResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1attachserverfilesystemresponse
- name: scaleway.instance.v1.AttachServerVolumeRequest.VolumeType
  property_count: 0
  slug: scaleway-scalewayinstancev1attachservervolumerequestvolumetype
- name: scaleway.instance.v1.AttachServerVolumeResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1attachservervolumeresponse
- name: scaleway.instance.v1.Bootscript
  property_count: 12
  slug: scaleway-scalewayinstancev1bootscript
- name: scaleway.instance.v1.BootType
  property_count: 0
  slug: scaleway-scalewayinstancev1boottype
- name: scaleway.instance.v1.CreateImageResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1createimageresponse
- name: scaleway.instance.v1.CreateIpResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1createipresponse
- name: scaleway.instance.v1.CreatePlacementGroupResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1createplacementgroupresponse
- name: scaleway.instance.v1.CreatePrivateNICResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1createprivatenicresponse
- name: scaleway.instance.v1.CreateSecurityGroupResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1createsecuritygroupresponse
- name: scaleway.instance.v1.CreateSecurityGroupRuleResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1createsecuritygroupruleresponse
- name: scaleway.instance.v1.CreateServerResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1createserverresponse
- name: scaleway.instance.v1.CreateSnapshotResponse
  property_count: 2
  slug: scaleway-scalewayinstancev1createsnapshotresponse
- name: scaleway.instance.v1.CreateVolumeResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1createvolumeresponse
- name: scaleway.instance.v1.Dashboard
  property_count: 16
  slug: scaleway-scalewayinstancev1dashboard
- name: scaleway.instance.v1.DetachServerFileSystemResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1detachserverfilesystemresponse
- name: scaleway.instance.v1.DetachServerVolumeResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1detachservervolumeresponse
- name: scaleway.instance.v1.ExportSnapshotResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1exportsnapshotresponse
- name: scaleway.instance.v1.GetDashboardResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1getdashboardresponse
- name: scaleway.instance.v1.GetImageResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1getimageresponse
- name: scaleway.instance.v1.GetIpResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1getipresponse
- name: scaleway.instance.v1.GetPlacementGroupResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1getplacementgroupresponse
- name: scaleway.instance.v1.GetPlacementGroupServersResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1getplacementgroupserversresponse
- name: scaleway.instance.v1.GetPrivateNICResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1getprivatenicresponse
- name: scaleway.instance.v1.GetSecurityGroupResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1getsecuritygroupresponse
- name: scaleway.instance.v1.GetSecurityGroupRuleResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1getsecuritygroupruleresponse
- name: scaleway.instance.v1.GetServerResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1getserverresponse
- name: scaleway.instance.v1.GetServerTypesAvailabilityResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1getservertypesavailabilityresponse
- name: scaleway.instance.v1.GetSnapshotResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1getsnapshotresponse
- name: scaleway.instance.v1.GetVolumeResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1getvolumeresponse
- name: scaleway.instance.v1.Image
  property_count: 15
  slug: scaleway-scalewayinstancev1image
- name: scaleway.instance.v1.Image.State
  property_count: 0
  slug: scaleway-scalewayinstancev1imagestate
- name: scaleway.instance.v1.Ip
  property_count: 12
  slug: scaleway-scalewayinstancev1ip
- name: scaleway.instance.v1.Ip.State
  property_count: 0
  slug: scaleway-scalewayinstancev1ipstate
- name: scaleway.instance.v1.IpType
  property_count: 0
  slug: scaleway-scalewayinstancev1iptype
- name: scaleway.instance.v1.ListImagesResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1listimagesresponse
- name: scaleway.instance.v1.ListIpsResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1listipsresponse
- name: scaleway.instance.v1.ListPlacementGroupsResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1listplacementgroupsresponse
- name: scaleway.instance.v1.ListPrivateNICsResponse
  property_count: 2
  slug: scaleway-scalewayinstancev1listprivatenicsresponse
- name: scaleway.instance.v1.ListSecurityGroupRulesResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1listsecuritygrouprulesresponse
- name: scaleway.instance.v1.ListSecurityGroupsResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1listsecuritygroupsresponse
- name: scaleway.instance.v1.ListServerActionsResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1listserveractionsresponse
- name: scaleway.instance.v1.ListServersResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1listserversresponse
- name: scaleway.instance.v1.ListServersTypesResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1listserverstypesresponse
- name: scaleway.instance.v1.ListServerUserDataResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1listserveruserdataresponse
- name: scaleway.instance.v1.ListSnapshotsResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1listsnapshotsresponse
- name: scaleway.instance.v1.ListVolumesResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1listvolumesresponse
- name: scaleway.instance.v1.ListVolumesTypesResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1listvolumestypesresponse
- name: scaleway.instance.v1.MigrationPlan
  property_count: 3
  slug: scaleway-scalewayinstancev1migrationplan
- name: scaleway.instance.v1.NullableStringValue
  property_count: 0
  slug: scaleway-scalewayinstancev1nullablestringvalue
- name: scaleway.instance.v1.PlacementGroup
  property_count: 9
  slug: scaleway-scalewayinstancev1placementgroup
- name: scaleway.instance.v1.PlacementGroup.PolicyMode
  property_count: 0
  slug: scaleway-scalewayinstancev1placementgrouppolicymode
- name: scaleway.instance.v1.PlacementGroup.PolicyType
  property_count: 0
  slug: scaleway-scalewayinstancev1placementgrouppolicytype
- name: scaleway.instance.v1.PlacementGroupServer
  property_count: 3
  slug: scaleway-scalewayinstancev1placementgroupserver
- name: scaleway.instance.v1.PrivateNIC
  property_count: 8
  slug: scaleway-scalewayinstancev1privatenic
- name: scaleway.instance.v1.SecurityGroup
  property_count: 17
  slug: scaleway-scalewayinstancev1securitygroup
- name: scaleway.instance.v1.SecurityGroupRule
  property_count: 10
  slug: scaleway-scalewayinstancev1securitygrouprule
- name: scaleway.instance.v1.SecurityGroupRule.Action
  property_count: 0
  slug: scaleway-scalewayinstancev1securitygroupruleaction
- name: scaleway.instance.v1.SecurityGroupRule.Direction
  property_count: 0
  slug: scaleway-scalewayinstancev1securitygroupruledirection
- name: scaleway.instance.v1.SecurityGroupRule.Protocol
  property_count: 0
  slug: scaleway-scalewayinstancev1securitygroupruleprotocol
- name: scaleway.instance.v1.SecurityGroupTemplate
  property_count: 2
  slug: scaleway-scalewayinstancev1securitygrouptemplate
- name: scaleway.instance.v1.Server
  property_count: 36
  slug: scaleway-scalewayinstancev1server
- name: scaleway.instance.v1.Server.Action
  property_count: 0
  slug: scaleway-scalewayinstancev1serveraction
- name: scaleway.instance.v1.ServerActionResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1serveractionresponse
- name: scaleway.instance.v1.ServerCompatibleTypes
  property_count: 1
  slug: scaleway-scalewayinstancev1servercompatibletypes
- name: scaleway.instance.v1.Server.Filesystem
  property_count: 2
  slug: scaleway-scalewayinstancev1serverfilesystem
- name: scaleway.instance.v1.Server.Filesystem.State
  property_count: 0
  slug: scaleway-scalewayinstancev1serverfilesystemstate
- name: scaleway.instance.v1.Server.Ip
  property_count: 10
  slug: scaleway-scalewayinstancev1serverip
- name: scaleway.instance.v1.Server.Maintenance
  property_count: 2
  slug: scaleway-scalewayinstancev1servermaintenance
- name: scaleway.instance.v1.ServerSummary
  property_count: 2
  slug: scaleway-scalewayinstancev1serversummary
- name: scaleway.instance.v1.ServerType.Network.Interface
  property_count: 2
  slug: scaleway-scalewayinstancev1servertypenetworkinterface
- name: scaleway.instance.v1.ServerTypesAvailability
  property_count: 0
  slug: scaleway-scalewayinstancev1servertypesavailability
- name: scaleway.instance.v1.SetImageResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1setimageresponse
- name: scaleway.instance.v1.SetPlacementGroupResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1setplacementgroupresponse
- name: scaleway.instance.v1.SetPlacementGroupServersResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1setplacementgroupserversresponse
- name: scaleway.instance.v1.SetSecurityGroupResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1setsecuritygroupresponse
- name: scaleway.instance.v1.SetSecurityGroupRuleResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1setsecuritygroupruleresponse
- name: scaleway.instance.v1.SetSecurityGroupRulesRequest.Rule
  property_count: 10
  slug: scaleway-scalewayinstancev1setsecuritygrouprulesrequestrule
- name: scaleway.instance.v1.SetSecurityGroupRulesResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1setsecuritygrouprulesresponse
- name: scaleway.instance.v1.SetSnapshotResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1setsnapshotresponse
- name: scaleway.instance.v1.SetVolumeResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1setvolumeresponse
- name: scaleway.instance.v1.Snapshot
  property_count: 13
  slug: scaleway-scalewayinstancev1snapshot
- name: scaleway.instance.v1.Snapshot.BaseVolume
  property_count: 2
  slug: scaleway-scalewayinstancev1snapshotbasevolume
- name: scaleway.instance.v1.Snapshot.State
  property_count: 0
  slug: scaleway-scalewayinstancev1snapshotstate
- name: scaleway.instance.v1.Task
  property_count: 9
  slug: scaleway-scalewayinstancev1task
- name: scaleway.instance.v1.UpdateImageResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1updateimageresponse
- name: scaleway.instance.v1.UpdateIpResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1updateipresponse
- name: scaleway.instance.v1.UpdatePlacementGroupResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1updateplacementgroupresponse
- name: scaleway.instance.v1.UpdatePlacementGroupServersResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1updateplacementgroupserversresponse
- name: scaleway.instance.v1.UpdateSecurityGroupResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1updatesecuritygroupresponse
- name: scaleway.instance.v1.UpdateSecurityGroupRuleResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1updatesecuritygroupruleresponse
- name: scaleway.instance.v1.UpdateServerResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1updateserverresponse
- name: scaleway.instance.v1.UpdateSnapshotResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1updatesnapshotresponse
- name: scaleway.instance.v1.UpdateVolumeResponse
  property_count: 1
  slug: scaleway-scalewayinstancev1updatevolumeresponse
- name: scaleway.instance.v1.Volume
  property_count: 13
  slug: scaleway-scalewayinstancev1volume
- name: scaleway.instance.v1.VolumeServer.State
  property_count: 0
  slug: scaleway-scalewayinstancev1volumeserverstate
- name: scaleway.instance.v1.VolumeServerTemplate
  property_count: 8
  slug: scaleway-scalewayinstancev1volumeservertemplate
- name: scaleway.instance.v1.VolumeServer.VolumeType
  property_count: 0
  slug: scaleway-scalewayinstancev1volumeservervolumetype
- name: scaleway.instance.v1.VolumeSummary
  property_count: 4
  slug: scaleway-scalewayinstancev1volumesummary
- name: scaleway.instance.v1.VolumeType.Capabilities
  property_count: 1
  slug: scaleway-scalewayinstancev1volumetypecapabilities
- name: scaleway.instance.v1.VolumeType.Constraints
  property_count: 2
  slug: scaleway-scalewayinstancev1volumetypeconstraints
- name: scaleway.instance.v1.Volume.VolumeType
  property_count: 0
  slug: scaleway-scalewayinstancev1volumevolumetype
- name: scaleway.k8s.v1.ACLRule
  property_count: 4
  slug: scaleway-scalewayk8sv1aclrule
- name: scaleway.k8s.v1.ACLRuleRequest
  property_count: 3
  slug: scaleway-scalewayk8sv1aclrulerequest
- name: scaleway.k8s.v1.AddClusterACLRulesResponse
  property_count: 1
  slug: scaleway-scalewayk8sv1addclusteraclrulesresponse
- name: scaleway.k8s.v1.Cluster
  property_count: 29
  slug: scaleway-scalewayk8sv1cluster
- name: scaleway.k8s.v1.ClusterType
  property_count: 9
  slug: scaleway-scalewayk8sv1clustertype
- name: scaleway.k8s.v1.CNI
  property_count: 0
  slug: scaleway-scalewayk8sv1cni
- name: scaleway.k8s.v1.CoreV1Taint
  property_count: 3
  slug: scaleway-scalewayk8sv1corev1taint
- name: scaleway.k8s.v1.CreateClusterRequest.PoolConfig
  property_count: 20
  slug: scaleway-scalewayk8sv1createclusterrequestpoolconfig
- name: scaleway.k8s.v1.ExternalNode
  property_count: 14
  slug: scaleway-scalewayk8sv1externalnode
- name: scaleway.k8s.v1.ExternalNode.CoreV1Taint
  property_count: 3
  slug: scaleway-scalewayk8sv1externalnodecorev1taint
- name: scaleway.k8s.v1.ListClusterACLRulesResponse
  property_count: 2
  slug: scaleway-scalewayk8sv1listclusteraclrulesresponse
- name: scaleway.k8s.v1.ListClusterAvailableTypesResponse
  property_count: 2
  slug: scaleway-scalewayk8sv1listclusteravailabletypesresponse
- name: scaleway.k8s.v1.ListClusterAvailableVersionsResponse
  property_count: 1
  slug: scaleway-scalewayk8sv1listclusteravailableversionsresponse
- name: scaleway.k8s.v1.ListClustersResponse
  property_count: 2
  slug: scaleway-scalewayk8sv1listclustersresponse
- name: scaleway.k8s.v1.ListClusterTypesResponse
  property_count: 2
  slug: scaleway-scalewayk8sv1listclustertypesresponse
- name: scaleway.k8s.v1.ListNodesResponse
  property_count: 2
  slug: scaleway-scalewayk8sv1listnodesresponse
- name: scaleway.k8s.v1.ListPoolsResponse
  property_count: 2
  slug: scaleway-scalewayk8sv1listpoolsresponse
- name: scaleway.k8s.v1.ListVersionsResponse
  property_count: 1
  slug: scaleway-scalewayk8sv1listversionsresponse
- name: scaleway.k8s.v1.Node
  property_count: 10
  slug: scaleway-scalewayk8sv1node
- name: scaleway.k8s.v1.Pool
  property_count: 27
  slug: scaleway-scalewayk8sv1pool
- name: scaleway.k8s.v1.Runtime
  property_count: 0
  slug: scaleway-scalewayk8sv1runtime
- name: scaleway.k8s.v1.SetClusterACLRulesResponse
  property_count: 1
  slug: scaleway-scalewayk8sv1setclusteraclrulesresponse
- name: scaleway.k8s.v1.Version
  property_count: 11
  slug: scaleway-scalewayk8sv1version
- name: scaleway.lb.v1.Acl
  property_count: 9
  slug: scaleway-scalewaylbv1acl
- name: scaleway.lb.v1.AclSpec
  property_count: 5
  slug: scaleway-scalewaylbv1aclspec
- name: scaleway.lb.v1.Backend
  property_count: 25
  slug: scaleway-scalewaylbv1backend
- name: scaleway.lb.v1.BackendServerStats
  property_count: 6
  slug: scaleway-scalewaylbv1backendserverstats
- name: scaleway.lb.v1.Certificate
  property_count: 13
  slug: scaleway-scalewaylbv1certificate
- name: scaleway.lb.v1.Frontend
  property_count: 13
  slug: scaleway-scalewaylbv1frontend
- name: scaleway.lb.v1.HealthCheck
  property_count: 13
  slug: scaleway-scalewaylbv1healthcheck
- name: scaleway.lb.v1.Instance
  property_count: 7
  slug: scaleway-scalewaylbv1instance
- name: scaleway.lb.v1.Ip
  property_count: 9
  slug: scaleway-scalewaylbv1ip
- name: scaleway.lb.v1.Lb
  property_count: 20
  slug: scaleway-scalewaylbv1lb
- name: scaleway.lb.v1.LbStats
  property_count: 1
  slug: scaleway-scalewaylbv1lbstats
- name: scaleway.lb.v1.LbType
  property_count: 7
  slug: scaleway-scalewaylbv1lbtype
- name: scaleway.lb.v1.ListAclResponse
  property_count: 2
  slug: scaleway-scalewaylbv1listaclresponse
- name: scaleway.lb.v1.ListBackendsResponse
  property_count: 2
  slug: scaleway-scalewaylbv1listbackendsresponse
- name: scaleway.lb.v1.ListBackendStatsResponse
  property_count: 2
  slug: scaleway-scalewaylbv1listbackendstatsresponse
- name: scaleway.lb.v1.ListCertificatesResponse
  property_count: 2
  slug: scaleway-scalewaylbv1listcertificatesresponse
- name: scaleway.lb.v1.ListFrontendsResponse
  property_count: 2
  slug: scaleway-scalewaylbv1listfrontendsresponse
- name: scaleway.lb.v1.ListIpsResponse
  property_count: 2
  slug: scaleway-scalewaylbv1listipsresponse
- name: scaleway.lb.v1.ListLbPrivateNetworksResponse
  property_count: 2
  slug: scaleway-scalewaylbv1listlbprivatenetworksresponse
- name: scaleway.lb.v1.ListLbsResponse
  property_count: 2
  slug: scaleway-scalewaylbv1listlbsresponse
- name: scaleway.lb.v1.ListLbTypesResponse
  property_count: 2
  slug: scaleway-scalewaylbv1listlbtypesresponse
- name: scaleway.lb.v1.ListRoutesResponse
  property_count: 2
  slug: scaleway-scalewaylbv1listroutesresponse
- name: scaleway.lb.v1.ListSubscriberResponse
  property_count: 2
  slug: scaleway-scalewaylbv1listsubscriberresponse
- name: scaleway.lb.v1.PrivateNetwork
  property_count: 8
  slug: scaleway-scalewaylbv1privatenetwork
- name: scaleway.lb.v1.Route
  property_count: 6
  slug: scaleway-scalewaylbv1route
- name: scaleway.lb.v1.SetAclsResponse
  property_count: 2
  slug: scaleway-scalewaylbv1setaclsresponse
- name: scaleway.lb.v1.Subscriber
  property_count: 4
  slug: scaleway-scalewaylbv1subscriber
- name: scaleway.rdb.v1.ACLRule
  property_count: 6
  slug: scaleway-scalewayrdbv1aclrule
- name: scaleway.rdb.v1.ACLRule.Action
  property_count: 0
  slug: scaleway-scalewayrdbv1aclruleaction
- name: scaleway.rdb.v1.ACLRule.Direction
  property_count: 0
  slug: scaleway-scalewayrdbv1aclruledirection
- name: scaleway.rdb.v1.ACLRule.Protocol
  property_count: 0
  slug: scaleway-scalewayrdbv1aclruleprotocol
- name: scaleway.rdb.v1.ACLRuleRequest
  property_count: 2
  slug: scaleway-scalewayrdbv1aclrulerequest
- name: scaleway.rdb.v1.AddInstanceACLRulesResponse
  property_count: 1
  slug: scaleway-scalewayrdbv1addinstanceaclrulesresponse
- name: scaleway.rdb.v1.AddInstanceSettingsResponse
  property_count: 1
  slug: scaleway-scalewayrdbv1addinstancesettingsresponse
- name: scaleway.rdb.v1.Database
  property_count: 4
  slug: scaleway-scalewayrdbv1database
- name: scaleway.rdb.v1.DatabaseBackup
  property_count: 14
  slug: scaleway-scalewayrdbv1databasebackup
- name: scaleway.rdb.v1.DatabaseEngine
  property_count: 4
  slug: scaleway-scalewayrdbv1databaseengine
- name: scaleway.rdb.v1.DeleteInstanceACLRulesResponse
  property_count: 1
  slug: scaleway-scalewayrdbv1deleteinstanceaclrulesresponse
- name: scaleway.rdb.v1.DeleteInstanceSettingsResponse
  property_count: 1
  slug: scaleway-scalewayrdbv1deleteinstancesettingsresponse
- name: scaleway.rdb.v1.Endpoint
  property_count: 8
  slug: scaleway-scalewayrdbv1endpoint
- name: scaleway.rdb.v1.EndpointSpec
  property_count: 2
  slug: scaleway-scalewayrdbv1endpointspec
- name: scaleway.rdb.v1.EngineSetting
  property_count: 11
  slug: scaleway-scalewayrdbv1enginesetting
- name: scaleway.rdb.v1.EngineVersion
  property_count: 7
  slug: scaleway-scalewayrdbv1engineversion
- name: scaleway.rdb.v1.Instance
  property_count: 23
  slug: scaleway-scalewayrdbv1instance
- name: scaleway.rdb.v1.InstanceLog
  property_count: 7
  slug: scaleway-scalewayrdbv1instancelog
- name: scaleway.rdb.v1.InstanceMetrics
  property_count: 1
  slug: scaleway-scalewayrdbv1instancemetrics
- name: scaleway.rdb.v1.InstanceSetting
  property_count: 2
  slug: scaleway-scalewayrdbv1instancesetting
- name: scaleway.rdb.v1.ListDatabaseBackupsResponse
  property_count: 2
  slug: scaleway-scalewayrdbv1listdatabasebackupsresponse
- name: scaleway.rdb.v1.ListDatabaseEnginesResponse
  property_count: 2
  slug: scaleway-scalewayrdbv1listdatabaseenginesresponse
- name: scaleway.rdb.v1.ListDatabasesResponse
  property_count: 2
  slug: scaleway-scalewayrdbv1listdatabasesresponse
- name: scaleway.rdb.v1.ListInstanceACLRulesResponse
  property_count: 2
  slug: scaleway-scalewayrdbv1listinstanceaclrulesresponse
- name: scaleway.rdb.v1.ListInstanceLogsDetailsResponse
  property_count: 1
  slug: scaleway-scalewayrdbv1listinstancelogsdetailsresponse
- name: scaleway.rdb.v1.ListInstanceLogsDetailsResponse.InstanceLogDetail
  property_count: 2
  slug: scaleway-scalewayrdbv1listinstancelogsdetailsresponseinstancelogdetai
- name: scaleway.rdb.v1.ListInstanceLogsResponse
  property_count: 1
  slug: scaleway-scalewayrdbv1listinstancelogsresponse
- name: scaleway.rdb.v1.ListInstancesResponse
  property_count: 2
  slug: scaleway-scalewayrdbv1listinstancesresponse
- name: scaleway.rdb.v1.ListNodeTypesResponse
  property_count: 2
  slug: scaleway-scalewayrdbv1listnodetypesresponse
- name: scaleway.rdb.v1.ListPrivilegesResponse
  property_count: 2
  slug: scaleway-scalewayrdbv1listprivilegesresponse
- name: scaleway.rdb.v1.ListSnapshotsResponse
  property_count: 2
  slug: scaleway-scalewayrdbv1listsnapshotsresponse
- name: scaleway.rdb.v1.ListUsersResponse
  property_count: 2
  slug: scaleway-scalewayrdbv1listusersresponse
- name: scaleway.rdb.v1.Maintenance
  property_count: 7
  slug: scaleway-scalewayrdbv1maintenance
- name: scaleway.rdb.v1.NodeType
  property_count: 14
  slug: scaleway-scalewayrdbv1nodetype
- name: scaleway.rdb.v1.NodeType.VolumeType
  property_count: 6
  slug: scaleway-scalewayrdbv1nodetypevolumetype
- name: scaleway.rdb.v1.PrepareInstanceLogsResponse
  property_count: 1
  slug: scaleway-scalewayrdbv1prepareinstancelogsresponse
- name: scaleway.rdb.v1.Privilege
  property_count: 3
  slug: scaleway-scalewayrdbv1privilege
- name: scaleway.rdb.v1.ReadReplica
  property_count: 6
  slug: scaleway-scalewayrdbv1readreplica
- name: scaleway.rdb.v1.ReadReplicaEndpointSpec
  property_count: 2
  slug: scaleway-scalewayrdbv1readreplicaendpointspec
- name: scaleway.rdb.v1.SetInstanceACLRulesResponse
  property_count: 1
  slug: scaleway-scalewayrdbv1setinstanceaclrulesresponse
- name: scaleway.rdb.v1.SetInstanceSettingsResponse
  property_count: 1
  slug: scaleway-scalewayrdbv1setinstancesettingsresponse
- name: scaleway.rdb.v1.Snapshot
  property_count: 12
  slug: scaleway-scalewayrdbv1snapshot
- name: scaleway.rdb.v1.StorageClass
  property_count: 0
  slug: scaleway-scalewayrdbv1storageclass
- name: scaleway.rdb.v1.UpgradableVersion
  property_count: 4
  slug: scaleway-scalewayrdbv1upgradableversion
- name: scaleway.rdb.v1.User
  property_count: 2
  slug: scaleway-scalewayrdbv1user
- name: scaleway.rdb.v1.Volume.Type
  property_count: 0
  slug: scaleway-scalewayrdbv1volumetype
- name: scaleway.secret_manager.v1beta1.AccessSecretVersionResponse
  property_count: 5
  slug: scaleway-scalewaysecret-managerv1beta1accesssecretversionresponse
- name: scaleway.secret_manager.v1beta1.ListSecretsRequest.OrderBy
  property_count: 0
  slug: scaleway-scalewaysecret-managerv1beta1listsecretsrequestorderby
- name: scaleway.secret_manager.v1beta1.ListSecretsResponse
  property_count: 2
  slug: scaleway-scalewaysecret-managerv1beta1listsecretsresponse
- name: scaleway.secret_manager.v1beta1.ListSecretVersionsResponse
  property_count: 2
  slug: scaleway-scalewaysecret-managerv1beta1listsecretversionsresponse
- name: scaleway.secret_manager.v1beta1.Product
  property_count: 0
  slug: scaleway-scalewaysecret-managerv1beta1product
- name: scaleway.secret_manager.v1beta1.Secret
  property_count: 18
  slug: scaleway-scalewaysecret-managerv1beta1secret
- name: scaleway.secret_manager.v1beta1.SecretVersion
  property_count: 11
  slug: scaleway-scalewaysecret-managerv1beta1secretversion
- name: scaleway.secret_manager.v1beta1.SecretVersion.Status
  property_count: 0
  slug: scaleway-scalewaysecret-managerv1beta1secretversionstatus
- name: scaleway.std.File
  property_count: 3
  slug: scaleway-scalewaystdfile
- name: scaleway.std.ServiceInfo
  property_count: 6
  slug: scaleway-scalewaystdserviceinfo
- name: scaleway.std.StringsValue
  property_count: 0
  slug: scaleway-scalewaystdstringsvalue
- name: scaleway.std.TimeSeries
  property_count: 3
  slug: scaleway-scalewaystdtimeseries
- name: scaleway.std.TimeSeries.Point
  property_count: 0
  slug: scaleway-scalewaystdtimeseriespoint
- name: scaleway.transactional_email.v1alpha1.Blocklist
  property_count: 9
  slug: scaleway-scalewaytransactional-emailv1alpha1blocklist
- name: scaleway.transactional_email.v1alpha1.BulkCreateBlocklistsResponse
  property_count: 1
  slug: scaleway-scalewaytransactional-emailv1alpha1bulkcreateblocklistsrespo
- name: scaleway.transactional_email.v1alpha1.CreateEmailRequest.Address
  property_count: 2
  slug: scaleway-scalewaytransactional-emailv1alpha1createemailrequestaddress
- name: scaleway.transactional_email.v1alpha1.CreateEmailRequest.Attachment
  property_count: 3
  slug: scaleway-scalewaytransactional-emailv1alpha1createemailrequestattachm
- name: scaleway.transactional_email.v1alpha1.CreateEmailRequest.Header
  property_count: 2
  slug: scaleway-scalewaytransactional-emailv1alpha1createemailrequestheader
- name: scaleway.transactional_email.v1alpha1.CreateEmailResponse
  property_count: 1
  slug: scaleway-scalewaytransactional-emailv1alpha1createemailresponse
- name: scaleway.transactional_email.v1alpha1.Domain
  property_count: 17
  slug: scaleway-scalewaytransactional-emailv1alpha1domain
- name: scaleway.transactional_email.v1alpha1.DomainLastStatus
  property_count: 7
  slug: scaleway-scalewaytransactional-emailv1alpha1domainlaststatus
- name: scaleway.transactional_email.v1alpha1.Domain.Status
  property_count: 0
  slug: scaleway-scalewaytransactional-emailv1alpha1domainstatus
- name: scaleway.transactional_email.v1alpha1.Email
  property_count: 15
  slug: scaleway-scalewaytransactional-emailv1alpha1email
- name: scaleway.transactional_email.v1alpha1.Email.Flag
  property_count: 0
  slug: scaleway-scalewaytransactional-emailv1alpha1emailflag
- name: scaleway.transactional_email.v1alpha1.Email.Status
  property_count: 0
  slug: scaleway-scalewaytransactional-emailv1alpha1emailstatus
- name: scaleway.transactional_email.v1alpha1.Email.Try
  property_count: 4
  slug: scaleway-scalewaytransactional-emailv1alpha1emailtry
- name: scaleway.transactional_email.v1alpha1.ListBlocklistsResponse
  property_count: 2
  slug: scaleway-scalewaytransactional-emailv1alpha1listblocklistsresponse
- name: scaleway.transactional_email.v1alpha1.ListDomainsResponse
  property_count: 2
  slug: scaleway-scalewaytransactional-emailv1alpha1listdomainsresponse
- name: scaleway.transactional_email.v1alpha1.ListEmailsResponse
  property_count: 2
  slug: scaleway-scalewaytransactional-emailv1alpha1listemailsresponse
- name: scaleway.transactional_email.v1alpha1.ListOffersResponse
  property_count: 2
  slug: scaleway-scalewaytransactional-emailv1alpha1listoffersresponse
- name: scaleway.transactional_email.v1alpha1.ListOfferSubscriptionsResponse
  property_count: 2
  slug: scaleway-scalewaytransactional-emailv1alpha1listoffersubscriptionsres
- name: scaleway.transactional_email.v1alpha1.ListPoolsResponse
  property_count: 2
  slug: scaleway-scalewaytransactional-emailv1alpha1listpoolsresponse
- name: scaleway.transactional_email.v1alpha1.ListWebhookEventsResponse
  property_count: 2
  slug: scaleway-scalewaytransactional-emailv1alpha1listwebhookeventsresponse
- name: scaleway.transactional_email.v1alpha1.ListWebhooksResponse
  property_count: 2
  slug: scaleway-scalewaytransactional-emailv1alpha1listwebhooksresponse
- name: scaleway.transactional_email.v1alpha1.Offer
  property_count: 9
  slug: scaleway-scalewaytransactional-emailv1alpha1offer
- name: scaleway.transactional_email.v1alpha1.OfferSubscription
  property_count: 11
  slug: scaleway-scalewaytransactional-emailv1alpha1offersubscription
- name: scaleway.transactional_email.v1alpha1.Pool
  property_count: 6
  slug: scaleway-scalewaytransactional-emailv1alpha1pool
- name: scaleway.transactional_email.v1alpha1.ProjectConsumption
  property_count: 6
  slug: scaleway-scalewaytransactional-emailv1alpha1projectconsumption
- name: scaleway.transactional_email.v1alpha1.ProjectSettings
  property_count: 1
  slug: scaleway-scalewaytransactional-emailv1alpha1projectsettings
- name: scaleway.transactional_email.v1alpha1.Statistics
  property_count: 6
  slug: scaleway-scalewaytransactional-emailv1alpha1statistics
- name: scaleway.transactional_email.v1alpha1.Webhook
  property_count: 9
  slug: scaleway-scalewaytransactional-emailv1alpha1webhook
- name: scaleway.transactional_email.v1alpha1.WebhookEvent
  property_count: 11
  slug: scaleway-scalewaytransactional-emailv1alpha1webhookevent
- name: scaleway.transactional_email.v1alpha1.WebhookEvent.Status
  property_count: 0
  slug: scaleway-scalewaytransactional-emailv1alpha1webhookeventstatus
- name: scaleway.transactional_email.v1alpha1.WebhookEvent.Type
  property_count: 0
  slug: scaleway-scalewaytransactional-emailv1alpha1webhookeventtype
- name: scaleway.vpc.v2.AclRule
  property_count: 9
  slug: scaleway-scalewayvpcv2aclrule
- name: scaleway.vpc.v2.Action
  property_count: 0
  slug: scaleway-scalewayvpcv2action
- name: scaleway.vpc.v2.AddSubnetsResponse
  property_count: 1
  slug: scaleway-scalewayvpcv2addsubnetsresponse
- name: scaleway.vpc.v2.DeleteSubnetsResponse
  property_count: 1
  slug: scaleway-scalewayvpcv2deletesubnetsresponse
- name: scaleway.vpc.v2.GetAclResponse
  property_count: 2
  slug: scaleway-scalewayvpcv2getaclresponse
- name: scaleway.vpc.v2.ListPrivateNetworksResponse
  property_count: 2
  slug: scaleway-scalewayvpcv2listprivatenetworksresponse
- name: scaleway.vpc.v2.ListSubnetOverlapsResponse
  property_count: 2
  slug: scaleway-scalewayvpcv2listsubnetoverlapsresponse
- name: scaleway.vpc.v2.ListSubnetOverlapsResponse.SubnetOverlap
  property_count: 4
  slug: scaleway-scalewayvpcv2listsubnetoverlapsresponsesubnetoverlap
- name: scaleway.vpc.v2.ListSubnetsResponse
  property_count: 2
  slug: scaleway-scalewayvpcv2listsubnetsresponse
- name: scaleway.vpc.v2.ListVPCConnectorsResponse
  property_count: 2
  slug: scaleway-scalewayvpcv2listvpcconnectorsresponse
- name: scaleway.vpc.v2.ListVPCsResponse
  property_count: 2
  slug: scaleway-scalewayvpcv2listvpcsresponse
- name: scaleway.vpc.v2.PrivateNetwork
  property_count: 12
  slug: scaleway-scalewayvpcv2privatenetwork
- name: scaleway.vpc.v2.Route
  property_count: 13
  slug: scaleway-scalewayvpcv2route
- name: scaleway.vpc.v2.SetAclResponse
  property_count: 2
  slug: scaleway-scalewayvpcv2setaclresponse
- name: scaleway.vpc.v2.Subnet
  property_count: 7
  slug: scaleway-scalewayvpcv2subnet
- name: scaleway.vpc.v2.VPC
  property_count: 12
  slug: scaleway-scalewayvpcv2vpc
- name: scaleway.vpc.v2.VPCConnector
  property_count: 12
  slug: scaleway-scalewayvpcv2vpcconnector
- name: Scaleway Secret
  property_count: 14
  slug: scaleway-secret
json_structures:
- name: Scaleway Cluster Structure
  property_count: 0
  slug: scaleway-cluster-structure
- name: Scaleway Instance Structure
  property_count: 0
  slug: scaleway-instance-structure
- name: Scaleway Structure
  property_count: 0
  slug: scaleway-structure
jsonld:
- class_count: 1
  name: Scaleway Context
  property_count: 31
  slug: scaleway-context
layout: provider
modified: '2026-05-19'
name: Scaleway
nav: Providers
network: true
overview: 'Scaleway publishes 73 APIs on the [APIs.io](https://apis.io/) network, including Access Control List API, ACLs API, Alert Subscribers API, and 70 more. Tagged areas include AI, Cloud Computing, Containers, Database, and European Cloud.


  The Scaleway catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Scaleway''s developer surface includes authentication, developer portal, documentation, API reference, GitHub presence, CLI, pricing, and 19 more developer resources.'
plans:
- name: Scaleway Plans Pricing
  plan_count: 2
  slug: scaleway-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Scaleway Rate Limits
  slug: scaleway-rate-limits
rules:
- name: Scaleway API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: scaleway-jsonschema-spectral-rules
- name: Scaleway API Rules
  rule_count: 10
  severity_counts:
    error: 2
    hint: 2
    info: 0
    warn: 6
  slug: scaleway-rules
score:
  band: strong
  composite: 57.8
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 64.1
    developer_ergonomics: 63.0
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 42.1
  previous_composite: 57.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 73
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Scaleway Authentication
  slug: scaleway-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Scaleway Domain Security
  slug: scaleway-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Scaleway Vulnerability Disclosure
  slug: scaleway-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Scaleway Trust Center
  slug: scaleway-trust-center
  summary_line: ISO 27001, GDPR, CSA STAR
slug: scaleway
tags:
- AI
- Cloud Computing
- Containers
- Database
- European Cloud
- Infrastructure
- Kubernetes
- Serverless
- Storage
website: https://www.scaleway.com/en/developers/
---
