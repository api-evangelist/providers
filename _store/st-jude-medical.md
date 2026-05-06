---
aid: st-jude-medical
name: St. Jude Medical
description: St. Jude Medical was a global medical device company specializing in cardiovascular devices including implantable cardioverter defibrillators (ICDs), pacemakers, cardiac resynchronization therapy (CRT) devices, and electrophysiology products. The company was acquired by Abbott in January 2017 and now operates as Abbott's cardiac rhythm management division. Its flagship remote monitoring platform, Merlin.net Patient Care Network, enables clinicians to remotely monitor patients with implanted cardiac devices via the Merlin@home transmitter and the myMerlinPulse mobile application.
url: https://raw.githubusercontent.com/api-evangelist/st-jude-medical/refs/heads/main/apis.yml
tags:
  - Cardiac
  - Cardiovascular
  - Healthcare
  - Medical Devices
  - Patient Monitoring
  - Remote Care
created: '2026-03-24'
modified: '2026-05-02'
apis:
  - aid: st-jude-medical:merlin-net
    name: Merlin.net Patient Care Network API
    tags:
      - Cardiac
      - Healthcare
      - Patient Monitoring
      - Remote Monitoring
    baseURL: https://www.merlin.net
    humanURL: https://www.merlin.net
    description: The Merlin.net Patient Care Network is Abbott's (formerly St. Jude Medical's) remote cardiac monitoring platform. It allows clinicians to receive scheduled transmissions and daily alert notifications from patients with implanted cardiac rhythm management devices including ICDs, CRT devices, and pacemakers. The Merlin@home transmitter communicates with the implanted device via radio frequency and transmits data to the Merlin.net platform via landline, cellular, or wireless broadband.
    properties:
      - url: https://www.cardiovascular.abbott/us/en/hcp/products/cardiac-rhythm-management/connectivity-remote-care/merlin-home-transmitter.html
        type: Documentation
      - url: https://www.merlin.net
        type: Portal
common:
  - url: https://www.cardiovascular.abbott/us/en/home.html
    type: Website
  - url: https://www.st-jude-medical.com
    type: Website
  - url: https://www.abbott.com
    type: Website
  - url: https://www.cardiovascular.abbott/us/en/hcp/products/cardiac-rhythm-management/connectivity-remote-care/merlin-patient-care-network.html
    type: Documentation
  - url: json-ld/st-jude-medical-context.jsonld
    type: JSON-LD
  - url: json-schema/st-jude-medical-cardiac-device-schema.json
    type: JSONSchema
  - url: vocabulary/st-jude-medical-vocabulary.yml
    type: Vocabulary
---
