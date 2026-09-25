A P1 SLA says 15 minutes. Then three P1s land at the same time, the endpoint team isn't answering, telemetry is running 20 minutes behind, and your night shift has two analysts.

Now what?

That gap — between the SLA written in a contract and the SLA actually managed inside a live SOC at 2:17 AM — is what this paper is about.

An SLA measures elapsed time. A SOC manages uncertainty, dependencies, evidence, and risk. Those are not the same thing, and treating them as the same thing is where both bad management and bad journalism about SOC performance come from.

Inside "The SOC SLA Reality":

→ Why "P1 = 15 minutes" isn't a NIST, FIRST, ITIL, or industry standard — and why every real SLA table is contract-specific
→ Nine different SLA clocks (acknowledgement, triage, notification, escalation, containment, resolution, closure...) that everyone calls "the SLA"
→ Ten real-condition case studies: 20 alerts at once, a P1 crossing a shift boundary, a customer who won't answer, a SIEM that reports the world 29 minutes late, three P1s and two analysts
→ SLA gaming — the specific behaviors (premature closure, fake "awaiting customer" states, severity downgrades) that make a dashboard look great while the SOC quietly gets worse
→ SLA vs. OLA vs. UC, and why a customer-facing SLA without internal operational targets behind it is a promise with no owner
→ What a SOC manager should actually watch that a compliance percentage will never show

Meeting the SLA doesn't always mean the investigation was good. Breaching the SLA doesn't always mean the SOC failed. Both statements are true, and this paper tries to explain why — with real research (NIST, CISA, FIRST, SANS, and named vendor documentation from Microsoft, IBM/QRadar, Google SecOps, ServiceNow, CrowdStrike, and others), ten illustrative case studies, and no invented "industry standard" numbers.

Full paper (with sources) linked below.

#SOC #CyberSecurity #SecurityOperations #IncidentResponse #SIEM #DetectionEngineering
