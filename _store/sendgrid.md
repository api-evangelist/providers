---
aid: sendgrid
url: >-
  https://raw.githubusercontent.com/api-evangelist/sendgrid/refs/heads/main/apis.yml
apis:
  - aid: sendgrid:twilio-sendgrid-account-provisioning-api
    name: Twilio SendGrid Account Provisioning API
    tags: []
    properties:
      - url: openapi/tsg_account_provisioning_v3.yaml
        type: OpenAPI
    description: >-
      The Twilio SendGrid Account Provisioning API provides a platform for
      Twilio SendGrid resellers to manage their customer accounts. This API is
      for companies that have a formal reseller partnership with Twilio
      SendGrid.


      You can access Twilio SendGrid sub-account functionality without becoming
      a reseller. If you require sub-account functionality, see the Twilio
      [SendGrid
      Subusers](https://docs.sendgrid.com/ui/account-and-settings/subusers)
      feature, which is available with [Pro and Premier
      plans](https://sendgrid.com/pricing/).
  - aid: sendgrid:twilio-sendgrid-alerts-api
    name: Twilio SendGrid Alerts API
    tags: []
    properties:
      - url: openapi/tsg_alerts_v3.yaml
        type: OpenAPI
    description: >-
      The Twilio SendGrid Alerts API allows you to specify an email address to
      receive notifications regarding your email usage or statistics. You can
      set up alerts to be sent to a specific email address on a recurring basis,
      whether for informational purposes or when specific account actions occur.


      For most alerts, you can choose to have the alert sent to you as needed,
      hourly, daily, weekly, or monthly. The information contained in your alert
      will be for the last period of the alert. For example, if you choose
      weekly for the statistics alert, you will receive the statistics for the
      last week.
  - aid: sendgrid:twilio-sendgrid-api-keys-api
    name: Twilio SendGrid API Keys API
    tags: []
    properties:
      - url: openapi/tsg_api_keys_v3.yaml
        type: OpenAPI
    description: >-
      The Twilio SendGrid API Keys API allows you manage your API keys and their
      settings. Your application, mail client, or website can all use API keys
      to authenticate access to SendGrid services.


      To create your initial SendGrid API Key, you should use the [SendGrid
      application user interface](https://app.sendgrid.com/settings/api_keys).
      Once you have created a first key with scopes to manage additional API
      keys, you can use this API for all other key management.
  - aid: sendgrid:twilio-sendgrid-domain-authentication-api
    name: Twilio SendGrid Domain Authentication API
    tags: []
    properties:
      - url: openapi/tsg_domain_authentication_v3.yaml
        type: OpenAPI
    description: >-
      The Twilio SendGrid Domain Authentication API allows you to manage your
      authenticated domains and their settings.


      Domain Authentication is a required step when setting up your Twilio
      SendGrid account because it's essential to ensuring the deliverability of
      your email. Domain Authentication signals trustworthiness to email inbox
      providers and your recipients by approving SendGrid to send email on
      behalf of your domain. For more information, see [**How to Set Up Domain
      Authentication**](https://sendgrid.com/docs/ui/account-and-settings/how-to-set-up-domain-authentication/).


      Each user may have a maximum of 3,000 authenticated domains and 3,000 link
      brandings. This limit is at the user level, meaning each Subuser belonging
      to a parent account may have its own 3,000 authenticated domains and 3,000
      link brandings.
  - aid: sendgrid:twilio-sendgrid-email-activity-api
    name: Twilio SendGrid Email Activity API
    tags: []
    properties:
      - url: openapi/tsg_email_activity_v3.yaml
        type: OpenAPI
    description: >-
      The Twilio SendGrid Email Activity API allows you to query all of your
      stored messages, query individual messages, and download a CSV with data
      about the stored messages. Once retrieved, you can inspect the data
      associated with your messages to better understand your mail send. For
      example, you may retrieve all bounced messages or all messages with the
      same subject line and search for commonalities among them.


      You must [purchase additional email activity
      history](https://app.sendgrid.com/settings/billing/addons/email_activity)
      to gain access to the Email Activity Feed API.


      See **Getting Started with the Email Activity Feed API** for help building
      queries and working with this API. You can also work with email activity
      in the **Activity** section of the [Twilio SendGrid application user
      interface](https://app.sendgrid.com/email_activity).
  - aid: sendgrid:twilio-sendgrid-email-address-validation-api
    name: Twilio SendGrid Email Address Validation API
    tags: []
    properties:
      - url: openapi/tsg_email_validation_v3.yaml
        type: OpenAPI
    description: >-
      The Twilio SendGrid Email Address Validation API provides real-time
      detailed information on the validity of email addresses. You can integrate
      this validation process into your platform's signup form and customize the
      best use of email address validation for your use case.


      Email Address Validation is available to [Email API Pro and Premier level
      accounts](https://sendgrid.com/pricing) only. Prior to upgrading your
      account to Pro or Premier, you will not see the option to create an Email
      Validation API key. An Email Validation API key is separate from and in
      addition to your other keys, including Full Access API keys.


      You can use this API to:

      - Indicate to users that the address they have entered into a form is
      invalid.

      - Drop invalid email addresses from your database.

      - Suppress invalid email addresses from your sending to decrease your
      bounce rate.


      See [**Email Address
      Validation**](https://docs.sendgrid.com/ui/managing-contacts/email-address-validation)
      for more information.


      You can also view your Email Validation results and metrics in the
      Validation section of the [Twilio SendGrid application user
      interface](https://docs.sendgrid.com/ui/managing-contacts/email-address-validation).
  - aid: sendgrid:twilio-sendgrid-enforced-tls-api
    name: Twilio SendGrid Enforced TLS API
    tags: []
    properties:
      - url: openapi/tsg_enforced_tls_v3.yaml
        type: OpenAPI
    description: >-
      The Twilio SendGrid Enforced TLS API allows you to specify whether or not
      the recipient of your mail send is required to support TLS or have a valid
      certificate.


      Twilio SendGrid sends all emails with [Opportunistic
      TLS](https://sendgrid.com/blog/myth-opportunistic-tls-email-privacy/) by
      default, meaning email is sent with TLS, and if the recipient's inbox
      provider does not accept the TLS encryption, we then send the message
      unencrypted.


      You can optionally choose to enforce TLS encryption, meaning that if the
      recipient's inbox provider does not accept the TLS encryption, Twilio
      SendGrid drops the message and sends a block event with the message, TLS
      required but not supported as the description.
  - aid: sendgrid:twilio-sendgrid-integrations-api
    name: Twilio SendGrid Integrations API
    tags: []
    properties:
      - url: openapi/tsg_integrations_v3.yaml
        type: OpenAPI
    description: >-
      Integrations allows you to connect your SendGrid applications with
      third-party services and forward SendGrid email events to those external
      applications. Currently, Integrations supports event forwarding to
      [Segment](https://segment.com/docs). You can use this API to create,
      delete, view, and update your Integrations.
  - aid: sendgrid:twilio-sendgrid-ip-access-management-api
    name: Twilio SendGrid IP Access Management API
    tags: []
    properties:
      - url: openapi/tsg_ip_access_management_v3.yaml
        type: OpenAPI
    description: >-
      IP Twilio SendGrid IP Access Management API allows you to control which IP
      addresses can be used to access your account, either through the SendGrid
      application user interface or the API.


      There is no limit to the number of IP addresses that you can allow.


      It is possible to remove your own IP address from your list of allowed
      addresses, thus blocking your own access to your account. While we are
      able to restore your access, we do require thorough proof of your identify
      and ownership of your account. We take the security of your account very
      seriously and wish to prevent any 'bad actors' from maliciously gaining
      access to your account. Your current IP is clearly displayed to help
      prevent you from accidentally removing it from the allowed addresses.


      See [**IP Access
      Management**](https://docs.sendgrid.com/ui/account-and-settings/ip-access-management)
      for more information.
  - aid: sendgrid:twilio-sendgrid-ip-address-management-api
    name: Twilio SendGrid IP Address Management API
    tags: []
    properties:
      - url: openapi/tsg_ip_address_management_v3.yaml
        type: OpenAPI
    description: >-
      The Twilio SendGrid IP Address Management API combines functionality that
      was previously split between the Twilio SendGrid [IP Address
      API](https://docs.sendgrid.com/api-reference/ip-address) and [IP Pools
      API](https://docs.sendgrid.com/api-reference/ip-pools). This functionality
      includes adding IP addresses to your account, assigning IP addresses to IP
      Pools and Subusers, among other tasks.
  - aid: sendgrid:twilio-sendgrid-ip-warmup-api
    name: Twilio SendGrid IP Warmup API
    tags: []
    properties:
      - url: openapi/tsg_ip_warmup_v3.yaml
        type: OpenAPI
    description: >-
      The Twilio SendGrid IP Warm Up API allows you to gradually increasing the
      volume of mail sent with a dedicated IP address according to a
      predetermined schedule. This gradual process helps to establish a
      reputation with ISPs (Internet Service Providers) as a legitimate email
      sender.


      SendGrid can automatically warm up dedicated IP addresses by limiting the
      amount of mail that can be sent through them per hour. The limit is
      determined by how long the IP address has been warming up.


      See the [warmup
      schedule](https://sendgrid.com/docs/ui/sending-email/warming-up-an-ip-address/#automated-ip-warmup-hourly-send-schedule)
      to learn how SendGrid limits your email traffic for IPs in warmup.


      You can also choose to use Twilio SendGrid's automated IP warmup for any
      of your IPs from the **IP Addresses** settings menu in the [Twilio
      SendGrid application user
      interface](https://app.sendgrid.com/settings/ip_addresses).
  - aid: sendgrid:twilio-sendgrid-ip-address-api
    name: Twilio SendGrid IP Address API
    tags: []
    properties:
      - url: openapi/tsg_ips_v3.yaml
        type: OpenAPI
    description: >-
      The Twilio SendGrid IP Address API allows you to add and manage dedicated
      IP addresses and IP Pools for your SendGrid account and Subusers. If you
      are sending any significant amount of email, SendGrid typically suggests
      sending from dedicated IPs. It's also best to send marketing and
      transactional emails from separate IP addresses. In order to do this,
      you'll need to set up IP Pools, which are groups of dedicated IP addresses
      you define to send particular types of messages. See the [**Dedicated IP
      Addresses**](https://docs.sendgrid.com/ui/account-and-settings/dedicated-ip-addresses)
      for more information about obtaining and allocating IPs.
  - aid: sendgrid:twilio-sendgrid-link-branding-api
    name: Twilio SendGrid Link Branding API
    tags: []
    properties:
      - url: openapi/tsg_link_branding_v3.yaml
        type: OpenAPI
    description: >-
      The Twilio SendGrid Link Branding API allows you to configure your domain
      settings so that all of the click-tracked links, opens, and images in your
      emails are served from your domain rather than `sendgrid.net`. Spam
      filters and recipient servers look at the links within emails to determine
      whether the email appear trustworthy. They use the reputation of the root
      domain to determine whether the links can be trusted.


      You can also manage Link Branding in the **Sender Authentication** section
      of the Twilio SendGrid application user interface.

       See [**How to Set Up Link Branding**](https: //sendgrid.com/docs/ui/account-and-settings/how-to-set-up-link-branding/) for more information.
  - aid: sendgrid:twilio-sendgrid-legacy-marketing-campaigns-campaigns-api
    name: Twilio SendGrid Legacy Marketing Campaigns Campaigns API
    tags: []
    properties:
      - url: openapi/tsg_lmc_campaigns_v3.yaml
        type: OpenAPI
    description: >-
      The Twilio SendGrid Legacy Marketing Campaigns Campaigns API allows you to
      manage your marketing email messages programmatically. This API is
      operational, but we recommend using the current version of Marketing
      Campaigns to manage your marketing messages with SendGrid [Single
      Sends](https://docs.sendgrid.com/api-reference/single-sends/) and
      [Automations](https://docs.sendgrid.com/ui/sending-email/getting-started-with-automation).


      See [**Migrating from Legacy Marketing
      Campaigns**](https://docs.sendgrid.com/ui/sending-email/migrating-from-legacy-marketing-campaigns)
      for more information.
  - aid: sendgrid:twilio-sendgrid-legacy-marketing-campaigns-contacts-api
    name: Twilio SendGrid Legacy Marketing Campaigns Contacts API
    tags: []
    properties:
      - url: openapi/tsg_lmc_contactdb_v3.yaml
        type: OpenAPI
    description: >-
      The Twilio SendGrid Legacy Marketing Campaigns Contacts API allows you to
      manage your marketing contacts programmatically. This API is operational,
      but we recommend using the current version of Marketing Campaigns'
      [Contacts API](https://docs.sendgrid.com/api-reference/contacts/), [Lists
      API](https://docs.sendgrid.com/api-reference/lists/), and [Segments
      API](https://docs.sendgrid.com/api-reference/segmenting-contacts-v2/) to
      manage your contacts.


      See [**Migrating from Legacy Marketing
      Campaigns**](https://docs.sendgrid.com/ui/sending-email/migrating-from-legacy-marketing-campaigns)
      for more information.
  - aid: sendgrid:twilio-sendgrid-legacy-marketing-campaigns-sender-identities-api
    name: Twilio SendGrid Legacy Marketing Campaigns Sender Identities API
    tags: []
    properties:
      - url: openapi/tsg_lmc_senders_v3.yaml
        type: OpenAPI
    description: >-
      The Twilio SendGrid Legacy Marketing Campaigns Sender Identites API allows
      you to manage the email addresses used to send your marketing email. This
      API is operational, but we recommend using the current version of
      Marketing Campaigns to manage your
      [senders](https://docs.sendgrid.com/api-reference/senders/).


      See [**Migrating from Legacy Marketing
      Campaigns**](https://docs.sendgrid.com/ui/sending-email/migrating-from-legacy-marketing-campaigns)
      for more information.
  - aid: sendgrid:twilio-sendgrid-mail-settings-api
    name: Twilio SendGrid Mail Settings API
    tags: []
    properties:
      - url: openapi/tsg_mail_settings_v3.yaml
        type: OpenAPI
    description: >-
      The Twilio SendGrid Mail Settings API allows you to retrieve and configure
      the various Mail Settings available. Mail Settings instruct SendGrid to
      apply specific settings to every email that you send over [SendGrids Web
      API](https://docs.sendgrid.com/api-reference/mail-send/v3-mail-send) or
      [SMTP
      relay](https://sendgrid.com/docs/for-developers/sending-email/building-an-x-smtpapi-header/).
      These settings include how to embed a custom footer, how to manage blocks,
      spam, and bounces, and more.


      For a full list of Twilio SendGrid's Mail Settings, and what each one
      does, see [**Mail
      Settings**](https://sendgrid.com/docs/ui/account-and-settings/mail/).


      You can also manage your Mail Settings in the Twilio SendGrid application
      user interface.
  - aid: sendgrid:twilio-sendgrid-mail-api
    name: Twilio SendGrid Mail API
    tags: []
    properties:
      - url: openapi/tsg_mail_v3.yaml
        type: OpenAPI
    description: >-
      The Twilio SendGrid v3 Mail API allows you to send email at scale over
      HTTP. The Mail Send endpoint supports many levels of functionality,
      allowing you to send templates, set categories and custom arguments that
      can be used to analyze your send, and configure which tracking settings to
      include such as opens and clicks. You can also group mail sends into
      batches, allowing you to schedule and cancel sends by their batch IDs.
  - aid: sendgrid:twilio-sendgrid-marketing-campaigns-contacts-api
    name: Twilio SendGrid Marketing Campaigns Contacts API
    tags: []
    properties:
      - url: openapi/tsg_mc_contacts_v3.yaml
        type: OpenAPI
    description: >-
      The Twilio SendGrid Marketing Campaigns Contacts API allows you to manage
      all of your marketing contacts programmatically. You can also import and
      export contacts using this API. The Contacts API allows you to associate
      contacts with lists and segments; however, to manage the lists and
      segments themselves, see the [Lists
      API](https://docs.sendgrid.com/api-reference/lists/) and [Segments
      API](https://docs.sendgrid.com/api-reference/segmenting-contacts-v2/).


      You can also manage your marketing contacts with the [Marketing Campaigns
      application user interface](https://mc.sendgrid.com/contacts). See [**How
      to Send Email with New Marketing
      Campaigns**](https://docs.sendgrid.com/ui/sending-email/how-to-send-email-with-marketing-campaigns)
      for more information.
  - aid: sendgrid:twilio-sendgrid-marketing-campaigns-custom-fields-api
    name: Twilio SendGrid Marketing Campaigns Custom Fields API
    tags: []
    properties:
      - url: openapi/tsg_mc_custom_fields_v3.yaml
        type: OpenAPI
    description: >-
      The Twilio SendGrid Marketing Campaigns Custom Fields API allows you to
      add extra information about your marketing contacts that is relevant to
      your needs. For example, a fashion retailer might create a custom field
      for customers' shoe sizes, an ice cream shop might store customers'
      favorite flavors in a custom field, and you can create custom fields that
      make sense for your business.


      With custom fields, you can also create
      [segments](https://docs.sendgrid.com/api-reference/segmenting-contacts-v2/)
      based on custom fields values. Your custom fields are completely
      customizable to the use-cases and user information that you need.


      You can also manage your Custom Fields using the SendGrid application user
      interface. See [**Using Custom
      Fields**](https://docs.sendgrid.com/ui/managing-contacts/custom-fields)
      for more information, including a list of Reserved Fields. You can also
      manage your custom fields in the [Marketing Campaigns application user
      interface](https://mc.sendgrid.com/custom-fields).
  - aid: sendgrid:twilio-sendgrid-marketing-campaigns-designs
    name: Twilio SendGrid Marketing Campaigns Designs
    tags: []
    properties:
      - url: openapi/tsg_mc_designs_v3.yaml
        type: OpenAPI
    description: >-
      The Twilio SendGrid Designs API offers the ability to manage assets stored
      in the Twilio SendGrid [Design
      Library](https://mc.sendgrid.com/design-library/my-designs).


      The Design Library is a feature-rich email layout tool and media
      repository. You can [build designs for all your marketing email
      needs](https://sendgrid.com/docs/ui/sending-email/working-with-marketing-campaigns-email-designs/),
      including Single Sends and Automations.


      You can also duplicate and then modify one of the pre-built designs
      provided by Twilio SendGrid to get you started.


      The Designs API provides a REST-like interface for creating new designs,
      retrieving a list of existing designs, duplicating or updating a design,
      and deleting a design.
  - aid: sendgrid:twilio-sendgrid-marketing-campaigns-lists-api
    name: Twilio SendGrid Marketing Campaigns Lists API
    tags: []
    properties:
      - url: openapi/tsg_mc_lists_v3.yaml
        type: OpenAPI
    description: >-
      The Twilio SendGrid Marketing Campaigns Lists API allows you to manage
      your contacts lists programmatically. Lists are static collections of
      Marketing Campaigns contacts. You can use this API to interact with the
      list objects themselves. To add contacts to a list, you must use the
      [Contacts API](https://docs.sendgrid.com/api-reference/contacts/).


      You can also manage your lists using the Contacts menu in the [Marketing
      Campaigns application user interface](https://mc.sendgrid.com/contacts).
      For more information about lists and best practices for building them, see
      [**Building your Contact
      Lists**](https://sendgrid.com/docs/ui/managing-contacts/building-your-contact-list/).
  - aid: sendgrid:twilio-sendgrid-marketing-campaigns-segments-20-api
    name: Twilio SendGrid Marketing Campaigns Segments 2.0 API
    tags: []
    properties:
      - url: openapi/tsg_mc_segments_2.0_v3.yaml
        type: OpenAPI
    description: >-
      The Twilio SendGrid Marketing Campaigns Segments V2 API allows you to
      create, edit, and delete segments as well as retrieve a list of segments
      or an individual segment by ID.


      Segments are similar to contact lists, except they update dynamically over
      time as information stored about your contacts or the criteria used to
      define your segments changes. When you segment your audience, you are able
      to create personalized Automation emails and Single Sends that directly
      address the wants and needs of your particular audience.


      Note that Twilio SendGrid checks for newly added or modified contacts who
      meet a segment's criteria on an hourly schedule. Only existing contacts
      who meet a segment's criteria will be included in the segment searches
      within 15 minutes.


      Segments built using engagement data such as "was sent" or "clicked" will
      take approximately 30 minutes to begin populating.


      Segment samples and counts are refreshed approximately once per hour; they
      do not update immediately. If no contacts are added to or removed from a
      segment since the last refresh, the sample and UI count displayed will be
      refreshed at increasing time intervals with a maximum sample and count
      refresh delay of 24 hours.


      You can also manage your Segments with the [Marketing Campaigns
      application user interface](https://mc.sendgrid.com/contacts). See
      [**Segmenting Your
      Contacts**](https://docs.sendgrid.com/ui/managing-contacts/segmenting-your-contacts)
      for more information.
  - aid: sendgrid:twilio-sendgrid-marketing-campaigns-segments-api
    name: Twilio SendGrid Marketing Campaigns Segments API
    tags: []
    properties:
      - url: openapi/tsg_mc_segments_v3.yaml
        type: OpenAPI
    description: >-
      This API was deprecated on December 31, 2022. Following deprecation, all
      segments created in the Marketing Campaigns user interface began using the
      [Segmentation v2
      API](https://docs.sendgrid.com/api-reference/segmenting-contacts-v2).


      To enable manual migration and data retrieval, this API's GET and DELETE
      operations will remain available. The POST (create) and PATCH (update)
      endpoints were removed on January 31, 2023 because it is no longer
      possible to create new v1 segments or modify existing ones. See our
      [Segmentation v1 to v2 upgrade
      instructions](https://docs.sendgrid.com/for-developers/sending-email/getting-started-the-marketing-campaigns-v2-segmentation-api#upgrade-a-v1-segment-to-v2)
      to manually migrate your segments to the v2 API.
  - aid: sendgrid:twilio-sendgrid-marketing-campaigns-senders-api
    name: Twilio SendGrid Marketing Campaigns Senders API
    tags: []
    properties:
      - url: openapi/tsg_mc_senders_v3.yaml
        type: OpenAPI
    description: >-
      The Twilio SendGrid Marketing Campaigns Senders API allows you to create a
      verified sender from which your marketing emails will be sent. To ensure
      our customers maintain the best possible sender reputations and to uphold
      legitimate sending behavior, we require customers to verify their Senders.
      A Sender represents your From email addressthe address your recipients
      will see as the sender of your emails.
  - aid: sendgrid:twilio-sendgrid-marketing-campaigns-single-sends-api
    name: Twilio SendGrid Marketing Campaigns Single Sends API
    tags: []
    properties:
      - url: openapi/tsg_mc_singlesends_v3.yaml
        type: OpenAPI
    description: >-
      The Twilio SendGrid Single Sends API allows you to create, manage, and
      send Single Sends. You can also search Single Sends and retrieve
      statistics about them to help you maintain, alter, and further develop
      your campaigns.


      A Single Send is a one-time non-automated email message delivered to a
      list or segment of your audience. A Single Send may be sent immediately or
      scheduled for future delivery.


      Single Sends can serve many use cases, including promotional offers,
      engagement campaigns, newsletters, announcements, legal notices, or policy
      updates. You can also create and manage Single Sends in the [Marketing
      Campaigns application user
      interface](https://mc.sendgrid.com/single-sends).


      The Single Sends API changed on May 6, 2020. See [**Single Sends 2020
      Update**](https://docs.sendgrid.com/for-developers/sending-email/single-sends-2020-update)
      for more information.
  - aid: sendgrid:twilio-sendgrid-marketing-campaigns-statistics-api
    name: Twilio SendGrid Marketing Campaigns Statistics API
    tags: []
    properties:
      - url: openapi/tsg_mc_stats_v3.yaml
        type: OpenAPI
    description: >-
      The Marketing Campaigns Stats API allows you to retrieve statistics for
      both Automations and Single Sends. The statistics provided include
      bounces, clicks, opens, and more. You can export stats in CSV format for
      use in other applications. You can also retrieve Marketing Campaigns stats
      in the [Marketing Campaigns application user
      interface](https://mc.sendgrid.com/).


      This API provides statistics for Marketing Campaigns only. For stats
      related to event tracking, please see the [Stats
      API](https://docs.sendgrid.com/api-reference/stats).
  - aid: sendgrid:twilio-sendgrid-marketing-campaigns-send-test-email-api
    name: Twilio SendGrid Marketing Campaigns Send Test Email API
    tags: []
    properties:
      - url: openapi/tsg_mc_test_v3.yaml
        type: OpenAPI
    description: >-
      The Twilio SendGrid Test Email API allows you to test a marketing email by
      first sending it to a list of up to 10 email addresses before pushing to a
      contact list or segment. With this feature, you can test the layout and
      content of your message in multiple email clients and with multiple
      recipients to see how it will function in a real-world scenario.
  - aid: sendgrid:twilio-sendgrid-partner-api
    name: Twilio SendGrid Partner API
    tags: []
    properties:
      - url: openapi/tsg_partner_v3.yaml
        type: OpenAPI
    description: >-
      The Twilio SendGrid Partner Settings API allows you to integrate your
      SendGrid account with our partners to increase your SendGrid experience
      and functionality. For more information about our partners and how you can
      begin integrating with them, please visit our [Partners
      page](https://sendgrid.com/partners/marketplace/).
  - aid: sendgrid:twilio-sendgrid-recipients-data-erasure-api
    name: Twilio SendGrid Recipients' Data Erasure API
    tags: []
    properties:
      - url: openapi/tsg_recipients_data_erasure_v3.yaml
        type: OpenAPI
    description: >-
      The Recipients' Data Erasure API allows Twilio SendGrid customers to
      delete their own customers' personal data from the Twilio SendGrid
      Platform. The use of this API facilitates the self-service removal of
      email personal data from the Twilio SendGrid platform and will enable
      customers to comply with various obligatory data privacy regulations.
  - aid: sendgrid:twilio-sendgrid-reverse-dns-api
    name: Twilio SendGrid Reverse DNS API
    tags: []
    properties:
      - url: openapi/tsg_reverse_dns_v3.yaml
        type: OpenAPI
    description: >-
      The Twilio SendGrid Reverse DNS API (formerly IP Whitelabel) allows you to
      configure reverse DNS settings for your account. Mailbox providers verify
      the sender of your emails by performing a reverse DNS lookup.


      When setting up Reverse DNS, Twilio SendGrid will provide an A Record
      (address record) for you to add to the DNS records of your sending domain.
      The A record maps your sending domain to a dedicated Twilio SendGrid IP
      address. Once Twilio SendGrid has verified that the appropriate A record
      for the IP address has been created, the appropriate reverse DNS record
      for the IP address is generated.


      Reverse DNS is available for [dedicated IP
      addresses](https://sendgrid.com/docs/ui/account-and-settings/dedicated-ip-addresses/)
      only.


      You can also manage your reverse DNS settings in the Sender Authentication
      setion of the [Twilio SendGrid application user
      interface](https://app.sendgrid.com/settings/sender_auth).


      See [**How to Set Up Reverse
      DNS**](https://sendgrid.com/docs/ui/account-and-settings/how-to-set-up-reverse-dns/)
      for more information.
  - aid: sendgrid:twilio-sendgrid-scheduled-sends-api
    name: Twilio SendGrid Scheduled Sends API
    tags: []
    properties:
      - url: openapi/tsg_scheduled_sends_v3.yaml
        type: OpenAPI
    description: >-
      The Twilio SendGrid Scheduled Sends API allows you to cancel or pause the
      send of one or more emails using a batch ID.


      A `batch_id` groups multiple scheduled mail send requests together with
      the same ID. You can cancel or pause all of the requests associated with a
      batch ID up to 10 minutes before the scheduled send time.


      See [**Canceling a Scheduled
      Send**](https://docs.sendgrid.com/for-developers/sending-email/stopping-a-scheduled-send)
      for a guide on creating a `batch_id`, assigning it to a scheduled send,
      and modifying the send.


      See the Mail API's batching operations to validate a `batch_id` and
      retrieve all scheduled sends as an array.


      When a batch is canceled, all messages associated with that batch will
      stay in your sending queue. When their `send_at` value is reached, they
      will be discarded.


      When a batch is paused, all messages associated with that batch will stay
      in your sending queue, even after their `send_at` value has passed. This
      means you can remove a pause status, and your scheduled send will be
      delivered once the pause is removed. Any messages left with a pause status
      that are more than 72 hours old will be discarded as Expired.
  - aid: sendgrid:twilio-sendgrid-scopes-api
    name: Twilio SendGrid Scopes API
    tags: []
    properties:
      - url: openapi/tsg_scopes_v3.yaml
        type: OpenAPI
    description: >-
      The Twilio SendGrid Scopes API allows you to retrieve the scopes or
      permissions available to a user, see the user's attempts to access your
      SendGrid account, and, if necessary, deny an access request.
  - aid: sendgrid:twilio-sendgrid-engagement-quality-api
    name: Twilio SendGrid Engagement Quality API
    tags: []
    properties:
      - url: openapi/tsg_seq_v3.yaml
        type: OpenAPI
    description: >-
      The SendGrid Engagement Quality (SEQ) API allows you to retrieve metrics
      that define the quality of your email program.


      An SEQ score is correlated with:

      - The quality of the data in a senders program.

      - How wanted the sender's email is by their recipients.


      Because wanted email and deliverability are closely related, a higher SEQ
      metric is correlated with greater deliverability. This means the higher
      your SEQ score, the more likely you are to land in your recipients'
      inboxes. See the SEQ Overview page to understand SEQ, how it's calculated,
      and how you can address your score. The SEQ endpoints allow you to
      retrieve your scores and scores for your Subusers.
  - aid: sendgrid:twilio-sendgrid-single-sign-on-api
    name: Twilio SendGrid Single Sign-On API
    tags: []
    properties:
      - url: openapi/tsg_sso_v3.yaml
        type: OpenAPI
    description: >-
      The Single Sign-On API allows you to manage your SAML 2.0 SSO
      configurations. You can also work with your SSO integrations using the SSO
      section of the [Twilio SendGrid application user
      interface](https://app.sendgrid.com/settings/sso).


      The Single Sign-On Settings operations allow you to create, retrieve,
      modify, and delete SSO integrations for your Twilio SendGrid account. Each
      integration will correspond to a specific IdP such as Okta, Duo, or
      Microsoft Azure Active Directory.


      The Single Sign-On Certificates operations allow you to create, modify,
      and delete SSO certificates. A SAML certificate allows your IdP and Twilio
      SendGrid to verify requests are coming from one another using the
      `public_certificate` and `integration_id` parameters.


      The Single Sign-On Teammates operations allow you to add and modify SSO
      Teammates. SSO Teammates are the individual user accounts who will access
      your Twilio SendGrid account with SSO credentials. To retrieve or delete
      an SSO Teammate, you will use the separate [Teammates
      API](https://docs.sendgrid.com/api-reference/teammates/).
  - aid: sendgrid:twilio-sendgrid-statistics-api
    name: Twilio SendGrid Statistics API
    tags: []
    properties:
      - url: openapi/tsg_stats_v3.yaml
        type: OpenAPI
    description: >-
      The Twilio SendGrid Statistics API allows you to retrieve the various
      statistics related to your email program.


      Tracking your emails is an important part of being a good sender and
      learning about how your users interact with your email. This includes
      everything from clicks and opens to looking at which browsers and mailbox
      providers your customers use.


      SendGrid has broken up statistics in specific ways so that you can get
      at-a-glance data, as well as the details of how your email is being used.


      Category statistics are available for the previous thirteen months only.


      See [**Statistics
      Overview**](https://docs.sendgrid.com/ui/analytics-and-reporting/stats-overview)
      for more information.
  - aid: sendgrid:twilio-sendgrid-subusers
    name: Twilio SendGrid Subusers
    tags: []
    properties:
      - url: openapi/tsg_subusers_v3.yaml
        type: OpenAPI
    description: >-
      The Twilio SendGrid Subusers API allows you to create and manage your
      Subuser accounts. Subusers are available on [Pro and Premier
      plans](https://sendgrid.com/pricing), and you can think of them as
      sub-accounts. Each Subuser can have its own sending domains, IP addresses,
      and reporting. SendGrid recommends creating Subusers for each of the
      different types of emails you sendone Subuser for transactional emails and
      another for marketing emails. Independent Software Vendor (ISV) customers
      may also create Subusers for each of their customers.


      You can also manage Subusers in the [Twilio SendGrid application user
      interface](https://app.sendgrid.com/settings/subusers). See
      [**Subusers**](https://docs.sendgrid.com/ui/account-and-settings/subusers)
      for more information.
  - aid: sendgrid:twilio-sendgrid-suppressions-api
    name: Twilio SendGrid Suppressions API
    tags: []
    properties:
      - url: openapi/tsg_suppressions_v3.yaml
        type: OpenAPI
    description: >-
      The Twilio SendGrid Suppressions API allows you to manage your
      Suppressions or Unsubscribes and Suppression or Unsubscribe groups. With
      SendGrid, an unsubscribe is the action an email recipient takes when they
      opt-out of receiving your messages. A suppression is the action you take
      as a sender to filter or suppress an unsubscribed address from your email
      send. From the perspective of the recipient, your suppression is the
      result of their unsubscribe.


      You can have global suppressions, which represent addresses that have been
      unsubscribed from all of your emails. You can also have suppression
      groups, also known as ASM groups, which represent categories or groups of
      emails that your recipients can unsubscribe from, rather than
      unsubscribing from all of your messages.


      SendGrid automatically suppresses emails sent to users for a variety of
      reasons, including blocks, bounces, invalid email addresses, spam reports,
      and unsubscribes. SendGrid suppresses these messages to help you maintain
      the best possible sender reputation by attempting to prevent unwanted
      mail. You may also add addresses to your suppressions.


      See
      [**Suppressions**](https://docs.sendgrid.com/for-developers/sending-email/suppressions)
      for more information.
  - aid: sendgrid:twilio-sendgrid-teammates-api
    name: Twilio SendGrid Teammates API
    tags: []
    properties:
      - url: openapi/tsg_teammates_v3.yaml
        type: OpenAPI
    description: >-
      The Twilio SendGrid Teammates API allows you to add, manage, and remove
      Teammates, or user accounts, from your SendGrid account. Teammates
      function like user accounts on the SendGrid account, allowing you to
      invite additional users to your account with scoped access. You can think
      of Teammates as SendGrid's approach to enabling [role-based access
      control](https://en.wikipedia.org/wiki/Role-based_access_control) for your
      SendGrid account. For even more control over the access to your account,
      see the [Twilio SendGrid SSO
      API](https://docs.sendgrid.com/api-reference/single-sign-on-teammates/),
      which enables SSO-authenticated Teammates to be managed through a SAML 2.0
      identity provider.
  - aid: sendgrid:twilio-sendgrid-templates-api
    name: Twilio SendGrid Templates API
    tags: []
    properties:
      - url: openapi/tsg_templates_v3.yaml
        type: OpenAPI
    description: >-
      The Twilio SendGrid Templates API allows you to create and manage email
      templates to be delivered with SendGrid's sending APIs. The templates you
      create will be available using a template ID that is passed to our sending
      APIs as part of the request. Each template may then have multiple versions
      associated with it. Whichever version is set as "active" at the time of
      the request will be sent to your recipients. This system allows you to
      update a single template's look and feel entirely without modifying your
      requests to our Mail Send API. For example, you could have a single
      template for welcome emails. That welcome template could then have a
      version for each season of the year that's themed appropriately and marked
      as active during the appropriate season. The template ID passed to our
      sending APIs never needs to change; you can just modify which version is
      active.


      This API provides operations to create and manage your templates as well
      as their versions.


      Each user can create up to 300 different templates. Templates are specific
      to accounts and Subusers. Templates created on a parent account will not
      be accessible from the Subusers' accounts.
  - aid: sendgrid:twilio-sendgrid-tracking-settings-api
    name: Twilio SendGrid Tracking Settings API
    tags: []
    properties:
      - url: openapi/tsg_tracking_settings_v3.yaml
        type: OpenAPI
    description: >-
      The Twilio SendGrid Tracking Settings API allows you to configure which
      tracking settings are enabled for your messages. You can track many of
      your recipients' interactions with your emails, including which emails
      they open, which links they click, and when they subscribe to or
      unsubscribe from your emails. See [**Tracking
      Settings**](https://docs.sendgrid.com/ui/account-and-settings/tracking)
      for more information.
  - aid: sendgrid:twilio-sendgrid-user-api
    name: Twilio SendGrid User API
    tags: []
    properties:
      - url: openapi/tsg_user_v3.yaml
        type: OpenAPI
    description: >-
      The Twilio SendGrid User API allows you to modify the settings of a
      SendGrid user account such as the user's email address or username.
      Keeping your user profile up to date helps SendGrid verify who you are and
      share important communications with you.


      See [**Account
      Details**](https://docs.sendgrid.com/ui/account-and-settings/account) for
      more information. You can also manage your user settings in the [SendGrid
      application user interface](https://app.sendgrid.com/account/details).
  - aid: sendgrid:twilio-sendgrid-verified-senders-api
    name: Twilio SendGrid Verified Senders API
    tags: []
    properties:
      - url: openapi/tsg_verified_senders_v3.yaml
        type: OpenAPI
    description: >-
      The Twilio SendGrid Verified Senders API allows you to programmatically
      manage the Sender Identities that are authorized to send email for your
      account. You can also manage Sender Identities in the [SendGrid
      application user
      interface](https://app.sendgrid.com/settings/sender_auth). See [**Single
      Sender
      Verification**](https://sendgrid.com/docs/ui/sending-email/sender-verification/)
      for more information.


      You an use this API to create new Sender Identities, retrieve a list of
      existing Sender Identities, check the status of a Sender Identity, update
      a Sender Identity, and delete a Sender Identity.


      This API offers additional operations to check for domains known to
      implement DMARC and resend verification emails to Sender Identities that
      have yet to complete the verification process.
  - aid: sendgrid:twilio-sendgrid-webhook-configuration-api
    name: Twilio SendGrid Webhook Configuration API
    tags: []
    properties:
      - url: openapi/tsg_webhooks_v3.yaml
        type: OpenAPI
    description: >-
      The Twilio SendGrid Webhooks API allows you to configure the Event and
      Parse Webhooks.


      Email is a data-rich channel, and implementing the Event Webhook will
      allow you to consume those data in nearly real time. This means you can
      actively monitor and participate in the health of your email program
      throughout the send cycle.


      The Inbound Parse Webhook processes all incoming email for a domain or
      subdomain, parses the contents and attachments and then POSTs
      `multipart/form-data` to a URL that you choose. 
name: SendGrid
tags:
  - Email
  - T1
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: properties/sendgrid-oai
    name: OpenAPI
    type: OpenAPI
created: '2025-08-14'
modified: '2025-12-31'
position: Consumer
description: >-
  SendGrid is a cloud-based customer communication platform that provides tools
  for email marketing and transactional email delivery. It helps businesses of
  all sizes easily create and send emails to their customers, enabling them to
  build stronger relationships and drive engagement. SendGrid also offers
  analytics and reporting tools to track the success of email campaigns, as well
  as features for managing subscriber lists and personalizing emails for
  targeted communications. Overall, SendGrid's platform allows businesses to
  streamline their email marketing efforts and improve their overall
  communication strategies.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'

---