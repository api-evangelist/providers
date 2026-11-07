---
access_model:
  confidence: high
  label: Paid licence · Self-serve signup · 15-day free trial
  onboarding: self-serve
  pricing: paid
  public: true
  source:
  - plans
  - pricing
  - authentication
  - sandbox
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 54.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 37
  human_in_the_loop: 0
  name: Cpanel Agentic Access
  operation_count: 1282
  slug: cpanel-agentic-access
  summary_line: 1282 operations · 37 acting
api_count: 2
apis:
- description: cPanel API 2 is the legacy XML/JSON API for cPanel-user operations. cPanel marks the whole system deprecated on every function page and directs new development to UAPI, but it remains supported for ba
  name: cPanel API 2 (Legacy)
  slug: cpanel-api-2
- description: The Manage2 API automates cPanel LICENCE management for cPanel partners and direct licence holders — activating, reactivating, transferring and cancelling licences, changing a licence's IP address, ma
  name: Manage2 API
  slug: manage2
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The 360 Monitoring module for WHM API 1.
  name: cPanel 360 Monitoring API
  slug: cpanel-360-monitoring-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: Accounts Creation / Accounts
  name: cPanel Account Creation API
  slug: cpanel-account-creation-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Account Enhancement module for UAPI.
  name: cPanel Account Enhancements API
  slug: cpanel-account-enhancements-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: Accounts / Account Management
  name: cPanel Account Management API
  slug: cpanel-account-management-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Account Restoration module for WHM API 1.
  name: cPanel Account Restoration API
  slug: cpanel-account-restoration-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Accounts module for WHM API 1.
  name: cPanel Accounts API
  slug: cpanel-accounts-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The AddonDomain module for UAPI.
  name: cPanel Addon Domain API
  slug: cpanel-addondomain-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Server Administration module for WHM API 1.
  name: cPanel API Execution API
  slug: cpanel-api-execution-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: API Development Tools / Applications
  name: cPanel Applications API
  slug: cpanel-applications-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Authentication module for WHM API 1.
  name: cPanel Authentication API
  slug: cpanel-authentication-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Backup module for UAPI.
  name: cPanel Backup API
  slug: cpanel-backup-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Backups module for WHM API 1.
  name: cPanel Backups API
  slug: cpanel-backups-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: Accounts / Bandwidth and Disk Quotas
  name: cPanel Bandwidth and Disk Quotas API
  slug: cpanel-bandwidth-and-disk-quotas-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Bandwidth module for UAPI.
  name: cPanel Bandwidth API
  slug: cpanel-bandwidth-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Batch module for UAPI.
  name: cPanel Batch API
  slug: cpanel-batch-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The BlockIP module for UAPI.
  name: cPanel Block IP API
  slug: cpanel-blockip-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The BoxTrapper module for UAPI.
  name: cPanel Box Trapper API
  slug: cpanel-boxtrapper-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Branding module for UAPI.
  name: cPanel Branding API
  slug: cpanel-branding-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The CacheBuster module for UAPI.
  name: cPanel Cache Buster API
  slug: cpanel-cachebuster-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Chkservd module for UAPI.
  name: cPanel Chkservd API
  slug: cpanel-chkservd-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Chrome module for UAPI.
  name: cPanel Chrome API
  slug: cpanel-chrome-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The ClamScanner module provides methods for ClamAV® virus scans and disinfection.
  name: cPanel Clam Scanner API
  slug: cpanel-clamscanner-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: Server Administration / Configurations
  name: cPanel Configurations API
  slug: cpanel-configurations-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The cPanel Analytics module for WHM API 1.
  name: cPanel cPanel Analytics API
  slug: cpanel-cpanel-analytics-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: Server Information / cPanel Server Information
  name: cPanel cPanel Server Information API
  slug: cpanel-cpanel-server-information-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The cPGreyList module for UAPI.
  name: cPanel C P Grey List API
  slug: cpanel-cpgreylist-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The cPHulk module for WHM API 1.
  name: cPanel C P Hulk API
  slug: cpanel-cphulk-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The CSVImport module for UAPI.
  name: cPanel CSV Import API
  slug: cpanel-csvimport-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Customizations module for WHM API 1.
  name: cPanel Customizations API
  slug: cpanel-customizations-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Databases module for WHM API 1.
  name: cPanel Databases API
  slug: cpanel-databases-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The DAV module for UAPI.
  name: cPanel DAV API
  slug: cpanel-dav-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The DCV module for UAPI.
  name: cPanel DCV API
  slug: cpanel-dcv-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The DirectoryIndexes module for UAPI.
  name: cPanel Directory Indexes API
  slug: cpanel-directoryindexes-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The DirectoryPrivacy module for UAPI.
  name: cPanel Directory Privacy API
  slug: cpanel-directoryprivacy-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The DirectoryProtection module for UAPI.
  name: cPanel Directory Protection API
  slug: cpanel-directoryprotection-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The DNS module for UAPI.
  name: cPanel DNS API
  slug: cpanel-dns-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The DNSSEC module for UAPI.
  name: cPanel DNSSEC API
  slug: cpanel-dnssec-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Domain module for UAPI.
  name: cPanel Domain API
  slug: cpanel-domain-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: Accounts / Domain Domain Information
  name: cPanel Domain Information API
  slug: cpanel-domain-information-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The DomainInfo module for UAPI.
  name: cPanel Domain Info API
  slug: cpanel-domaininfo-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The DomainRecommendations module for UAPI.
  name: cPanel Domain Recommendations API
  slug: cpanel-domainrecommendations-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The DynamicDNS module for UAPI.
  name: cPanel Dynamic DNS API
  slug: cpanel-dynamicdns-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The EA4 module for UAPI.
  name: cPanel EA4 API
  slug: cpanel-ea4-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The EasyApache module for WHM API 1.
  name: cPanel Easy Apache API
  slug: cpanel-easyapache-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Email module for UAPI.
  name: cPanel Email API
  slug: cpanel-email-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: DNS / Email DNS Settings
  name: cPanel Email DNS Settings API
  slug: cpanel-email-dns-settings-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The EmailAuth module for UAPI.
  name: cPanel Email Auth API
  slug: cpanel-emailauth-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The ExternalAuthentication module for UAPI.
  name: cPanel External Authentication API
  slug: cpanel-externalauthentication-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The ExtractInfo module for UAPI.
  name: cPanel Extract Info API
  slug: cpanel-extractinfo-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Features module for UAPI.
  name: cPanel Features API
  slug: cpanel-features-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: cPanel Account Backups / File Restoration
  name: cPanel File Restoration API
  slug: cpanel-file-restoration-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Fileman module for UAPI.
  name: cPanel Fileman API
  slug: cpanel-fileman-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The FTP module for UAPI.
  name: cPanel Ftp API
  slug: cpanel-ftp-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The GPG module for UAPI.
  name: cPanel GPG API
  slug: cpanel-gpg-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Greylisting module for WHM API 1.
  name: cPanel Greylisting API
  slug: cpanel-greylisting-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The ImageManager module for UAPI.
  name: cPanel Image Manager API
  slug: cpanel-imagemanager-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The InProductSurvey module for cPanel UAPI.
  name: cPanel In Product Survey API
  slug: cpanel-inproductsurvey-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Integration module for UAPI.
  name: cPanel Integration API
  slug: cpanel-integration-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The IP Addresses module for WHM API 1.
  name: cPanel IP Addresses API
  slug: cpanel-ip-addresses-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The LangPHP module for UAPI.
  name: cPanel Lang PHP API
  slug: cpanel-langphp-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The LastLogin module for UAPI.
  name: cPanel Last Login API
  slug: cpanel-lastlogin-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Locale module for UAPI.
  name: cPanel Locale API
  slug: cpanel-locale-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The LogManager module for UAPI.
  name: cPanel Log Manager API
  slug: cpanel-logmanager-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Mail module for WHM API 1.
  name: cPanel Mail API
  slug: cpanel-mail-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Mailboxes module for UAPI.
  name: cPanel Mailboxes API
  slug: cpanel-mailboxes-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Market module for UAPI.
  name: cPanel Market API
  slug: cpanel-market-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Mime module for UAPI.
  name: cPanel Mime API
  slug: cpanel-mime-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The ModSecurity module for UAPI.
  name: cPanel Mod Security API
  slug: cpanel-modsecurity-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Mysql module for UAPI.
  name: cPanel Mysql API
  slug: cpanel-mysql-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The NGINX Manager module for WHM API 1.
  name: cPanel NGINX Manager API
  slug: cpanel-nginx-manager-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The NginxCaching module for UAPI.
  name: cPanel Nginx Caching API
  slug: cpanel-nginxcaching-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Notifications module for UAPI.
  name: cPanel Notifications API
  slug: cpanel-notifications-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Packages module for WHM API 1.
  name: cPanel Packages API
  slug: cpanel-packages-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Park module for UAPI.
  name: cPanel Park API
  slug: cpanel-park-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Parser module for UAPI.
  name: cPanel Parser API
  slug: cpanel-parser-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The PassengerApps module for UAPI.
  name: cPanel Passenger Apps API
  slug: cpanel-passengerapps-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The PasswdStrength module for UAPI.
  name: cPanel Passwd Strength API
  slug: cpanel-passwdstrength-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: Accounts / Passwords
  name: cPanel Passwords API
  slug: cpanel-passwords-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Personalization module for UAPI.
  name: cPanel Personalization API
  slug: cpanel-personalization-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: PHP recommendations
  name: cPanel PHP API
  slug: cpanel-php-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: Web Server Configuration / PHP-FPM
  name: cPanel PHP FPM API
  slug: cpanel-php-fpm-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The plugin-based features module for WHM API 1.
  name: cPanel Plugin-Based Features API
  slug: cpanel-plugin-based-features-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Plugins module for UAPI.
  name: cPanel Plugins API
  slug: cpanel-plugins-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Postgresql module for UAPI.
  name: cPanel Postgresql API
  slug: cpanel-postgresql-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Pushbullet module for UAPI.
  name: cPanel Pushbullet API
  slug: cpanel-pushbullet-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Quota module for UAPI.
  name: cPanel Quota API
  slug: cpanel-quota-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Resellers module for UAPI.
  name: cPanel Resellers API
  slug: cpanel-resellers-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The RPM module for WHM API 1.
  name: cPanel RPM API
  slug: cpanel-rpm-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Script Hooks module for WHM API 1.
  name: cPanel Script Hooks API
  slug: cpanel-script-hooks-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Security module for WHM API 1.
  name: cPanel Security API
  slug: cpanel-security-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Server Administration module for WHM API 1.
  name: cPanel Server Administration API
  slug: cpanel-server-administration-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The ServiceProxy module for UAPI.
  name: cPanel Service Proxy API
  slug: cpanel-serviceproxy-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: Server Administration / Services
  name: cPanel Services API
  slug: cpanel-services-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Session module for UAPI.
  name: cPanel Session API
  slug: cpanel-session-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Sitejet module for UAPI.
  name: cPanel Sitejet API
  slug: cpanel-sitejet-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The SiteQuality module for UAPI.
  name: cPanel Site Quality API
  slug: cpanel-sitequality-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The SpamAssassin module for UAPI.
  name: cPanel Spam Assassin API
  slug: cpanel-spamassassin-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The SSH module for UAPI.
  name: cPanel SSH API
  slug: cpanel-ssh-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: Authentication / SSH Keys and Connections
  name: cPanel SSH Keys and Connections API
  slug: cpanel-ssh-keys-and-connections-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The SSL module for UAPI.
  name: cPanel SSL API
  slug: cpanel-ssl-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Stats module for UAPI.
  name: cPanel Stats API
  slug: cpanel-stats-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The StatsBar module for UAPI.
  name: cPanel Stats Bar API
  slug: cpanel-statsbar-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The StatsManager module for UAPI.
  name: cPanel Stats Manager API
  slug: cpanel-statsmanager-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: Server Administration / Account Management
  name: cPanel Styles API
  slug: cpanel-styles-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The SubDomain module for cPanel UAPI.
  name: cPanel Subdomains API
  slug: cpanel-subdomains-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Support Tickets module for WHM API 1.
  name: cPanel Support Tickets API
  slug: cpanel-support-tickets-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: Accounts / Suspensions
  name: cPanel Suspensions API
  slug: cpanel-suspensions-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Team Roles module for UAPI.
  name: cPanel Team Roles API
  slug: cpanel-team-roles-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Team User module for UAPI.
  name: cPanel Team Users API
  slug: cpanel-team-users-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Themes module for UAPI.
  name: cPanel Themes API
  slug: cpanel-themes-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Tokens module for UAPI.
  name: cPanel Tokens API
  slug: cpanel-tokens-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Transfers module for WHM API 1.
  name: cPanel Transfers API
  slug: cpanel-transfers-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Trash module for UAPI.
  name: cPanel Trash API
  slug: cpanel-trash-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: Server Administration / Updates
  name: cPanel Updates API
  slug: cpanel-updates-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The UserManager module for UAPI.
  name: cPanel User Manager API
  slug: cpanel-usermanager-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Users module for UAPI.
  name: cPanel Users API
  slug: cpanel-users-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Variables module for UAPI.
  name: cPanel Variables API
  slug: cpanel-variables-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The VersionControlDeployment module for UAPI.
  name: cPanel Version Control Deployment API
  slug: cpanel-versioncontroldeployment-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The Web Log Retention module for WHM API 1.
  name: cPanel Web Log Retention API
  slug: cpanel-web-log-retention-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The WebApp module for UAPI.
  name: cPanel Web App API
  slug: cpanel-webapp-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The WebDisk module for UAPI.
  name: cPanel Web Disk API
  slug: cpanel-webdisk-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The WebmailApps module for UAPI.
  name: cPanel Webmail Apps API
  slug: cpanel-webmailapps-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The WebProsMCP module for UAPI.
  name: cPanel Web Pros MCP API
  slug: cpanel-webprosmcp-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The WebVhosts module for UAPI.
  name: cPanel Web Vhosts API
  slug: cpanel-webvhosts-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: Security / WHM Access
  name: cPanel WHM Access API
  slug: cpanel-whm-access-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The WordPressBackup module for UAPI.
  name: cPanel Word Press Backup API
  slug: cpanel-wordpressbackup-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The WordPressRestore module for UAPI.
  name: cPanel Word Press Restore API
  slug: cpanel-wordpressrestore-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The WordPressSite module for UAPI.
  name: cPanel Word Press Site API
  slug: cpanel-wordpresssite-api
- baseURL: https://{host}:2083/execute
  baseurl_source: declared
  description: The ZoneEdit module for UAPI.
  name: cPanel Zone Edit API
  slug: cpanel-zoneedit-api
- baseURL: https://{host}:2083/json-api/cpanel
  baseurl_source: declared
  description: The BackupInfo module for UAPI.
  name: cPanel Backup Info API
  slug: cpanel-backup-info-api
- baseURL: https://{host}:2083/json-api/cpanel
  baseurl_source: declared
  description: The CCS module for UAPI.
  name: cPanel C Cs API
  slug: cpanel-c-cs-api
- baseURL: https://{host}:2083/json-api/cpanel
  baseurl_source: declared
  description: The ContactInformation module for UAPI.
  name: cPanel Contact Information API
  slug: cpanel-contact-information-api
- baseURL: https://{host}:2083/json-api/cpanel
  baseurl_source: declared
  description: The Contactus module for UAPI.
  name: cPanel Contact Us API
  slug: cpanel-contact-us-api
- baseURL: https://{host}:2083/json-api/cpanel
  baseurl_source: declared
  description: The DomainLookup module for UAPI.
  name: cPanel Domain Lookup API
  slug: cpanel-domain-lookup-api
- baseURL: https://{host}:2083/json-api/cpanel
  baseurl_source: declared
  description: The KnownHosts module for UAPI.
  name: cPanel Known Hosts API
  slug: cpanel-known-hosts-api
- baseURL: https://{host}:2083/json-api/cpanel
  baseurl_source: declared
  description: The ResourceUsage module for UAPI.
  name: cPanel Resource Usage API
  slug: cpanel-resource-usage-api
- baseURL: https://{host}:2083/json-api/cpanel
  baseurl_source: declared
  description: The ServerInformation module for UAPI.
  name: cPanel Server Information API
  slug: cpanel-server-information-api
- baseURL: https://{host}:2083/json-api/cpanel
  baseurl_source: declared
  description: The SubDomain module for UAPI.
  name: cPanel Sub Domain API
  slug: cpanel-sub-domain-api
- baseURL: https://{host}:2083/json-api/cpanel
  baseurl_source: declared
  description: The TwoFactorAuth module for UAPI.
  name: cPanel Two Factor Auth API
  slug: cpanel-two-factor-auth-api
- baseURL: https://{host}:2083/json-api/cpanel
  baseurl_source: declared
  description: The UserData module for cPanel UAPI.
  name: cPanel User Data API
  slug: cpanel-user-data-api
- baseURL: https://{host}:2083/json-api/cpanel
  baseurl_source: declared
  description: The UserTasks module for UAPI.
  name: cPanel User Tasks API
  slug: cpanel-user-tasks-api
- baseURL: https://{host}:2083/json-api/cpanel
  baseurl_source: declared
  description: The VersionControl module for UAPI.
  name: cPanel Version Control API
  slug: cpanel-version-control-api
artifact_total: 161
asyncapis:
- description: ''
  name: Cpanel Webhooks
  slug: cpanel-webhooks
common:
- group: other
  href: https://artifacts.apis.io/cpanel/capabilities/cpanel-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cpanel-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/cpanel/overlays/cpanel-uapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cpanel-uapi-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cpanel/overlays/cpanel-whm-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cpanel-whm-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://cpanel.net/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.cpanel.net/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://api.docs.cpanel.net/
- group: docs
  title: ''
  type: APIReference
  url: https://api.docs.cpanel.net/specifications/cpanel.openapi
- group: start
  title: ''
  type: GettingStarted
  url: https://api.docs.cpanel.net/guides/quickstart-development-guide/
- group: learn
  title: ''
  type: Tutorials
  url: https://api.docs.cpanel.net/guides/
- group: other
  title: ''
  type: KnowledgeBase
  url: https://docs.cpanel.net/knowledge-base/
- group: auth
  href: https://artifacts.apis.io/cpanel/authentication/cpanel-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cpanel-authentication.yml
- group: auth
  title: ''
  type: Authentication
  url: https://api.docs.cpanel.net/guides/guide-to-api-authentication/
- group: auth
  href: https://artifacts.apis.io/cpanel/scopes/cpanel-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/cpanel-scopes.yml
- group: agent
  href: https://artifacts.apis.io/cpanel/mcp/cpanel-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cpanel-mcp.yml
- group: build
  href: https://artifacts.apis.io/cpanel/mcp/cpanel-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/cpanel-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/cpanel/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/cpanel/agentic-access/cpanel-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cpanel-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/cpanel/llms/cpanel-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cpanel-llms.txt
- group: agent
  title: ''
  type: LlmsText
  url: https://api.docs.cpanel.net/llms.txt
- group: build
  href: https://artifacts.apis.io/cpanel/packages/cpanel-packages.yml
  title: ''
  type: Packages
  url: packages/cpanel-packages.yml
- group: build
  href: https://artifacts.apis.io/cpanel/packages/cpanel-packages.yml
  title: ''
  type: SDKs
  url: packages/cpanel-packages.yml
- group: build
  href: https://artifacts.apis.io/cpanel/cli/cpanel-cli.yml
  title: ''
  type: CLI
  url: cli/cpanel-cli.yml
- group: design
  href: https://artifacts.apis.io/cpanel/conventions/cpanel-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cpanel-conventions.yml
- group: design
  href: https://artifacts.apis.io/cpanel/errors/cpanel-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cpanel-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cpanel/data-model/cpanel-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cpanel-data-model.yml
- group: design
  href: https://artifacts.apis.io/cpanel/conformance/cpanel-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cpanel-conformance.yml
- group: design
  href: https://artifacts.apis.io/cpanel/lifecycle/cpanel-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cpanel-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/cpanel/asyncapi/cpanel-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/cpanel-webhooks.yml
- group: start
  href: https://artifacts.apis.io/cpanel/sandbox/cpanel-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/cpanel-sandbox.yml
- group: commercial
  href: https://artifacts.apis.io/cpanel/plans/cpanel-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cpanel-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cpanel/rate-limits/cpanel-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cpanel-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cpanel/finops/cpanel-finops.yml
  title: ''
  type: FinOps
  url: finops/cpanel-finops.yml
- group: agent
  href: https://artifacts.apis.io/cpanel/well-known/cpanel-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cpanel-well-known.yml
- group: auth
  href: https://artifacts.apis.io/cpanel/well-known/cpanel-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cpanel-security.txt
- group: auth
  href: https://artifacts.apis.io/cpanel/security/cpanel-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/cpanel-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cpanel/security/cpanel-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cpanel-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cpanel/security/cpanel-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cpanel-domain-security.yml
- group: operate
  href: https://artifacts.apis.io/cpanel/changelog/cpanel-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cpanel-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.cpanel.net/changelogs/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.cpanel.net/release-notes/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cpanel.net/
- group: operate
  title: ''
  type: Roadmap
  url: https://features.cpanel.net/
- group: commercial
  title: ''
  type: Pricing
  url: https://cpanel.net/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.cpanel.net/products/trial/
- group: operate
  title: ''
  type: Support
  url: https://support.cpanel.net/hc/en-us
- group: operate
  title: ''
  type: Forums
  url: https://forums.cpanel.net/
- group: company
  title: ''
  type: Blog
  url: https://www.cpanel.net/blog/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/CpanelInc
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CpanelInc
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cpanel.net/legal-notices/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cpanel.net/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cpanel
- group: learn
  title: ''
  type: Training
  url: https://university.cpanel.net/
created: '2025-02-09'
description: cPanel is a web-based control panel that provides a graphical interface and automation tools to simplify the management of web hosting services. cPanel exposes a family of HTTP APIs (UAPI, WHM API 1, and the legacy cPanel API 2) for automating account, domain, email, database, DNS, and server-wide operations. APIs accept API tokens or Basic Authentication and return JSON or XML responses.
finops:
- has_sources: true
  method: derived
  name: Cpanel Finops
  primary_unit: 1 account
  service_category: ''
  slug: cpanel-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cpanel.png
layout: provider
mcp_servers:
- description: 'cPanel publishes a live, anonymously reachable remote MCP server on its own developer documentation host. It is a DOCUMENTATION/DISCOVERY server, not a control-plane server: its six tools read the cPa'
  name: cPanel & WHM Developer Portal MCP Server
  slug: cpanel-whm-developer-portal-mcp-server
modified: '2026-09-05'
name: cPanel
nav: Providers
network: true
overview: 'cPanel publishes 144 API contracts indexed on the [APIs.io](https://apis.io/) network, including 360 Monitoring API, Account Creation API, Account Enhancements API, and 141 more. Tagged areas include Control Panel, DNS, Domains, Email, and Hosting.


  The cPanel catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  cPanel''s developer surface includes documentation, API reference, getting-started guide, authentication, CLI, sandbox, changelog, and 46 more developer resources.'
plans:
- name: Cpanel Plans Pricing
  plan_count: 15
  slug: cpanel-plans-pricing
- name: Cpanel Price Estimates
  plan_count: 0
  slug: cpanel-price-estimates
random_paper: 3
rate_limits:
- limit_count: 0
  name: Cpanel Rate Limits
  slug: cpanel-rate-limits
rules:
- authorship: generated
  effective_rule_count: 107
  extends:
  - spectral:oas
  name: cPanel API Rules
  rule_count: 66
  severity_counts:
    error: 54
    hint: 0
    info: 1
    warn: 11
  slug: cpanel-rules
scopes:
- name: Cpanel Scopes
  scope_count: 0
  slug: cpanel-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 67.9
  coverage:
    artifact_dirs: 32
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 13.6
    contract_quality: 55.2
    developer_ergonomics: 80.4
    discoverability: 75.0
    operational_transparency: 60.5
  previous_composite: 67.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 142
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/cpanel/cpanel-2026-06-20T175154.png
security:
- kind: authentication
  name: Cpanel Authentication
  slug: cpanel-authentication
  summary_line: http/api-key-in-authorization-header · 6 schemes
- kind: domain-security
  name: Cpanel Domain Security
  slug: cpanel-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Cpanel Vulnerability Disclosure
  slug: cpanel-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
skill_count: 5
skills:
- name: cpanel-manage-email-accounts
  slug: cpanel-manage-email-accounts
- name: cpanel-manage-tls-autossl
  slug: cpanel-manage-tls-autossl
- name: cpanel-provision-hosting-account
  slug: cpanel-provision-hosting-account
- name: cpanel-provision-mysql-database
  slug: cpanel-provision-mysql-database
- name: cpanel-rotate-api-tokens
  slug: cpanel-rotate-api-tokens
slug: cpanel
tags:
- Control Panel
- DNS
- Domains
- Email
- Hosting
- Reseller
- Server Administration
- Web Hosting
- WHM
website: https://cpanel.net/
---
