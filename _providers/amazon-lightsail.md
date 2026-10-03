---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.2
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 97
  human_in_the_loop: 13
  name: Amazon Lightsail Agentic Access
  operation_count: 162
  slug: amazon-lightsail-agentic-access
  summary_line: 162 operations · 97 acting · 13 human-in-the-loop
api_count: 3
apis:
- baseURL: https://lightsail.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Account API from Amazon Lightsail — 14 operation(s) for account.
  name: Amazon Lightsail Account API
  phrasing_intents:
  - id: CreateCloudFormationStack
    intent: Create an EC2 instance from an exported snapshot
    question: How do I turn an exported Lightsail snapshot into a full EC2 instance?
  - id: DeleteKnownHostKeys
    intent: Reset browser SSH/RDP known host keys
    question: The browser SSH client says the host key changed — how can I clear the saved key?
  - id: DisableAddOn
    intent: Turn off an add-on such as automatic snapshots
    question: How do I switch off automatic snapshots on an instance or disk?
  - id: EnableAddOn
    intent: Enable or change an add-on on a resource
    question: How can I turn on automatic daily snapshots for my Lightsail instance?
  - id: GetActiveNames
    intent: List names of all active resources
    question: What resource names are currently in use in my Lightsail account?
  - id: GetCloudFormationStackRecords
    intent: List CloudFormation stack records from exports
    question: Where can I see the CloudFormation stacks created when I moved snapshots to EC2?
  - id: GetProfile
    intent: Get my Lightsail account profile
    question: What does my Lightsail account profile look like?
  - id: IsVpcPeered
    intent: Check whether the Lightsail VPC is peered
    question: Is my Lightsail VPC peered with my default VPC?
  phrasing_ops: 14
  slug: amazon-lightsail-account-api
- baseURL: https://lightsail.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Alarms API from Amazon Lightsail — 4 operation(s) for alarms.
  name: Amazon Lightsail Alarms API
  phrasing_intents:
  - id: DeleteAlarm
    intent: Delete a metric alarm
    question: How do I get rid of an alarm I no longer need?
  - id: GetAlarms
    intent: List configured metric alarms
    question: Which alarms are set up on my Lightsail resources?
  - id: PutAlarm
    intent: Create or update a metric alarm
    question: How do I get alerted when my instance CPU goes over 80%?
  - id: TestAlarm
    intent: Test an alarm's notifications
    question: How can I check that an alarm actually sends me a notification?
  phrasing_ops: 4
  slug: amazon-lightsail-alarms-api
- baseURL: https://lightsail.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Blueprints API from Amazon Lightsail — 1 operation(s) for blueprints.
  name: Amazon Lightsail Blueprints API
  phrasing_intents:
  - id: GetBlueprints
    intent: List available instance images (blueprints)
    question: Which operating systems and apps can I launch a Lightsail instance with?
  phrasing_ops: 1
  slug: amazon-lightsail-blueprints-api
- baseURL: https://lightsail.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Buckets API from Amazon Lightsail — 11 operation(s) for buckets.
  name: Amazon Lightsail Buckets API
  phrasing_intents:
  - id: CreateBucket
    intent: Create an object storage bucket
    question: How do I create a Lightsail bucket to store files and images?
  - id: CreateBucketAccessKey
    intent: Create an access key for a bucket
    question: How do I get programmatic credentials for a single bucket?
  - id: DeleteBucket
    intent: Delete a storage bucket
    question: How do I delete a bucket that still has objects in it?
  - id: DeleteBucketAccessKey
    intent: Revoke a bucket access key
    question: My bucket secret key leaked — how do I revoke that access key?
  - id: GetBucketAccessKeys
    intent: List a bucket's access key IDs
    question: Which access keys exist for my bucket?
  - id: GetBucketBundles
    intent: List bucket storage plans
    question: What storage plans and prices are available for buckets?
  - id: GetBucketMetricData
    intent: Get storage metrics for a bucket
    question: How much space is my bucket using over time?
  - id: GetBuckets
    intent: List buckets or get one bucket's details
    question: What buckets do I have and what are their access settings?
  phrasing_ops: 11
  slug: amazon-lightsail-buckets-api
- baseURL: https://lightsail.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Bundles API from Amazon Lightsail — 1 operation(s) for bundles.
  name: Amazon Lightsail Bundles API
  phrasing_intents:
  - id: GetBundles
    intent: List instance plans (bundles)
    question: What instance sizes and monthly prices can I choose from?
  phrasing_ops: 1
  slug: amazon-lightsail-bundles-api
- baseURL: https://lightsail.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Certificates API from Amazon Lightsail — 7 operation(s) for certificates.
  name: Amazon Lightsail Certificates API
  phrasing_intents:
  - id: AttachLoadBalancerTlsCertificate
    intent: Attach a TLS certificate to a load balancer
    question: How do I enable HTTPS on my load balancer with a validated certificate?
  - id: CreateCertificate
    intent: Request a certificate for a CDN or container service
    question: How do I get an SSL certificate for my Lightsail distribution's custom domain?
  - id: CreateLoadBalancerTlsCertificate
    intent: Create a TLS certificate on a load balancer
    question: How do I create an SSL certificate specifically for a Lightsail load balancer?
  - id: DeleteCertificate
    intent: Delete a CDN/container certificate
    question: How do I delete a certificate I made for my CDN distribution?
  - id: DeleteLoadBalancerTlsCertificate
    intent: Delete a load balancer's TLS certificate
    question: How do I remove a TLS certificate from my load balancer?
  - id: GetCertificates
    intent: List CDN and container certificates
    question: Which of my distribution certificates are still pending validation?
  - id: GetLoadBalancerTlsCertificates
    intent: List a load balancer's TLS certificates
    question: What certificates are associated with my load balancer?
  phrasing_ops: 7
  slug: amazon-lightsail-certificates-api
- baseURL: https://lightsail.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Contact Methods API from Amazon Lightsail — 4 operation(s) for contact methods.
  name: Amazon Lightsail Contact Methods API
  phrasing_intents:
  - id: CreateContactMethod
    intent: Add an email or SMS contact method
    question: How do I get Lightsail notifications sent to my phone by text?
  - id: DeleteContactMethod
    intent: Remove a notification contact method
    question: How do I stop getting Lightsail alerts by SMS?
  - id: GetContactMethods
    intent: List notification contact methods
    question: Which email and phone contacts get my Lightsail notifications?
  - id: SendContactMethodVerification
    intent: Send a verification to an email contact
    question: How do I verify the email address I added for notifications?
  phrasing_ops: 4
  slug: amazon-lightsail-contact-methods-api
- baseURL: https://lightsail.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Container Services API from Amazon Lightsail — 10 operation(s) for container services.
  name: Amazon Lightsail Container Services API
  phrasing_intents:
  - id: GetContainerAPIMetadata
    intent: Get Lightsail container API metadata
    question: Which version of the lightsailctl plugin is current?
  - id: CreateContainerServiceRegistryLogin
    intent: Get temporary Docker registry login credentials
    question: How do I log my local Docker in so I can push images to a container service?
  - id: GetContainerServicePowers
    intent: List container service power sizes
    question: What power levels (CPU and memory) can a container service use?
  - id: CreateContainerService
    intent: Create a container service
    question: How do I create a Lightsail container service to run my Docker app?
  - id: GetContainerServices
    intent: List container services or get one
    question: Which container services am I running and what state are they in?
  - id: DeleteContainerService
    intent: Delete a container service
    question: How do I tear down a container service I'm done with?
  - id: UpdateContainerService
    intent: Change a container service's power, scale or domains
    question: How do I scale my container service to more nodes?
  - id: GetContainerLog
    intent: Read a container's log events
    question: How do I see the logs from a container in my service?
  phrasing_ops: 14
  slug: amazon-lightsail-container-services-api
- baseURL: https://lightsail.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Cost Estimate API from Amazon Lightsail — 1 operation(s) for cost estimate.
  name: Amazon Lightsail Cost Estimate API
  phrasing_intents:
  - id: GetCostEstimate
    intent: Estimate a resource's cost over a time range
    question: How much has my Lightsail instance cost this month so far?
  phrasing_ops: 1
  slug: amazon-lightsail-cost-estimate-api
- baseURL: https://lightsail.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Distributions API from Amazon Lightsail — 11 operation(s) for distributions.
  name: Amazon Lightsail Distributions API
  phrasing_intents:
  - id: AttachCertificateToDistribution
    intent: Attach a certificate to a CDN distribution
    question: How do I use my custom domain with HTTPS on a Lightsail CDN distribution?
  - id: CreateDistribution
    intent: Create a CDN distribution
    question: How do I put a CDN in front of my Lightsail instance or bucket?
  - id: DeleteDistribution
    intent: Delete a CDN distribution
    question: How do I delete a CDN distribution I no longer need?
  - id: DetachCertificateFromDistribution
    intent: Remove the certificate from a distribution
    question: How do I stop using my custom-domain certificate on a distribution?
  - id: GetDistributionBundles
    intent: List CDN distribution plans
    question: What CDN plans are available and how much transfer do they include?
  - id: GetDistributionLatestCacheReset
    intent: Check the last CDN cache reset
    question: When was my distribution's cache last cleared?
  - id: GetDistributionMetricData
    intent: Get traffic metrics for a distribution
    question: How many requests is my CDN distribution serving?
  - id: GetDistributions
    intent: List CDN distributions
    question: What CDN distributions do I have and what domains do they serve?
  phrasing_ops: 11
  slug: amazon-lightsail-distributions-api
- baseURL: https://lightsail.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Domains API from Amazon Lightsail — 7 operation(s) for domains.
  name: Amazon Lightsail Domains API
  phrasing_intents:
  - id: CreateDomain
    intent: Create a DNS zone for a domain
    question: How do I manage my domain's DNS in Lightsail?
  - id: CreateDomainEntry
    intent: Add a DNS record to a domain
    question: How do I add an A record pointing my domain at an instance?
  - id: DeleteDomain
    intent: Delete a domain's DNS zone
    question: How do I delete a domain and all of its DNS records?
  - id: DeleteDomainEntry
    intent: Delete one DNS record
    question: How do I remove a single DNS record from my domain?
  - id: GetDomain
    intent: Get a domain and its DNS records
    question: What DNS records are set on one of my domains?
  - id: GetDomains
    intent: List all DNS zones in the account
    question: Which domains are managed in my Lightsail account?
  - id: UpdateDomainEntry
    intent: Change an existing DNS record
    question: How do I point an existing A record at a new IP address?
  phrasing_ops: 7
  slug: amazon-lightsail-domains-api
- baseURL: https://lightsail.us-east-1.amazonaws.com
  baseurl_source: declared
  description: Lightsail virtual server instance management
  name: Amazon Lightsail Instances API
  phrasing_intents:
  - id: CreateInstances
    intent: Create instances via the REST-style /instances path
    question: Can I create instances by POSTing to the /instances resource path?
  - id: GetInstances
    intent: List instances via the REST-style /instances path
    question: Is there a plain GET /instances resource path for listing my servers?
  - id: GetInstance
    intent: Get an instance via the REST-style /instances path
    question: Can I fetch one server with a plain GET on its /instances resource path?
  - id: DeleteInstance
    intent: Delete an instance via an HTTP DELETE on /instances
    question: Can I remove a server with an HTTP DELETE on its /instances path?
  - id: StartInstance
    intent: Start an instance via the REST-style /start path
    question: Can I boot a server by POSTing to its /start sub-path?
  - id: StopInstance
    intent: Stop an instance via the REST-style /stop path
    question: Can I shut down a server by POSTing to its /stop sub-path?
  - id: CloseInstancePublicPorts
    intent: Close a firewall port on an instance
    question: How do I close port 22 to the public on my instance?
  - id: postLsApi20161128CreateInstances
    intent: Launch new instances from a blueprint
    question: How do I launch a new Lightsail server running WordPress or Ubuntu?
  phrasing_ops: 22
  slug: amazon-lightsail-instances-api
- baseURL: https://lightsail.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Load Balancers API from Amazon Lightsail — 9 operation(s) for load balancers.
  name: Amazon Lightsail Load Balancers API
  phrasing_intents:
  - id: AttachInstancesToLoadBalancer
    intent: Add instances to a load balancer
    question: How do I put my web servers behind a Lightsail load balancer?
  - id: CreateLoadBalancer
    intent: Create a load balancer
    question: How do I create a load balancer for my Lightsail instances?
  - id: DeleteLoadBalancer
    intent: Delete a load balancer
    question: How do I delete a load balancer I no longer need?
  - id: DetachInstancesFromLoadBalancer
    intent: Remove instances from a load balancer
    question: How do I take an instance out of the load balancer for maintenance?
  - id: GetLoadBalancer
    intent: Get one load balancer's details
    question: Are the instances behind my load balancer healthy?
  - id: GetLoadBalancerMetricData
    intent: Get health metrics for a load balancer
    question: How many requests is my load balancer handling?
  - id: GetLoadBalancerTlsPolicies
    intent: List load balancer TLS security policies
    question: Which TLS security policies can I apply to a load balancer?
  - id: GetLoadBalancers
    intent: List all load balancers
    question: What load balancers are in my account?
  phrasing_ops: 9
  slug: amazon-lightsail-load-balancers-api
- baseURL: https://lightsail.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Operations API from Amazon Lightsail — 3 operation(s) for operations.
  name: Amazon Lightsail Operations API
  phrasing_intents:
  - id: GetOperation
    intent: Check the status of one operation
    question: Did the request I just made finish successfully?
  - id: GetOperations
    intent: List all recent operations in the account
    question: What changes have been made in my Lightsail account recently?
  - id: GetOperationsForResource
    intent: List operations for one resource
    question: What has happened to a specific instance or static IP?
  phrasing_ops: 3
  slug: amazon-lightsail-operations-api
- baseURL: https://lightsail.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Regions API from Amazon Lightsail — 1 operation(s) for regions.
  name: Amazon Lightsail Regions API
  phrasing_intents:
  - id: GetRegions
    intent: List Lightsail regions and zones
    question: Which AWS regions is Lightsail available in?
  phrasing_ops: 1
  slug: amazon-lightsail-regions-api
- baseURL: https://lightsail.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Relational Databases API from Amazon Lightsail — 22 operation(s) for relational databases.
  name: Amazon Lightsail Relational Databases API
  phrasing_intents:
  - id: CreateRelationalDatabase
    intent: Create a managed database
    question: How do I spin up a managed MySQL or PostgreSQL database in Lightsail?
  - id: CreateRelationalDatabaseFromSnapshot
    intent: Restore a database from a snapshot or point in time
    question: How do I restore a database from one of its snapshots?
  - id: CreateRelationalDatabaseSnapshot
    intent: Take a snapshot of a database
    question: How can I back up my managed database right now?
  - id: DeleteRelationalDatabase
    intent: Delete a managed database
    question: How do I delete a database but keep a final snapshot?
  - id: DeleteRelationalDatabaseSnapshot
    intent: Delete a database snapshot
    question: How do I remove an old database snapshot?
  - id: GetRelationalDatabase
    intent: Get one database's details
    question: What's the endpoint and port of my managed database?
  - id: GetRelationalDatabaseBlueprints
    intent: List database engines and versions
    question: Which MySQL and PostgreSQL versions can I create?
  - id: GetRelationalDatabaseBundles
    intent: List database plans
    question: What database sizes and monthly prices are offered?
  phrasing_ops: 22
  slug: amazon-lightsail-relational-databases-api
- baseURL: https://lightsail.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Setup API from Amazon Lightsail — 1 operation(s) for setup.
  name: Amazon Lightsail Setup API
  phrasing_intents:
  - id: GetSetupHistory
    intent: Review recent HTTPS setup attempts on an instance
    question: Why did my HTTPS setup on the instance fail?
  phrasing_ops: 1
  slug: amazon-lightsail-setup-api
- baseURL: https://lightsail.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Snapshots API from Amazon Lightsail — 15 operation(s) for snapshots.
  name: Amazon Lightsail Snapshots API
  phrasing_intents:
  - id: CopySnapshot
    intent: Copy a snapshot, even to another region
    question: How do I copy an instance snapshot to another AWS region?
  - id: CreateDiskFromSnapshot
    intent: Restore a disk from a disk snapshot
    question: How do I restore a block storage disk from a snapshot?
  - id: CreateDiskSnapshot
    intent: Take a snapshot of a block storage disk
    question: How do I back up a block storage disk?
  - id: CreateInstanceSnapshot
    intent: Take a snapshot of an instance
    question: How do I back up my whole Lightsail server before an upgrade?
  - id: CreateInstancesFromSnapshot
    intent: Launch instances from an instance snapshot
    question: How do I restore a server from a snapshot onto a bigger plan?
  - id: DeleteAutoSnapshot
    intent: Delete an automatic snapshot by date
    question: How do I delete one day's automatic snapshot of an instance?
  - id: DeleteDiskSnapshot
    intent: Delete a manual disk snapshot
    question: How do I delete an old block storage disk snapshot?
  - id: DeleteInstanceSnapshot
    intent: Delete a manual instance snapshot
    question: How do I delete an instance snapshot to stop paying for it?
  phrasing_ops: 15
  slug: amazon-lightsail-snapshots-api
- baseURL: https://lightsail.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Static IPs API from Amazon Lightsail — 6 operation(s) for static ips.
  name: Amazon Lightsail Static IPs API
  phrasing_intents:
  - id: AllocateStaticIp
    intent: Reserve a new static IP address
    question: How do I get a fixed public IP that doesn't change on reboot?
  - id: AttachStaticIp
    intent: Attach a static IP to an instance
    question: How do I assign my static IP to an instance?
  - id: DetachStaticIp
    intent: Detach a static IP from its instance
    question: How do I unassign a static IP but keep it reserved?
  - id: GetStaticIp
    intent: Get details of one static IP
    question: Which instance is a given static IP attached to?
  - id: GetStaticIps
    intent: List all static IPs
    question: What static IP addresses do I have reserved?
  - id: ReleaseStaticIp
    intent: Release a static IP address
    question: How do I give back a static IP I no longer need?
  phrasing_ops: 6
  slug: amazon-lightsail-static-ips-api
- baseURL: https://lightsail.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Tags API from Amazon Lightsail — 2 operation(s) for tags.
  name: Amazon Lightsail Tags API
  phrasing_intents:
  - id: TagResource
    intent: Add tags to a resource
    question: How do I tag my Lightsail resources by project or cost center?
  - id: UntagResource
    intent: Remove tags from a resource
    question: How can I remove a tag key from a Lightsail resource?
  phrasing_ops: 2
  slug: amazon-lightsail-tags-api
- baseURL: https://lightsail.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The blockstorage API from Amazon Lightsail — 6 operation(s) for blockstorage.
  name: Amazon Lightsail Blockstorage API
  phrasing_intents:
  - id: AttachDisk
    intent: Attach a block storage disk to an instance
    question: How do I add extra storage to my Lightsail instance?
  - id: CreateDisk
    intent: Create a new empty block storage disk
    question: How do I create a new blank SSD disk for an instance?
  - id: DeleteDisk
    intent: Delete a block storage disk
    question: How do I permanently delete a disk I no longer use?
  - id: DetachDisk
    intent: Detach a disk from its instance
    question: How do I unplug a disk from an instance without deleting it?
  - id: GetDisk
    intent: Get details of one block storage disk
    question: What size and state is a particular disk in?
  - id: GetDisks
    intent: List all block storage disks
    question: Which block storage disks do I have in this region?
  phrasing_ops: 6
  slug: amazon-lightsail-blockstorage-api
- baseURL: https://lightsail.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Keypairs API from Amazon Lightsail — 6 operation(s) for keypairs.
  name: Amazon Lightsail Keypairs API
  phrasing_intents:
  - id: CreateKeyPair
    intent: Generate a new SSH key pair
    question: How do I create a new SSH key pair for my instances?
  - id: DeleteKeyPair
    intent: Delete an SSH key pair
    question: How do I delete an SSH key pair I no longer use?
  - id: DownloadDefaultKeyPair
    intent: Download the regional default key pair
    question: Where do I get the default SSH private key for this region?
  - id: GetKeyPair
    intent: Get details of one key pair
    question: What's the fingerprint of a particular key pair?
  - id: GetKeyPairs
    intent: List all SSH key pairs
    question: Which SSH key pairs exist in my account?
  - id: ImportKeyPair
    intent: Import an existing public SSH key
    question: How do I use my own existing SSH key with Lightsail?
  phrasing_ops: 6
  slug: amazon-lightsail-keypairs-api
artifact_total: 54
collections:
- collection_type: postman
  name: Amazon Lightsail Instances API
  slug: postman-amazon-lightsail-instances-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Lightsail Instances API
  slug: open-amazon-lightsail-instances-api
- collection_type: open
  name: Amazon Lightsail API
  slug: open-amazon-lightsail
- collection_type: open
  name: Amazon Lightsail API
  slug: open-openapi
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/overlays/amazon-lightsail-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/amazon-lightsail-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-lightsail/overview
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/agentic-access/amazon-lightsail-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-lightsail-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/security/amazon-lightsail-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/amazon-lightsail-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/security/amazon-lightsail-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-lightsail-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/security/amazon-lightsail-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amazon-lightsail-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/authentication/amazon-lightsail-authentication.yml
  title: ''
  type: Authentication
  url: authentication/amazon-lightsail-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/lightsail/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/lightsail/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/compute/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://lightsail.aws.amazon.com/
- group: start
  title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- group: start
  title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: other
  title: ''
  type: knowledge-center
  url: https://repost.aws/knowledge-center
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-lightsail
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/security/amazon-lightsail-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/amazon-lightsail-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/rules/amazon-lightsail-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/amazon-lightsail-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/vocabulary/amazon-lightsail-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-lightsail-vocabulary.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/lightsail/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/Welcome.html
- group: start
  title: ''
  type: GettingStarted
  url: https://aws.amazon.com/lightsail/getting-started/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/lightsail/pricing/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/smithy/amazon-lightsail-2016-11-28.json
  title: ''
  type: Smithy
  url: smithy/amazon-lightsail-2016-11-28.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/packages/amazon-lightsail-packages.yml
  title: ''
  type: Packages
  url: packages/amazon-lightsail-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/packages/amazon-lightsail-packages.yml
  title: ''
  type: SDKs
  url: packages/amazon-lightsail-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/cli/amazon-lightsail-cli.yml
  title: ''
  type: CLI
  url: cli/amazon-lightsail-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/well-known/amazon-lightsail-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/amazon-lightsail-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/well-known/amazon-lightsail-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/amazon-lightsail-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/mcp/amazon-lightsail-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/amazon-lightsail-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/mcp/amazon-lightsail-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/amazon-lightsail-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/llms/amazon-lightsail-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/amazon-lightsail-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/conformance/amazon-lightsail-conformance.yml
  title: ''
  type: Conformance
  url: conformance/amazon-lightsail-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/errors/amazon-lightsail-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/amazon-lightsail-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/lifecycle/amazon-lightsail-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/amazon-lightsail-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/conventions/amazon-lightsail-conventions.yml
  title: ''
  type: Conventions
  url: conventions/amazon-lightsail-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/changelog/amazon-lightsail-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/amazon-lightsail-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/data-model/amazon-lightsail-data-model.yml
  title: ''
  type: DataModel
  url: data-model/amazon-lightsail-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/plans/amazon-lightsail-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/amazon-lightsail-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/rate-limits/amazon-lightsail-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/amazon-lightsail-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/finops/amazon-lightsail-finops.yml
  title: ''
  type: FinOps
  url: finops/amazon-lightsail-finops.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/examples/amazon-lightsail-instance-example.json
  title: ''
  type: Examples
  url: examples/amazon-lightsail-instance-example.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/postman/amazon-lightsail-instances-api.postman_collection.json
  title: ''
  type: Postman
  url: postman/amazon-lightsail-instances-api.postman_collection.json
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://aws.amazon.com/security/
created: '2024-01-15'
description: Amazon Lightsail is a virtual private server (VPS) provider and is the easiest way to get started with AWS for developers, small businesses, students, and other users who need a solution to build and host their applications on cloud. Lightsail provides developers compute, storage, and networking capacity and capabilities to deploy and manage websites and web applications in the cloud.
examples:
- key_count: 7
  name: Amazon Lightsail Instance Example
  slug: amazon-lightsail-instance-example
features:
- description: Launch virtual servers with pre-configured Linux/Windows environments in minutes.
  name: Simple Virtual Servers
- description: Deploy managed databases (MySQL, PostgreSQL) without server management.
  name: Managed Databases
- description: Deploy containerized applications using Lightsail container services.
  name: Containers
- description: Create CloudFront-powered CDN distributions for faster content delivery.
  name: CDN Distributions
- description: Fixed monthly pricing with no surprise bills including compute, storage, and data transfer.
  name: Predictable Pricing
finops:
- name: Amazon Lightsail Finops
  service_category: API
  slug: amazon-lightsail-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Connect Lightsail instances to S3 buckets for object storage.
  name: Amazon S3
- description: Distribute Lightsail content globally via CloudFront CDN distributions.
  name: AWS CloudFront
- description: Manage DNS for Lightsail resources using Route 53.
  name: Amazon Route 53
- description: Migrate Lightsail instances to EC2 when you need more control.
  name: Amazon EC2
json_schemas:
- name: Instance
  property_count: 7
  slug: amazon-lightsail-instance
json_structures:
- name: Amazon Lightsail Instance Structure
  property_count: 7
  slug: amazon-lightsail-instance-structure
jsonld:
- class_count: 1
  name: Amazon Lightsail Context
  property_count: 7
  slug: amazon-lightsail-context
layout: provider
mcp_servers:
- description: ''
  name: Amazon Lightsail MCP Server
  slug: amazon-lightsail-mcp-server
modified: '2026-09-17'
name: Amazon Lightsail
nav: Providers
network: true
overview: 'Amazon Lightsail publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Account API, Alarms API, Blueprints API, and 19 more. Tagged areas include Cloud, Compute, Virtual Private Server, Hosting, and Containers.


  The Amazon Lightsail catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Lightsail''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 46 more developer resources.'
plans:
- name: Amazon Lightsail Plans Pricing
  plan_count: 100
  slug: amazon-lightsail-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Amazon Lightsail Rate Limits
  slug: amazon-lightsail-rate-limits
rules:
- effective_rule_count: 3
  extends: []
  name: Amazon Lightsail API Rules
  rule_count: 3
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 2
  slug: amazon-lightsail-jsonschema-spectral-rules
- effective_rule_count: 64
  extends:
  - spectral:oas
  name: Amazon Lightsail API Rules
  rule_count: 23
  severity_counts:
    error: 9
    hint: 0
    info: 0
    warn: 14
  slug: amazon-lightsail-spectral-rules
score:
  band: exemplar
  composite: 75.3
  coverage:
    artifact_dirs: 32
    catalog_earned: 74.4
    catalog_earned_first_party: 12.0
    catalog_gap: 40.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 100.0
    contract_governance: 45.5
    contract_quality: 65.6
    developer_ergonomics: 81.5
    discoverability: 80.0
    operational_transparency: 44.7
  previous_composite: 74.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/screenshots/amazon-lightsail-2026-06-20T171728.png
security:
- kind: authentication
  name: Amazon Lightsail Authentication
  slug: amazon-lightsail-authentication
  summary_line: sigv4 · 1 scheme
- kind: domain-security
  name: Amazon Lightsail Domain Security
  slug: amazon-lightsail-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Lightsail Vulnerability Disclosure
  slug: amazon-lightsail-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Lightsail Trust Center
  slug: amazon-lightsail-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-lightsail
tags:
- Cloud
- Compute
- Virtual Private Server
- Hosting
- Containers
- Database
- Storage
- CDN
- Networking
- Infrastructure
- DevOps
use_cases:
- description: Host WordPress sites with pre-configured LAMP stacks at low, predictable cost.
  name: WordPress Hosting
- description: Develop and test web applications on simple cloud infrastructure.
  name: Web Application Development
- description: Power small business websites with affordable, managed cloud hosting.
  name: Small Business Websites
website: https://aws.amazon.com/lightsail/
---
