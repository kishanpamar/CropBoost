self.addEventListener('install', e=>{
  e.waitUntil(caches.open('cb-v1').then(c=>c.addAll(['/','/manifest.json','/static/sw.js'])));
});
self.addEventListener('fetch', e=>{
  e.respondWith(caches.match(e.request).then(r=> r || fetch(e.request)));
});