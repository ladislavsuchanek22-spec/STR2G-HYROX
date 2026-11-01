// STR2G Athletes – members-only content.
// Only logged-in members get this (through /api/athletes/me), it is never a public file.
// Update it every week / month and push. Leave a field as null and the members area shows "coming soon".

export const CONTENT = {
  workout: {
    // label: "WEEK 45",
    // title: "Compromised 1K repeats",
    // goal: "Hold race pace on the run straight after the sled.",
    // duration: "60 MIN",
    // parts: ["Warm-up: ...", "Main: ...", "Cool-down: ..."],
    // note: "Run the 1Ks at goal race pace, not faster.",
    label: null,
    title: null,
    goal: null,
    duration: null,
    parts: [],
    note: null,
  },
  topic: {
    // title: "Sled push: technique that saves 20 seconds",
    // videoUrl: "https://www.youtube.com/embed/XXXX",
    title: null,
    videoUrl: null,
  },
  qa: {
    // when: "Thu 20 Nov · 19:00 CET",
    // url: "https://meet.google.com/...",
    when: null,
    url: null,
  },
  challenge: {
    // title: "1000 m SkiErg + 50 wall balls",
    // submitUrl: "https://forms.gle/...",
    // leaderboard: [{ name: "Jana N.", result: "6:12" }],
    title: null,
    submitUrl: null,
    leaderboard: [],
  },
  community: {
    url: null, // invite link to the members group
    nextMeetup: null, // e.g. "HYROX Vienna · 6 Dec"
  },
  merch: {
    storeUrl: null,
    code: null,
    nextDrop: null,
  },
};
