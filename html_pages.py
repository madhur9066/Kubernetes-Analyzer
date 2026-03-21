"""
html_pages.py — All HTML/CSS/JS as Python string constants.
Fully offline. No CDN. No external fonts or resources.
"""

_CSS = """
*{box-sizing:border-box;margin:0;padding:0;}
html,body{height:100%;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:#f0f2f5;color:#1e293b;font-size:14px;}
#wrap{display:flex;height:100vh;overflow:hidden;}
#sb{width:220px;background:#1e293b;display:flex;flex-direction:column;flex-shrink:0;height:100vh;overflow-y:auto;}
#sb-brand{padding:16px;border-bottom:1px solid #334155;display:flex;align-items:center;gap:10px;cursor:pointer;}
#sb-brand-icon{font-size:22px;}
#sb-brand-name{color:#38bdf8;font-weight:700;font-size:14px;}
#sb-brand-sub{color:#475569;font-size:10px;}
.sb-sec{padding:12px 12px 3px;font-size:10px;font-weight:600;color:#475569;letter-spacing:1.5px;text-transform:uppercase;}
.sb-item{display:flex;align-items:center;gap:9px;padding:9px 14px;color:#94a3b8;cursor:pointer;border-left:3px solid transparent;font-size:13px;font-weight:500;transition:all .12s;}
.sb-item:hover{background:#334155;color:#e2e8f0;}
.sb-item.active{background:#0f172a;color:#38bdf8;border-left-color:#38bdf8;}
.sb-item .ico{font-size:14px;width:18px;text-align:center;flex-shrink:0;}
.sb-badge{margin-left:auto;background:#0f172a;color:#475569;font-size:10px;padding:1px 6px;border-radius:10px;}
.sb-item.active .sb-badge{background:#1e3a5f;color:#38bdf8;}
.sb-divider{height:1px;background:#334155;margin:5px 12px;}
#sb-foot{margin-top:auto;padding:12px 14px;border-top:1px solid #334155;font-size:11px;color:#64748b;}
#sb-foot strong{color:#94a3b8;display:block;font-size:12px;margin-bottom:2px;}
#main{flex:1;display:flex;flex-direction:column;overflow:hidden;}
#topbar{height:56px;background:#fff;border-bottom:1px solid #e2e8f0;display:flex;align-items:center;padding:0 20px;gap:12px;flex-shrink:0;box-shadow:0 1px 3px rgba(0,0,0,.05);}
#tb-title{font-size:17px;font-weight:700;color:#1e293b;display:flex;align-items:center;gap:8px;white-space:nowrap;}
#tb-right{margin-left:auto;display:flex;align-items:center;gap:10px;}
.cl-wrap{position:relative;}
.cl-pill{display:flex;align-items:center;gap:7px;padding:6px 12px;background:#f8fafc;border:1px solid #e2e8f0;border-radius:6px;cursor:pointer;font-size:13px;font-weight:500;user-select:none;white-space:nowrap;}
.cl-pill:hover{border-color:#38bdf8;}
.cl-pill .arr{color:#94a3b8;font-size:10px;margin-left:2px;}
.cl-dd{position:absolute;top:calc(100%+4px);left:0;min-width:230px;background:#fff;border:1px solid #e2e8f0;border-radius:8px;box-shadow:0 6px 24px rgba(0,0,0,.1);z-index:300;display:none;}
.cl-dd.open{display:block;}
.cl-dd-item{padding:10px 14px;cursor:pointer;font-size:13px;color:#475569;border-bottom:1px solid #f1f5f9;display:flex;align-items:center;gap:9px;}
.cl-dd-item:hover{background:#f8fafc;color:#1e293b;}
.cl-dd-item.active{color:#38bdf8;font-weight:600;}
.cl-dd-manage{padding:9px 14px;cursor:pointer;font-size:12px;color:#38bdf8;font-weight:600;border-top:1px solid #f1f5f9;}
.cl-dd-manage:hover{background:#f0f9ff;}
#ns-sel{padding:6px 10px;border:1px solid #e2e8f0;border-radius:6px;font-family:inherit;font-size:13px;color:#1e293b;background:#f8fafc;outline:none;cursor:pointer;max-width:180px;}
#ns-sel:focus{border-color:#38bdf8;}
#ns-pill{display:none;padding:3px 10px;border-radius:20px;font-size:11px;font-weight:600;}
.btn{padding:6px 14px;border-radius:6px;cursor:pointer;font-family:inherit;font-size:13px;font-weight:500;border:1px solid #e2e8f0;background:#fff;color:#475569;transition:all .12s;}
.btn:hover{border-color:#38bdf8;color:#38bdf8;}
.btn-primary{background:#38bdf8;color:#fff;border-color:#38bdf8;}
.btn-primary:hover{background:#0ea5e9;}
.btn-danger{background:#fee2e2;color:#dc2626;border-color:#fca5a5;}
.btn-danger:hover{background:#fecaca;}
.btn-success{background:#d1fae5;color:#059669;border-color:#6ee7b7;}
.btn-warn{background:#fef3c7;color:#d97706;border-color:#fcd34d;}
.btn-warn:hover{background:#fde68a;}
#toast-wrap{position:fixed;bottom:22px;right:22px;z-index:9999;display:flex;flex-direction:column;gap:8px;pointer-events:none;}
.toast{padding:10px 16px;border-radius:8px;font-size:13px;font-weight:500;box-shadow:0 4px 16px rgba(0,0,0,.15);opacity:0;transform:translateY(8px);transition:all .25s;pointer-events:none;max-width:340px;}
.toast.show{opacity:1;transform:translateY(0);}
.toast-ok{background:#d1fae5;color:#059669;border:1px solid #6ee7b7;}
.toast-err{background:#fee2e2;color:#dc2626;border:1px solid #fca5a5;}
.toast-info{background:#e0f2fe;color:#0369a1;border:1px solid #7dd3fc;}
.act-wrap{position:relative;display:inline-block;}
.act-btn{background:none;border:none;cursor:pointer;padding:3px 7px;border-radius:5px;font-size:16px;color:#94a3b8;line-height:1;transition:all .12s;}
.act-btn:hover{background:#f1f5f9;color:#475569;}
.act-menu{position:absolute;right:0;top:100%;min-width:160px;background:#fff;border:1px solid #e2e8f0;border-radius:8px;box-shadow:0 6px 20px rgba(0,0,0,.12);z-index:500;display:none;overflow:hidden;}
.act-menu.open{display:block;}
.act-item{display:flex;align-items:center;gap:8px;padding:9px 14px;font-size:13px;cursor:pointer;color:#475569;transition:background .1s;white-space:nowrap;}
.act-item:hover{background:#f8fafc;}
.act-item.danger{color:#dc2626;}
.act-item.danger:hover{background:#fee2e2;}
.ar-bar{display:flex;align-items:center;gap:10px;padding:8px 0 12px;font-size:12px;color:#64748b;}
.ar-dot{width:8px;height:8px;border-radius:50%;background:#10b981;animation:ar-pulse 2s infinite;}
@keyframes ar-pulse{0%,100%{opacity:1;}50%{opacity:.3;}}
.ar-badge{background:#d1fae5;color:#059669;border-radius:20px;padding:2px 9px;font-size:11px;font-weight:600;}
.btn-sm{padding:4px 10px;font-size:12px;}
#content{flex:1;overflow-y:auto;padding:20px 22px;}
.dot{width:8px;height:8px;border-radius:50%;display:inline-block;flex-shrink:0;}
.dg{background:#10b981;}.dy{background:#f59e0b;}.dr{background:#ef4444;}.db{background:#3b82f6;}.dz{background:#94a3b8;}
.badge{display:inline-flex;align-items:center;padding:2px 9px;border-radius:20px;font-size:11px;font-weight:600;}
.b-green{background:#d1fae5;color:#059669;}.b-yellow{background:#fef3c7;color:#d97706;}
.b-red{background:#fee2e2;color:#dc2626;}.b-blue{background:#dbeafe;color:#2563eb;}
.b-cyan{background:#e0f2fe;color:#0369a1;}.b-gray{background:#f1f5f9;color:#64748b;}
.b-purple{background:#ede9fe;color:#7c3aed;}
.stat-row{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:12px;margin-bottom:20px;}
.stat-card{background:#fff;border-radius:10px;padding:14px 16px;display:flex;align-items:center;gap:12px;box-shadow:0 1px 3px rgba(0,0,0,.06);border:1px solid #f1f5f9;}
.stat-icon{width:40px;height:40px;border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:18px;flex-shrink:0;}
.si-blue{background:#e0f2fe;}.si-green{background:#d1fae5;}.si-yellow{background:#fef3c7;}
.si-red{background:#fee2e2;}.si-purple{background:#ede9fe;}.si-gray{background:#f1f5f9;}
.stat-val{font-size:22px;font-weight:700;color:#1e293b;line-height:1;}
.stat-label{font-size:11px;color:#64748b;margin-top:2px;}
.stat-sub{font-size:10px;margin-top:1px;}
.card{background:#fff;border-radius:10px;border:1px solid #e2e8f0;padding:18px 20px;box-shadow:0 1px 3px rgba(0,0,0,.04);}
.cl-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px;margin-bottom:20px;}
.cl-card{background:#fff;border-radius:10px;border:1px solid #e2e8f0;padding:18px;box-shadow:0 1px 3px rgba(0,0,0,.05);transition:border .15s;}
.cl-card:hover{border-color:#38bdf8;}
.cl-card.error-card{border-color:#fca5a5;background:#fffafa;}
.cl-card.error-card:hover{border-color:#f87171;}
.cl-err-banner{background:#fff5f5;border:1px solid #fecaca;border-radius:6px;padding:8px 10px;margin-bottom:10px;font-size:12px;color:#dc2626;display:flex;align-items:flex-start;gap:6px;}
.cl-card-head{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:10px;}
.cl-card-name{font-size:15px;font-weight:700;color:#1e293b;}
.cl-card-desc{font-size:11px;color:#94a3b8;margin-top:2px;}
.cl-card-meta{display:grid;grid-template-columns:90px 1fr;gap:3px 6px;font-size:12px;margin-bottom:12px;min-height:16px;}
.mk{color:#94a3b8;}.mv{color:#475569;word-break:break-all;}
.cl-card-stats{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-bottom:12px;}
.cl-st{background:#f8fafc;border-radius:6px;padding:8px 10px;text-align:center;}
.cl-st-val{font-size:18px;font-weight:700;color:#1e293b;}
.cl-st-label{font-size:10px;color:#94a3b8;margin-top:1px;}
.cl-card-actions{display:flex;gap:8px;flex-wrap:wrap;}
.pill{display:inline-flex;align-items:center;gap:4px;padding:3px 9px;border-radius:20px;font-size:11px;font-weight:600;}
.pill-ok{background:#d1fae5;color:#059669;}.pill-err{background:#fee2e2;color:#dc2626;}.pill-unk{background:#f1f5f9;color:#64748b;}
.res-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(190px,1fr));gap:12px;}
.res-card{background:#fff;border-radius:10px;border:1px solid #e2e8f0;padding:15px 17px;cursor:pointer;transition:all .15s;box-shadow:0 1px 3px rgba(0,0,0,.04);}
.res-card:hover{border-color:#38bdf8;box-shadow:0 2px 8px rgba(56,189,248,.15);transform:translateY(-1px);}
.res-card-head{display:flex;align-items:center;gap:9px;margin-bottom:5px;}
.res-card-icon{font-size:18px;}
.res-card-name{font-size:12px;font-weight:600;color:#64748b;}
.res-card-count{font-size:24px;font-weight:700;margin-bottom:2px;}
.res-card-sub{font-size:11px;color:#94a3b8;}
.rt-wrap{background:#fff;border-radius:10px;border:1px solid #e2e8f0;overflow:hidden;box-shadow:0 1px 3px rgba(0,0,0,.04);margin-bottom:16px;}
.rt-hdr{display:grid;padding:9px 14px;background:#f8fafc;border-bottom:1px solid #e2e8f0;font-size:10px;font-weight:600;color:#64748b;letter-spacing:.4px;text-transform:uppercase;}
.rt-row{display:grid;padding:11px 14px;border-bottom:1px solid #f1f5f9;align-items:center;font-size:13px;cursor:pointer;transition:background .1s;}
.rt-row:last-child{border-bottom:none;}
.rt-row:hover{background:#f8fafc;}
.rt-name{font-weight:600;color:#1e293b;}
.det-card{background:#fff;border-radius:10px;border:1px solid #e2e8f0;padding:18px 20px;margin-bottom:12px;box-shadow:0 1px 3px rgba(0,0,0,.04);}
.det-title{font-size:16px;font-weight:700;color:#1e293b;margin-bottom:12px;padding-bottom:10px;border-bottom:1px solid #f1f5f9;display:flex;align-items:center;gap:9px;flex-wrap:wrap;}
.det-sec{font-size:10px;font-weight:600;color:#94a3b8;letter-spacing:1px;text-transform:uppercase;margin-bottom:8px;}
.kv{display:grid;grid-template-columns:minmax(120px,340px) 1fr;gap:5px 14px;font-size:13px;}
.kk{color:#94a3b8;word-break:break-word;overflow-wrap:break-word;min-width:0;}
.kv2{color:#1e293b;word-break:break-word;overflow-wrap:break-word;min-width:0;}
.cont-card{background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:12px;margin-bottom:8px;}
.cont-name{font-size:13px;font-weight:700;color:#1e293b;margin-bottom:7px;}
.warn-tag{color:#d97706;font-size:11px;font-weight:500;}
.ev-row{display:grid;grid-template-columns:65px 60px 110px 1fr;gap:8px;font-size:12px;padding:5px 0;border-bottom:1px solid #f1f5f9;}
.ev-w{color:#dc2626;}.ev-n{color:#0369a1;}.ev-a{color:#94a3b8;}.ev-r{color:#d97706;}.ev-m{color:#475569;}
.log-box{background:#0f172a;border-radius:8px;padding:12px 14px;max-height:380px;overflow-y:auto;font-size:11px;line-height:1.7;font-family:'Courier New',Courier,monospace;display:none;margin-top:8px;}
.log-box.show{display:block;}
.le{color:#f87171;}.lw{color:#fbbf24;}.li{color:#94a3b8;}
table{width:100%;border-collapse:collapse;font-size:13px;}
th{text-align:left;padding:7px 10px;font-size:10px;font-weight:600;color:#64748b;letter-spacing:.4px;text-transform:uppercase;border-bottom:1px solid #e2e8f0;background:#f8fafc;}
td{padding:9px 10px;border-bottom:1px solid #f1f5f9;color:#475569;}
tr:hover td{background:#f8fafc;}
.cm-key{font-size:12px;font-weight:600;color:#d97706;margin-bottom:3px;}
.cm-val{background:#0f172a;border-radius:6px;padding:9px;font-size:11px;color:#94a3b8;white-space:pre-wrap;max-height:160px;overflow-y:auto;margin-bottom:10px;font-family:'Courier New',Courier,monospace;}
.form-row{margin-bottom:13px;}
.form-label{display:block;font-size:11px;font-weight:600;color:#374151;margin-bottom:5px;text-transform:uppercase;letter-spacing:.5px;}
.form-input{width:100%;padding:8px 11px;border:1px solid #e2e8f0;border-radius:6px;font-family:inherit;font-size:13px;color:#1e293b;outline:none;transition:border .12s;}
.form-input:focus{border-color:#38bdf8;box-shadow:0 0 0 3px rgba(56,189,248,.1);}
.form-hint{font-size:11px;color:#94a3b8;margin-top:4px;}
.form-msg{padding:9px 12px;border-radius:6px;font-size:13px;margin-bottom:12px;}
.fm-ok{background:#d1fae5;color:#059669;border:1px solid #6ee7b7;}
.fm-err{background:#fee2e2;color:#dc2626;border:1px solid #fca5a5;}
.fm-info{background:#e0f2fe;color:#0369a1;border:1px solid #7dd3fc;}
.drop-zone{border:2px dashed #cbd5e1;border-radius:8px;padding:22px;text-align:center;cursor:pointer;transition:all .2s;background:#f8fafc;}
.drop-zone:hover,.drop-zone.drag{border-color:#38bdf8;background:#f0f9ff;}
.dz-icon{font-size:28px;margin-bottom:6px;}
.dz-text{font-size:13px;color:#475569;font-weight:500;}
.dz-sub{font-size:11px;color:#94a3b8;margin-top:3px;}
.dz-ok{font-size:12px;color:#059669;font-weight:600;margin-top:5px;display:none;}
#add-form-toggle{display:flex;align-items:center;gap:8px;padding:10px 14px;background:#f0f9ff;border:1px solid #bae6fd;border-radius:8px;cursor:pointer;font-size:13px;font-weight:600;color:#0369a1;margin-bottom:14px;transition:background .15s;user-select:none;}
#add-form-toggle:hover{background:#e0f2fe;}
#add-form-toggle .tarr{margin-left:auto;transition:transform .2s;}
#add-form-toggle.open .tarr{transform:rotate(180deg);}
#add-form-body{display:none;}
#add-form-body.open{display:block;}
.node-wrap{background:#fff;border-radius:10px;border:1px solid #e2e8f0;overflow:hidden;box-shadow:0 1px 3px rgba(0,0,0,.04);margin-top:16px;}
.node-title{padding:12px 16px;background:#f8fafc;border-bottom:1px solid #e2e8f0;font-size:13px;font-weight:700;color:#1e293b;display:flex;align-items:center;justify-content:space-between;}
.spin{display:inline-block;width:13px;height:13px;border:2px solid #e2e8f0;border-top-color:#38bdf8;border-radius:50%;animation:_sp .7s linear infinite;margin-right:7px;vertical-align:middle;}
@keyframes _sp{to{transform:rotate(360deg);}}
.loading{color:#94a3b8;font-size:13px;padding:18px 0;display:flex;align-items:center;}
.empty{display:flex;flex-direction:column;align-items:center;justify-content:center;padding:60px;color:#94a3b8;}
.empty-icon{font-size:48px;margin-bottom:12px;opacity:.3;}
.ph{margin-bottom:20px;}
.ph h1{font-size:20px;font-weight:700;color:#1e293b;}
.ph p{color:#64748b;font-size:13px;margin-top:3px;}
::-webkit-scrollbar{width:5px;height:5px;}
::-webkit-scrollbar-track{background:#f1f5f9;}
::-webkit-scrollbar-thumb{background:#cbd5e1;border-radius:3px;}
"""

_JS = r"""
/* State */
const S = {cluster:null, namespace:null, data:{}, resType:null, page:'overview', nodesCluster:null};
let _kcData=null, _logRaw=[], _logPodNs=null, _logErrOnly=false;
let _detType=null, _detName=null;

/* Utils */
function esc(s){return String(s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function enc(s){return encodeURIComponent(s||'');}
function bold(s){return '<span class="rt-name">'+esc(s)+'</span>';}

async function GET(url){
  const r = await fetch(url, {cache:'no-store'});
  if(!r.ok) throw new Error(await r.text());
  return r.json();
}

async function POST(url){
  const r = await fetch(url, {method:'POST', cache:'no-store'});
  if(!r.ok) throw new Error(await r.text());
  return r.json();
}

async function DELETE(url){
  const r = await fetch(url, {method:'DELETE', cache:'no-store'});
  if(!r.ok) throw new Error(await r.text());
  return r.json();
}

function toast(msg, type){
  type = type || 'ok';
  const wrap = document.getElementById('toast-wrap');
  if(!wrap) return;
  const el = document.createElement('div');
  el.className = 'toast toast-'+type;
  el.textContent = msg;
  wrap.appendChild(el);
  requestAnimationFrame(()=>{ requestAnimationFrame(()=>{ el.classList.add('show'); }); });
  setTimeout(()=>{ el.classList.remove('show'); setTimeout(()=>el.remove(), 300); }, 3800);
}

/* Action menu — 3-dot */
function actMenu(items){
  var btns = items.map(function(it){
    var safeArgs = it.args.map(function(a){
      // store in data-* to avoid ALL inline escaping issues
      return '';
    });
    // We encode args as JSON in a data attribute, read by dispatcher
    var argsJson = JSON.stringify(it.args.map(String)).replace(/"/g,'&quot;');
    return '<div class="act-item'+(it.danger?' danger':'')+
      '" data-fn="'+it.fn+'" data-args="'+argsJson+
      '" onclick="handleActClick(event,this)">'+it.label+'</div>';
  }).join('');
  return '<div class="act-wrap">'+
    '<button class="act-btn" onclick="toggleActMenu(event,this.parentElement)" title="Actions">&#8943;</button>'+
    '<div class="act-menu">'+btns+'</div>'+
    '</div>';
}

function handleActClick(e, el){
  e.stopPropagation();
  var fn   = el.getAttribute('data-fn');
  var args = JSON.parse((el.getAttribute('data-args')||'[]').replace(/&quot;/g,'"'));
  var wrap = el.closest('.act-wrap');
  // close menu
  if(wrap){ wrap.querySelector('.act-menu').classList.remove('open'); _openMenu=null; }
  var fns = {
    restartPod:       function(){ doRestartPod(args[0], args[1]); },
    restartDep:       function(){ doRestartDep(args[0], args[1]); },
    restartSts:       function(){ doRestartSts(args[0], args[1]); },
    deletePod:        function(){ doDeletePod(args[0], args[1]); },
    deleteDeployment: function(){ doDeleteDeployment(args[0], args[1]); },
    deleteStatefulSet:function(){ doDeleteStatefulSet(args[0], args[1]); },
  };
  if(fns[fn]) fns[fn]();
}

let _openMenu = null;
document.addEventListener('click', e=>{
  if(_openMenu && !_openMenu.contains(e.target)){
    _openMenu.querySelector('.act-menu').classList.remove('open');
    _openMenu = null;
  }
});
function toggleActMenu(e, wrap){
  e.stopPropagation();
  const menu = wrap.querySelector('.act-menu');
  const wasOpen = menu.classList.contains('open');
  if(_openMenu && _openMenu !== wrap){
    _openMenu.querySelector('.act-menu').classList.remove('open');
  }
  menu.classList.toggle('open', !wasOpen);
  _openMenu = !wasOpen ? wrap : null;
}
function closeMenu(wrap){ wrap.querySelector('.act-menu').classList.remove('open'); _openMenu=null; }

/* Delete actions */
/* ── Action handlers called by handleActClick dispatcher ── */
async function doRestartPod(podName, podNs){
  if(!confirm('Restart pod "'+podName+'"?\n\nThe pod will be deleted and recreated by its controller.')) return;
  toast('⏳ Restarting pod '+podName+'...', 'info');
  try{
    const d = await POST('/api/'+enc(S.cluster)+'/'+enc(podNs)+'/pods/'+enc(podName)+'/restart');
    if(d.ok){
      toast('✅ '+d.message, 'ok');
      // Go back to list if on detail page, then refresh
      if(S.page==='detail' && _detName===podName){ goBack(); }
      // Fetch fresh pod list after 2s (pod will be terminating/recreating)
      setTimeout(()=>silentRefreshPodsForce(), 2000);
    } else toast('❌ '+(d.error||'Failed'), 'err');
  } catch(e){ toast('❌ '+e.message, 'err'); }
}

async function doRestartDep(name, ns){
  if(!confirm('Rollout restart deployment "'+name+'"?\n\nPods will be cycled one by one.')) return;
  toast('⏳ Restarting deployment '+name+'...', 'info');
  try{
    const d = await POST('/api/'+enc(S.cluster)+'/'+enc(ns)+'/deployments/'+enc(name)+'/restart');
    if(d.ok) toast('✅ '+d.message, 'ok');
    else     toast('❌ '+(d.error||'Failed'), 'err');
  } catch(e){ toast('❌ '+e.message, 'err'); }
}

async function doRestartSts(name, ns){
  if(!confirm('Rollout restart statefulset "'+name+'"?\n\nPods will be cycled according to update strategy.')) return;
  toast('⏳ Restarting statefulset '+name+'...', 'info');
  try{
    const d = await POST('/api/'+enc(S.cluster)+'/'+enc(ns)+'/statefulsets/'+enc(name)+'/restart');
    if(d.ok) toast('✅ '+d.message, 'ok');
    else     toast('❌ '+(d.error||'Failed'), 'err');
  } catch(e){ toast('❌ '+e.message, 'err'); }
}

async function doDeletePod(podName, podNs){
  if(!confirm('Delete pod "'+podName+'"?\n\nIt will be permanently deleted. If managed by a controller it will be recreated.')) return;
  toast('⏳ Deleting pod '+podName+'...', 'info');
  try{
    const d = await DELETE('/api/'+enc(S.cluster)+'/'+enc(podNs)+'/pods/'+enc(podName));
    if(d.ok){
      toast('🗑️ '+d.message, 'ok');
      // Immediately remove from local list
      S.data.pods = (S.data.pods||[]).filter(x=>x.name!==podName);
      // If viewing pods list, re-render immediately
      if(S.page==='resource' && S.resType==='pods') preserveScrollRenderPods();
      // If viewing this pod's detail, go back to list
      if(S.page==='detail' && _detName===podName){ goBack(); }
      // Then fetch fresh list from server after 2s (controller may recreate it)
      setTimeout(()=>silentRefreshPodsForce(), 2000);
    } else toast('❌ '+(d.error||'Failed'), 'err');
  } catch(e){ toast('❌ '+e.message, 'err'); }
}

async function doDeleteDeployment(name, ns){
  if(!confirm('DELETE deployment "'+name+'"?\n\n⚠️ This will remove the deployment and ALL its pods!')) return;
  toast('⏳ Deleting deployment '+name+'...', 'info');
  try{
    const d = await DELETE('/api/'+enc(S.cluster)+'/'+enc(ns)+'/deployments/'+enc(name));
    if(d.ok){
      toast('🗑️ '+d.message, 'ok');
      S.data.deployments = (S.data.deployments||[]).filter(x=>x.name!==name);
      if(S.resType==='deployments') renderResList('deployments');
    } else toast('❌ '+(d.error||'Failed'), 'err');
  } catch(e){ toast('❌ '+e.message, 'err'); }
}

async function doDeleteStatefulSet(name, ns){
  if(!confirm('DELETE statefulset "'+name+'"?\n\n⚠️ This will remove the statefulset and ALL its pods!')) return;
  toast('⏳ Deleting statefulset '+name+'...', 'info');
  try{
    const d = await DELETE('/api/'+enc(S.cluster)+'/'+enc(ns)+'/statefulsets/'+enc(name));
    if(d.ok){
      toast('🗑️ '+d.message, 'ok');
      S.data.statefulsets = (S.data.statefulsets||[]).filter(x=>x.name!==name);
      if(S.resType==='statefulsets') renderResList('statefulsets');
    } else toast('❌ '+(d.error||'Failed'), 'err');
  } catch(e){ toast('❌ '+e.message, 'err'); }
}

/* Legacy wrappers for detail-panel buttons (btn, name, ns) */
async function restartPod(btn, podName, podNs){ doRestartPod(podName, podNs); }
async function restartDep(btn, name, ns)      { doRestartDep(name, ns); }
async function restartSts(btn, name, ns)      { doRestartSts(name, ns); }

/* ── Auto-refresh for pods list ── */
let _arTick      = null;
let _arInterval  = 2;   /* seconds between refreshes */
let _arCountdown = 0;
let _arEnabled   = false;

function startAutoRefresh(){
  stopAutoRefresh();
  _arEnabled   = true;
  _arCountdown = _arInterval;
  _arTick = setInterval(()=>{
    _arCountdown--;
    const el = document.getElementById('ar-next');
    if(el) el.textContent = _arCountdown+'s';
    if(_arCountdown <= 0){
      _arCountdown = _arInterval;
      silentRefreshPods();
    }
  }, 1000);
}

function stopAutoRefresh(){
  _arEnabled = false;
  if(_arTick){ clearInterval(_arTick); _arTick=null; }
}

async function silentRefreshPods(){
  // Auto-refresh tick: only when actively viewing pods list
  if(!S.cluster||!S.namespace||S.page!=='resource'||S.resType!=='pods') return;
  await silentRefreshPodsForce();
}

async function silentRefreshPodsForce(){
  // Force-refresh pods data regardless of current page
  if(!S.cluster||!S.namespace) return;
  const isAll = S.namespace==='__all__';
  const base = isAll
    ? '/api/'+enc(S.cluster)+'/__all__'
    : '/api/'+enc(S.cluster)+'/'+enc(S.namespace);
  try{
    const fresh = await GET(base+'/pods');
    S.data.pods = fresh;
    // Only re-render if currently viewing pods list
    if(S.page==='resource' && S.resType==='pods') preserveScrollRenderPods();
  } catch(e){ /* silent */ }
}

function preserveScrollRenderPods(){
  const el = document.getElementById('page-resource');
  const scrollY = el ? el.scrollTop : 0;
  renderResList('pods');
  if(el) el.scrollTop = scrollY;
}



function badge(label){
  const m={healthy:'b-green',running:'b-green',bound:'b-green',available:'b-cyan',
           degraded:'b-yellow',pending:'b-yellow',released:'b-yellow',
           failed:'b-red',unhealthy:'b-red',lost:'b-red'};
  return '<span class="badge '+(m[label]||'b-gray')+'">'+esc(label)+'</span>';
}

function evHtml(evs){
  if(!evs||!evs.length) return '<p style="color:#94a3b8;font-size:12px;padding:6px 0">No events</p>';
  let h='<div style="font-size:11px;color:#94a3b8;margin-bottom:6px">'+evs.length+' event'+(evs.length!==1?'s':'')+' — newest first</div>'+
    '<div class="ev-row" style="font-weight:600;color:#94a3b8"><span>TYPE</span><span>AGE</span><span>REASON</span><span>MESSAGE</span></div>';
  evs.forEach(e=>{
    h+='<div class="ev-row"><span class="'+(e.type==='Warning'?'ev-w':'ev-n')+'">'+e.type+'</span><span class="ev-a">'+esc(e.age)+'</span><span class="ev-r">'+esc(e.reason)+'</span><span class="ev-m">'+esc(e.message)+'</span></div>';
  });
  return h;
}

function ccHtml(c){
  const w=c.warn?'<span class="warn-tag"> ⚠ no limits</span>':'';
  return '<div class="cont-card"><div class="cont-name">'+esc(c.name)+w+'</div><div class="kv">'+
    '<span class="kk">Image</span><span class="kv2">'+esc(c.image)+'</span>'+
    (c.state!==undefined?'<span class="kk">State</span><span class="kv2">'+esc(c.state)+'</span>':'')+
    (c.restarts!==undefined?'<span class="kk">Restarts</span><span class="kv2" style="color:'+(c.restarts>3?'#dc2626':'inherit')+'">'+c.restarts+'</span>':'')+
    (c.ready!==undefined?'<span class="kk">Ready</span><span class="kv2">'+(c.ready?'✓':'✗')+'</span>':'')+
    '<span class="kk">CPU req/lim</span><span class="kv2 '+(String(c.req_cpu||'').includes('⚠')?'warn-tag':'')+'">'+esc(c.req_cpu||'—')+' / '+esc(c.lim_cpu||'—')+'</span>'+
    '<span class="kk">Mem req/lim</span><span class="kv2 '+(String(c.req_memory||'').includes('⚠')?'warn-tag':'')+'">'+esc(c.req_memory||'—')+' / '+esc(c.lim_memory||'—')+'</span>'+
    '</div></div>';
}

/* Cluster dropdown */
function toggleDD(id){document.getElementById(id).classList.toggle('open');}
document.addEventListener('click',e=>{
  document.querySelectorAll('.cl-dd').forEach(d=>{
    if(!d.parentElement.contains(e.target)) d.classList.remove('open');
  });
});

async function loadDD(){
  try{
    const cls=await GET('/api/clusters');
    const el=document.getElementById('cl-dd-body');
    if(!cls.length){el.innerHTML='<div class="cl-dd-item" style="color:#94a3b8">No clusters yet</div>';return;}
    el.innerHTML=cls.map(c=>
      '<div class="cl-dd-item'+(c.name===S.cluster?' active':'')+'" onclick="pickCluster(\''+esc(c.name)+'\')">'+
      '<span class="dot '+(c.status==='connected'?'dg':c.status==='error'?'dr':'dy')+'"></span>'+
      '<span>'+esc(c.name)+'</span></div>'
    ).join('');
  }catch(e){}
}

async function pickCluster(name){
  document.querySelectorAll('.cl-dd').forEach(d=>d.classList.remove('open'));
  S.cluster=name; S.namespace=null; S.data={};
  document.getElementById('cl-pill-label').textContent=name;
  document.getElementById('cl-dot').className='dot dy';
  document.getElementById('sb-cl').textContent=name;
  document.getElementById('sb-ns').textContent='—';
  updateBadges(null); setNsPill(null);
  const sel=document.getElementById('ns-sel');
  sel.innerHTML='<option>Loading namespaces...</option>';
  try{
    const d=await GET('/api/'+enc(name)+'/namespaces');
    sel.innerHTML='<option value="">— select namespace —</option>'+
      '<option value="__all__">⬡ All Namespaces</option>'+
      '<option disabled>──────────────</option>'+
      d.namespaces.map(n=>'<option value="'+n+'">'+n+'</option>').join('');
    document.getElementById('cl-dot').className='dot dg';
  }catch(e){
    sel.innerHTML='<option>Error loading namespaces</option>';
    document.getElementById('cl-dot').className='dot dr';
  }
  loadDD();
}

function onNsChange(ns){
  if(!S.cluster||!ns) return;
  S.namespace=ns;
  document.getElementById('sb-ns').textContent=ns==='__all__'?'⬡ All Namespaces':ns;
  setNsPill(ns);
  showPage('ns-dashboard');
}

function setNsPill(ns){
  const el=document.getElementById('ns-pill');
  if(!ns){el.style.display='none';return;}
  el.style.display='inline-flex';
  if(ns==='__all__'){el.textContent='⬡ All Namespaces';el.className='badge b-cyan';}
  else{el.textContent=ns;el.className='badge b-gray';}
}

/* Page routing */
const PAGES=['overview','clusters','ns-dashboard','resource','detail','nodes'];
function showPage(id){
  S.page=id;
  PAGES.forEach(p=>document.getElementById('page-'+p).style.display=p===id?'block':'none');
  document.querySelectorAll('.sb-item').forEach(el=>el.classList.remove('active'));
  const nav=document.getElementById('nav-'+id);
  if(nav) nav.classList.add('active');
  const T={
    'overview':     ['🏠','Cluster Overview'],
    'clusters':     ['⚙️','Cluster Management'],
    'ns-dashboard': ['📊','Namespace Dashboard'],
    'resource':     ['📋', S.resType||'Resources'],
    'detail':       ['🔍','Detail'],
    'nodes':        ['🖥️','Nodes'],
  };
  const [icon,label]=T[id]||['📋',id];
  document.getElementById('tb-icon').textContent=icon;
  document.getElementById('tb-label').textContent=label;
  if(id!=='resource') stopAutoRefresh();
  if(id==='overview')   loadOverview();
  if(id==='clusters')   loadClusterMgmt();
  if(id==='ns-dashboard'&&S.cluster&&S.namespace) loadNsDashboard();
}

const RES_META={
  pods:        {icon:'🟢',label:'Pods'},
  deployments: {icon:'🚀',label:'Deployments'},
  statefulsets:{icon:'💾',label:'StatefulSets'},
  services:    {icon:'🌐',label:'Services'},
  pvcs:        {icon:'💿',label:'Persistent Volume Claims'},
  pvs:         {icon:'🗄️',label:'Persistent Volumes'},
  configmaps:  {icon:'📋',label:'ConfigMaps'},
  secrets:     {icon:'🔑',label:'Secrets'},
  ingresses:   {icon:'🔀',label:'Ingresses'},
  events:      {icon:'📣',label:'Events'},
};

function goRes(type){
  S.resType=type;
  S.page='resource';
  PAGES.forEach(p=>document.getElementById('page-'+p).style.display=p==='resource'?'block':'none');
  document.querySelectorAll('.sb-item').forEach(el=>el.classList.remove('active'));
  const nav=document.getElementById('nav-'+type);
  if(nav) nav.classList.add('active');
  document.getElementById('tb-icon').textContent=RES_META[type]?.icon||'📋';
  document.getElementById('tb-label').textContent=RES_META[type]?.label||type;
  renderResList(type);
  if(type==='pods'){ startAutoRefresh(); }
  else { stopAutoRefresh(); }
}

function goBack(){
  if(S.resType) goRes(S.resType);
  else showPage('ns-dashboard');
}

function updateBadges(s){
  const m={'sc-pods':s?.pods?.total,'sc-dep':s?.deployments,'sc-sts':s?.statefulsets,
           'sc-svc':s?.services,'sc-pvc':s?.pvcs,'sc-pv':s?.pvs,
           'sc-cm':s?.configmaps,'sc-sec':s?.secrets,'sc-ing':s?.ingresses,'sc-evt':null};
  Object.entries(m).forEach(([id,v])=>{const el=document.getElementById(id);if(el)el.textContent=v??'—';});
}

/* ══ Smart Refresh ══════════════════════════ */
async function refreshAll(){
  // Update cluster dot status
  if(S.cluster){
    GET('/api/clusters/'+enc(S.cluster)+'/status').then(s=>{
      const dot=document.getElementById('cl-dot');
      if(dot) dot.className='dot '+(s.status==='connected'?'dg':'dr');
    }).catch(()=>{});
  }
  const page=S.page||'overview';
  if(page==='overview')   { loadOverview(); return; }
  if(page==='clusters')   { loadClusterMgmt(); return; }
  if(page==='nodes')      { if(S.nodesCluster) viewNodes(S.nodesCluster); return; }
  if(!S.cluster||!S.namespace) { loadOverview(); return; }
  if(page==='ns-dashboard') { await loadNsDashboard(); return; }
  if(page==='resource')   { await loadNsDashboard(); renderResList(S.resType); return; }
  if(page==='detail'){
    await loadNsDashboard();
    if(_detType&&_detName){
      const item=(S.data[_detType]||[]).find(x=>x.name===_detName);
      if(item){
        const renders={pods:renderPod,deployments:renderDep,statefulsets:renderSts,
                       services:renderSvc,pvcs:renderPvc,pvs:renderPv,
                       configmaps:renderCm,secrets:renderSec,ingresses:renderIng};
        if(renders[_detType]) renders[_detType](item);
        if(_detType==='pods'){
          const evNs=item.namespace||(S.namespace!=='__all__'?S.namespace:'');
          if(evNs) refreshEvents(_detName,evNs);
          const lb=document.getElementById('log-box');
          if(lb&&lb.classList.contains('show')&&_logPodNs) fetchLogs(_detName,_logPodNs);
        }
      }
    }
  }
}

/* ══ Cluster Overview ══════════════════════ */
async function loadOverview(){
  const el=document.getElementById('page-overview');
  el.innerHTML='<div class="loading"><span class="spin"></span>Loading...</div>';
  let cls;
  try{
    cls=await GET('/api/clusters');
  }catch(e){
    el.innerHTML='<div class="empty"><div class="empty-icon">🔌</div>'+
      '<p style="font-weight:700;color:#dc2626;margin-bottom:6px">Cannot connect to backend</p>'+
      '<p style="font-size:12px;color:#94a3b8;max-width:380px;margin:0 auto 14px">'+esc(e.message)+'</p>'+
      '<button class="btn btn-primary" onclick="loadOverview()">↻ Retry</button></div>';
    return;
  }
  if(!cls.length){
    el.innerHTML='<div class="empty"><div class="empty-icon">⎈</div>'+
      '<p>No clusters added yet.</p>'+
      '<button class="btn btn-primary" style="margin-top:14px" onclick="showPage(\'clusters\')">Add First Cluster</button></div>';
    return;
  }
  // Render cards immediately
  let html='<div class="ph"><h1>🏠 Cluster Overview</h1>'+
    '<p>'+cls.length+' cluster'+(cls.length>1?'s':'')+' registered &nbsp;·&nbsp; '+
    '<span id="ov-status-lbl" style="color:#94a3b8">checking status...</span></p></div>'+
    '<div class="cl-grid">';
  cls.forEach(c=>{ html+=clCardHtml(c); });
  html+='</div><div style="text-align:right;margin-top:8px">'+
    '<button class="btn" onclick="showPage(\'clusters\')">⚙ Manage Clusters</button></div>';
  el.innerHTML=html;

  // Async status per cluster
  let conn=0,err=0,done=0;
  cls.forEach(c=>{
    if(c.error){ err++; done++; updateOvLabel(conn,err,done,cls.length); return; }
    GET('/api/clusters/'+enc(c.name)+'/status').then(s=>{
      applyClStatus(c.name,s);
      if(s.status==='connected'){ conn++; loadClDeepStats(c.name); }
      else err++;
    }).catch(e=>{
      applyClStatus(c.name,{name:c.name,status:'error',error:e.message});
      err++;
    }).finally(()=>{
      done++;
      updateOvLabel(conn,err,done,cls.length);
    });
  });
}

function updateOvLabel(conn,err,done,total){
  const lbl=document.getElementById('ov-status-lbl');
  if(!lbl) return;
  if(done<total){ lbl.innerHTML='<span style="color:#94a3b8">'+done+'/'+total+' checked...</span>'; return; }
  lbl.innerHTML='<span style="color:#059669">'+conn+' connected</span>'+
    (err>0?' &nbsp;·&nbsp; <span style="color:#dc2626">'+err+' error</span>':'');
}

function clCardHtml(c){
  var errBorder = c.error ? 'border-color:#fca5a5;' : '';
  return '<div class="cl-card" id="cl-card-'+esc(c.name)+'" style="'+errBorder+'">'+
    '<div class="cl-card-head">'+
    '<div><div class="cl-card-name">'+esc(c.name)+'</div><div class="cl-card-desc">'+esc(c.description||'')+'</div></div>'+
    '<span class="pill pill-unk" id="cl-pill-'+esc(c.name)+'">'+(c.error?'✗ No Data':'⏳ Checking...')+'</span>'+
    '</div>'+
    (c.error ? '<div style="background:#fff5f5;border:1px solid #fecaca;border-radius:6px;padding:8px 10px;margin-bottom:10px;font-size:12px;color:#dc2626;display:flex;align-items:flex-start;gap:6px"><span>⚠️</span><span>'+esc(c.error)+'</span></div>' : '') +
    '<div class="cl-card-meta" id="cl-meta-'+esc(c.name)+'">'+(c.error?'':'')+'</div>'+
    '<div class="cl-card-stats" id="cl-stats-'+esc(c.name)+'">'+
    (c.error
      ?'<div class="cl-st" style="grid-column:1/-1;color:#94a3b8;font-size:12px">Unavailable</div>'
      :'<div class="cl-st" style="grid-column:1/-1;color:#94a3b8;font-size:12px"><span class="spin"></span>Loading...</div>')+
    '</div>'+
    '<div class="cl-card-actions" id="cl-act-'+esc(c.name)+'">'+
    '<button class="btn btn-sm" onclick="showPage(\'clusters\')">Manage</button></div>'+
    '</div>';
}

function applyClStatus(name,s){
  const pill=document.getElementById('cl-pill-'+name);
  const meta=document.getElementById('cl-meta-'+name);
  const stats=document.getElementById('cl-stats-'+name);
  const act=document.getElementById('cl-act-'+name);
  if(pill){
    pill.className='pill '+(s.status==='connected'?'pill-ok':'pill-err');
    pill.textContent=s.status==='connected'?'✓ Connected':'✗ Error';
  }
  if(meta){
    if(s.status==='connected')
      meta.innerHTML=(s.cluster?'<span class="mk">Cluster</span><span class="mv">'+esc(s.cluster)+'</span>':'')+
                     (s.version?'<span class="mk">Version</span><span class="mv">'+esc(s.version)+'</span>':'')+
                     (s.namespaces?'<span class="mk">Namespaces</span><span class="mv">'+s.namespaces+'</span>':'');
    else
      meta.innerHTML='<span class="mk">Error</span><span class="mv" style="color:#dc2626">'+esc(s.error||'Connection failed')+'</span>';
  }
  if(stats){
    if(s.status==='connected')
      stats.innerHTML='<div class="cl-st"><div class="cl-st-val" id="cl-n-'+esc(name)+'">—</div><div class="cl-st-label">Nodes</div></div>'+
        '<div class="cl-st"><div class="cl-st-val">'+(s.namespaces||'—')+'</div><div class="cl-st-label">Namespaces</div></div>'+
        '<div class="cl-st"><div class="cl-st-val" id="cl-p-'+esc(name)+'">—</div><div class="cl-st-label">Pods</div></div>'+
        '<div class="cl-st"><div class="cl-st-val" id="cl-d-'+esc(name)+'">—</div><div class="cl-st-label">Deployments</div></div>';
    else
      stats.innerHTML='<div class="cl-st" style="grid-column:1/-1"><div style="display:flex;align-items:center;gap:8px;padding:4px 0"><span style="font-size:18px">⚠️</span><div><div style="font-size:12px;font-weight:600;color:#dc2626">Connection Failed</div><div style="font-size:11px;color:#94a3b8;margin-top:2px;word-break:break-all">'+esc(s.error||'Unable to reach cluster')+'</div></div></div></div>';
  }
  if(act){
    if(s.status==='connected')
      act.innerHTML='<button class="btn btn-primary btn-sm" onclick="openCluster(\''+esc(name)+'\')">Open Dashboard</button>'+
        '<button class="btn btn-sm" onclick="viewNodes(\''+esc(name)+'\')">🖥️ Nodes</button>'+
        '<button class="btn btn-sm" onclick="showPage(\'clusters\')">Manage</button>';
    else
      act.innerHTML='<button class="btn btn-sm" onclick="retryCluster(\''+esc(name)+'\',this)">Retry</button>'+
        '<button class="btn btn-sm" onclick="showPage(\'clusters\')">Manage</button>';
  }
}

async function loadClDeepStats(name){
  try{
    const d=await GET('/api/'+enc(name)+'/overview');
    if(!d.ok) return;
    const n=document.getElementById('cl-n-'+name);
    const p=document.getElementById('cl-p-'+name);
    const dep=document.getElementById('cl-d-'+name);
    if(n) n.innerHTML=d.nodes+'<span style="font-size:10px;color:'+(d.nodes_ready<d.nodes?'#d97706':'#10b981')+'"> /'+d.nodes_ready+'✓</span>';
    if(p) p.innerHTML='<span style="color:'+(d.pods_failed>0?'#dc2626':d.pods_pending>0?'#d97706':'#059669')+'">'+d.pods+'</span>';
    if(dep) dep.innerHTML='<span style="color:'+(d.dep_healthy<d.deployments?'#d97706':'#059669')+'">'+d.deployments+'</span>';
  }catch(e){}
}

async function openCluster(name){
  await pickCluster(name);
  // Default to All Namespaces
  const sel=document.getElementById('ns-sel');
  if(sel){ sel.value='__all__'; onNsChange('__all__'); }
  else showPage('ns-dashboard');
}

async function retryCluster(name,btn){
  btn.textContent='...';
  try{
    const s=await GET('/api/clusters/'+enc(name)+'/status');
    applyClStatus(name,s);
    if(s.status==='connected') loadClDeepStats(name);
    btn.textContent=s.status==='connected'?'✓ OK':'✗ Fail';
    setTimeout(()=>{btn.textContent='Retry';},2500);
  }catch(e){btn.textContent='Error';}
}

/* ══ Nodes ════════════════════════════════ */
async function viewNodes(clusterName){
  S.nodesCluster=clusterName;
  S.page='nodes';
  PAGES.forEach(p=>document.getElementById('page-'+p).style.display=p==='nodes'?'block':'none');
  document.getElementById('tb-icon').textContent='🖥️';
  document.getElementById('tb-label').textContent='Nodes — '+clusterName;
  document.querySelectorAll('.sb-item').forEach(el=>el.classList.remove('active'));
  const el=document.getElementById('page-nodes');
  el.innerHTML='<div class="loading"><span class="spin"></span>Loading nodes...</div>';
  try{
    const nodes=await GET('/api/'+enc(clusterName)+'/nodes');
    const ready=nodes.filter(n=>n.ready).length;
    const notReady=nodes.length-ready;
    let html='<div class="ph"><h1>🖥️ Nodes</h1><p>Cluster: <strong>'+esc(clusterName)+'</strong>'+
      ' &nbsp;·&nbsp; '+nodes.length+' nodes'+
      ' &nbsp;·&nbsp; <span style="color:#059669">'+ready+' ready</span>'+
      (notReady>0?' &nbsp;·&nbsp; <span style="color:#dc2626">'+notReady+' not ready</span>':'')+
      '</p></div>'+
      '<div class="stat-row" style="margin-bottom:20px">'+
      '<div class="stat-card"><div class="stat-icon si-blue">🖥️</div><div><div class="stat-val">'+nodes.length+'</div><div class="stat-label">Total Nodes</div></div></div>'+
      '<div class="stat-card"><div class="stat-icon si-green">✅</div><div><div class="stat-val">'+ready+'</div><div class="stat-label">Ready</div></div></div>'+
      (notReady>0?'<div class="stat-card"><div class="stat-icon si-red">⚠️</div><div><div class="stat-val">'+notReady+'</div><div class="stat-label">Not Ready</div></div></div>':'')+
      '</div>'+
      '<div class="node-wrap"><div class="node-title"><span>🖥️ Node List</span>'+
      '<span style="font-size:11px;color:#94a3b8;font-weight:400">Click row for full details</span></div>'+
      '<div class="rt-hdr" style="grid-template-columns:2fr 90px 110px 120px 100px 100px 80px">'+
      '<span>Name</span><span>Status</span><span>Role</span><span>Version</span><span>CPU</span><span>Memory</span><span>Age</span></div>';
    nodes.forEach(n=>{
      html+='<div class="rt-row" style="grid-template-columns:2fr 90px 110px 120px 100px 100px 80px" onclick=\'showNodeDet('+JSON.stringify(n)+')\'>'+
        '<span class="rt-name">'+esc(n.name)+'</span>'+
        '<span>'+(n.ready?'<span class="badge b-green">✓ Ready</span>':'<span class="badge b-red">✗ NotReady</span>')+'</span>'+
        '<span>'+n.roles.map(r=>'<span class="badge b-purple" style="margin-right:3px">'+esc(r)+'</span>').join('')+'</span>'+
        '<span style="font-size:12px;color:#64748b">'+esc(n.version)+'</span>'+
        '<span style="font-weight:600">'+esc(n.cpu_allocatable)+'</span>'+
        '<span style="font-weight:600">'+esc(n.mem_allocatable)+'</span>'+
        '<span style="color:#94a3b8">'+esc(n.age)+'</span></div>';
    });
    html+='</div><div id="node-det-panel"></div>';
    el.innerHTML=html;
  }catch(e){
    el.innerHTML='<div class="empty"><div class="empty-icon">⚠️</div><p style="color:#dc2626">'+esc(e.message)+'</p></div>';
  }
}

function showNodeDet(n){
  const el=document.getElementById('node-det-panel');
  if(!el) return;
  el.innerHTML='<div class="det-card" style="margin-top:16px">'+
    '<div class="det-title">🖥️ '+esc(n.name)+' '+
    (n.ready?'<span class="badge b-green">✓ Ready</span>':'<span class="badge b-red">✗ NotReady</span>')+
    (n.unschedulable?' <span class="badge b-yellow">Unschedulable</span>':'')+
    n.roles.map(r=>' <span class="badge b-purple">'+esc(r)+'</span>').join('')+
    '</div>'+
    '<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">'+
    '<div><div class="det-sec">Overview</div><div class="kv">'+
    '<span class="kk">Age</span><span class="kv2">'+n.age+'</span>'+
    '<span class="kk">Kubelet</span><span class="kv2">'+esc(n.version)+'</span>'+
    '<span class="kk">Internal IP</span><span class="kv2">'+esc(n.internal_ip)+'</span>'+
    '<span class="kk">External IP</span><span class="kv2">'+esc(n.external_ip)+'</span>'+
    '<span class="kk">Hostname</span><span class="kv2">'+esc(n.hostname)+'</span>'+
    '</div></div>'+
    '<div><div class="det-sec">System</div><div class="kv">'+
    '<span class="kk">OS</span><span class="kv2">'+esc(n.os)+'</span>'+
    '<span class="kk">Kernel</span><span class="kv2">'+esc(n.kernel)+'</span>'+
    '<span class="kk">Arch</span><span class="kv2">'+esc(n.architecture)+'</span>'+
    '<span class="kk">Runtime</span><span class="kv2">'+esc(n.container_runtime)+'</span>'+
    '</div></div></div></div>'+
    '<div class="det-card"><div class="det-sec">Capacity &amp; Allocatable</div>'+
    '<table><tr><th>Resource</th><th>Capacity</th><th>Allocatable</th></tr>'+
    '<tr><td>CPU</td><td><strong>'+esc(n.cpu_capacity)+'</strong></td><td>'+esc(n.cpu_allocatable)+'</td></tr>'+
    '<tr><td>Memory</td><td><strong>'+esc(n.mem_capacity)+'</strong></td><td>'+esc(n.mem_allocatable)+'</td></tr>'+
    '<tr><td>Max Pods</td><td colspan="2">'+esc(n.pods_capacity)+'</td></tr></table></div>'+
    '<div class="det-card"><div class="det-sec">Conditions</div><table>'+
    '<tr><th>Type</th><th>Status</th><th>Reason</th><th>Message</th></tr>'+
    n.conditions.map(c=>'<tr><td style="font-weight:600">'+esc(c.type)+'</td>'+
    '<td>'+(c.status==='True'?'<span class="badge b-green">True</span>':'<span class="badge b-gray">'+esc(c.status)+'</span>')+'</td>'+
    '<td style="color:#64748b">'+esc(c.reason)+'</td>'+
    '<td style="color:#94a3b8;font-size:12px">'+esc(c.message)+'</td></tr>').join('')+
    '</table></div>'+
    (n.taints.length?'<div class="det-card"><div class="det-sec">Taints</div><table>'+
    '<tr><th>Key</th><th>Value</th><th>Effect</th></tr>'+
    n.taints.map(t=>'<tr><td>'+esc(t.key)+'</td><td>'+esc(t.value||'—')+'</td>'+
    '<td><span class="badge b-yellow">'+esc(t.effect)+'</span></td></tr>').join('')+
    '</table></div>':'')+
    (Object.keys(n.labels).length?'<div class="det-card"><div class="det-sec">Labels</div><div class="kv">'+
    Object.entries(n.labels).map(([k,v])=>'<span class="kk">'+esc(k)+'</span><span class="kv2">'+esc(v)+'</span>').join('')+
    '</div></div>':'');
  el.scrollIntoView({behavior:'smooth',block:'start'});
}

/* ══ Namespace Dashboard ═══════════════════ */
async function loadNsDashboard(){
  if(!S.cluster||!S.namespace) return;
  stopAutoRefresh();
  document.getElementById('page-ns-dashboard').innerHTML=
    '<div class="loading"><span class="spin"></span>Loading...</div>';
  S.data={};
  const isAll=S.namespace==='__all__';
  const base=isAll?'/api/'+enc(S.cluster)+'/__all__':'/api/'+enc(S.cluster)+'/'+enc(S.namespace);
  const eps=['summary','pods','deployments','statefulsets','services','configmaps','secrets','ingresses','pvcs','events'];
  await Promise.all(eps.map(async ep=>{
    try{S.data[ep]=await GET(base+'/'+ep);}
    catch(e){S.data[ep]=ep==='summary'?{error:e.message}:[];}
  }));
  try{S.data['pvs']=await GET('/api/'+enc(S.cluster)+'/default/pvs');}
  catch(e){S.data['pvs']=[];}
  updateBadges(S.data.summary);
  if(isAll) renderAllNsDash(S.data.summary);
  else      renderNsDash();
}

/* All-NS Dashboard */
function renderAllNsDash(s){
  const p=s.pods||{};
  const bd=s.breakdown||[];
  const el=document.getElementById('page-ns-dashboard');
  let html='<div class="ph"><h1 style="display:flex;align-items:center;gap:10px">📊 All Namespaces '+
    '<span class="badge b-cyan">'+esc(S.cluster)+'</span></h1>'+
    '<p>'+bd.length+' namespace'+(bd.length!==1?'s':'')+' &nbsp;·&nbsp; click any row to drill in</p></div>'+
    '<div class="stat-row">'+
    sc('si-green','🟢',p.running||0,'Running Pods',''+(p.total||0)+' total')+
    sc('si-yellow','⚠️',p.pending||0,'Pending','')+
    sc('si-red','❌',p.failed||0,'Failed','')+
    sc('si-blue','⎈',bd.length,'Namespaces','')+
    sc('si-purple','🚀',s.deployments||0,'Deployments','')+
    sc('si-gray','🌐',s.services||0,'Services','')+
    '</div>'+
    '<div class="rt-wrap" style="margin-bottom:20px">'+
    '<div style="padding:10px 14px;background:#f8fafc;border-bottom:1px solid #e2e8f0;font-size:13px;font-weight:700;color:#1e293b;display:flex;align-items:center;justify-content:space-between">'+
    '<span>📋 Namespace Breakdown</span><span style="font-size:11px;font-weight:400;color:#94a3b8">Click row to drill in</span></div>'+
    '<div class="rt-hdr" style="grid-template-columns:2fr 80px 80px 90px 80px 80px 80px 80px">'+
    '<span>Namespace</span><span>Pods</span><span>Running</span><span>Deployments</span><span>STS</span><span>Services</span><span>PVCs</span><span>Secrets</span></div>';
  bd.forEach(r=>{
    html+='<div class="rt-row" style="grid-template-columns:2fr 80px 80px 90px 80px 80px 80px 80px" onclick="drillNs(\''+esc(r.namespace)+'\')">'+
      '<span style="font-weight:600;color:#1e293b;display:flex;align-items:center;gap:7px">'+
      '<span class="dot '+(r.pods_running===r.pods&&r.pods>0?'dg':r.pods_running>0?'dy':'dz')+'"></span>'+
      esc(r.namespace)+'</span>'+
      '<span style="color:'+(r.pods>0?'#1e293b':'#94a3b8')+';font-weight:'+(r.pods>0?600:400)+'">'+r.pods+'</span>'+
      '<span style="color:'+(r.pods_running===r.pods&&r.pods>0?'#059669':r.pods_running>0?'#d97706':'#94a3b8')+'">'+r.pods_running+'</span>'+
      '<span style="color:'+(r.deployments>0?'#1e293b':'#94a3b8')+'">'+r.deployments+'</span>'+
      '<span style="color:'+(r.statefulsets>0?'#1e293b':'#94a3b8')+'">'+r.statefulsets+'</span>'+
      '<span style="color:'+(r.services>0?'#1e293b':'#94a3b8')+'">'+r.services+'</span>'+
      '<span style="color:'+(r.pvcs>0?'#1e293b':'#94a3b8')+'">'+r.pvcs+'</span>'+
      '<span style="color:'+(r.secrets>0?'#1e293b':'#94a3b8')+'">'+r.secrets+'</span></div>';
  });
  html+='</div><p style="font-size:12px;color:#94a3b8;margin-bottom:12px">Browse all resources across namespaces:</p><div class="res-grid">';
  [['🟢','Pods','#2563eb','pods',p.total||0],
   ['🚀','Deployments','#7c3aed','deployments',s.deployments||0],
   ['💾','StatefulSets','#0891b2','statefulsets',s.statefulsets||0],
   ['🌐','Services','#059669','services',s.services||0],
   ['💿','PVCs','#d97706','pvcs',s.pvcs||0],
   ['📋','ConfigMaps','#64748b','configmaps',s.configmaps||0],
   ['🔑','Secrets','#dc2626','secrets',s.secrets||0],
   ['🔀','Ingresses','#0891b2','ingresses',s.ingresses||0],
   ['📣','Events','#dc2626','events',(S.data.events||[]).length],
  ].forEach(([ico,lbl,col,type,val])=>{
    html+='<div class="res-card" onclick="goRes(\''+type+'\')" style="border-left:4px solid '+col+'">'+
      '<div class="res-card-head"><span class="res-card-icon">'+ico+'</span><span class="res-card-name">'+lbl+'</span></div>'+
      '<div class="res-card-count" style="color:'+col+'">'+val+'</div>'+
      '<div class="res-card-sub">all namespaces</div></div>';
  });
  html+='</div>';
  el.innerHTML=html;
}

function sc(icon_cls,icon,val,label,sub){
  return '<div class="stat-card"><div class="stat-icon '+icon_cls+'">'+icon+'</div><div>'+
    '<div class="stat-val">'+val+'</div><div class="stat-label">'+label+'</div>'+
    (sub?'<div class="stat-sub" style="color:#94a3b8">'+sub+'</div>':'')+
    '</div></div>';
}

function drillNs(ns){
  S.namespace=ns;
  document.getElementById('ns-sel').value=ns;
  document.getElementById('sb-ns').textContent=ns;
  setNsPill(ns);
  showPage('ns-dashboard');
}

/* Single NS Dashboard */
function renderNsDash(){
  const s=S.data.summary||{};
  const p=s.pods||{};
  const el=document.getElementById('page-ns-dashboard');
  if(s.error){
    var isAuth = (s.error||'').toLowerCase().includes('unauthorized') || (s.error||'').toLowerCase().includes('forbidden');
    var isConn = (s.error||'').toLowerCase().includes('connect') || (s.error||'').toLowerCase().includes('timeout') || (s.error||'').toLowerCase().includes('refused');
    var icon = isAuth ? '🔐' : isConn ? '🔌' : '⚠️';
    var title = isAuth ? 'Authentication Error' : isConn ? 'Connection Failed' : 'Cluster Error';
    var hint  = isAuth ? 'Check that your kubeconfig credentials are valid and not expired.' :
                isConn ? 'The cluster may be unreachable. Check network connectivity and kubeconfig.' :
                         'An unexpected error occurred communicating with the cluster.';
    el.innerHTML='<div style="max-width:480px;margin:40px auto">'+
      '<div style="background:#fff;border:1px solid #fecaca;border-radius:12px;padding:28px 24px;text-align:center;box-shadow:0 2px 8px rgba(0,0,0,.06)">'+
      '<div style="font-size:42px;margin-bottom:12px">'+icon+'</div>'+
      '<div style="font-size:17px;font-weight:700;color:#1e293b;margin-bottom:6px">'+title+'</div>'+
      '<div style="font-size:12px;color:#94a3b8;margin-bottom:14px;line-height:1.5">'+hint+'</div>'+
      '<div style="background:#fff5f5;border:1px solid #fecaca;border-radius:8px;padding:10px 14px;font-size:12px;color:#dc2626;text-align:left;margin-bottom:18px;word-break:break-all">'+
      '<strong>Error:</strong> '+esc(s.error)+'</div>'+
      '<div style="display:flex;gap:8px;justify-content:center">'+
      '<button class="btn btn-primary btn-sm" onclick="loadNsDashboard()">↻ Retry</button>'+
      '<button class="btn btn-sm" onclick="showPage(\'clusters\')">⚙️ Manage Clusters</button>'+
      '</div></div></div>';
    return;
  }
  let html='<div class="ph"><h1>📊 '+esc(S.namespace)+'</h1>'+
    '<p>Cluster: <strong>'+esc(S.cluster)+'</strong></p></div>'+
    '<div class="stat-row">'+
    sc('si-green','🟢',p.running||0,'Running Pods',''+(p.total||0)+' total')+
    sc('si-yellow','⚠️',p.pending||0,'Pending','')+
    sc('si-red','❌',p.failed||0,'Failed','')+
    '</div><div class="res-grid">';
  [['🟢','Pods','#2563eb','pods',p.total||0,p.running+' run · '+(p.pending||0)+' pend'],
   ['🚀','Deployments','#7c3aed','deployments',s.deployments||0,'click to view'],
   ['💾','StatefulSets','#0891b2','statefulsets',s.statefulsets||0,'click to view'],
   ['🌐','Services','#059669','services',s.services||0,'click to view'],
   ['💿','PVCs','#d97706','pvcs',s.pvcs||0,'click to view'],
   ['🗄️','PVs','#dc2626','pvs',s.pvs||0,'cluster-wide'],
   ['📋','ConfigMaps','#64748b','configmaps',s.configmaps||0,'click to view'],
   ['🔑','Secrets','#7c3aed','secrets',s.secrets||0,'click to view'],
   ['🔀','Ingresses','#0891b2','ingresses',s.ingresses||0,'click to view'],
   ['📣','Events','#dc2626','events',(S.data.events||[]).length,'click to view'],
  ].forEach(([ico,lbl,col,type,val,sub])=>{
    html+='<div class="res-card" onclick="goRes(\''+type+'\')" style="border-left:4px solid '+col+'">'+
      '<div class="res-card-head"><span class="res-card-icon">'+ico+'</span><span class="res-card-name">'+lbl+'</span></div>'+
      '<div class="res-card-count" style="color:'+col+'">'+val+'</div>'+
      '<div class="res-card-sub">'+sub+'</div></div>';
  });
  html+='</div>';
  el.innerHTML=html;
}

/* Resource list */
function renderResList(type){
  const el=document.getElementById('page-resource');
  const items=S.data[type]||[];
  if(!S.cluster||!S.namespace){
    el.innerHTML='<div class="empty"><div class="empty-icon">⎈</div><p>Select a cluster and namespace first</p></div>';
    return;
  }
  if(!items.length){
    el.innerHTML='<div class="empty"><div class="empty-icon">📭</div><p>No '+type+' in "'+(S.namespace==='__all__'?'all namespaces':S.namespace)+'"</p></div>';
    return;
  }
  const allNs=S.namespace==='__all__';
  const nsColH=allNs?'<span>Namespace</span>':'';
  const nsColW=allNs?'130px ':'';
  const nsCell=(item)=>allNs?'<span><span class="badge b-cyan">'+esc(item.namespace||'')+'</span></span>':'';

  const cfgs={
    pods:{
      cols:'<span>Name</span>'+nsColH+'<span>Status</span><span>Ready</span><span>Node</span><span>Age</span><span></span>',
      ws:'2fr '+nsColW+'100px 80px 1.5fr 70px 38px',
      row:function(p){
        var pns=p.namespace||(S.namespace!='__all__'?S.namespace:'');
        var act='<span onclick="event.stopPropagation()">'+actMenu([
          {label:'&#x1F5D1;&#xFE0F; Delete Pod', fn:'deletePod', args:[p.name,pns], danger:true}
        ])+'</span>';
        return '<span>'+bold(p.name)+'</span>'+nsCell(p)+'<span>'+badge(p.phase.toLowerCase())+'</span><span>'+p.ready+'</span><span>'+esc(p.node)+'</span><span>'+p.age+'</span>'+act;
      }
    },
    deployments:{
      cols:'<span>Name</span>'+nsColH+'<span>Health</span><span>Ready</span><span>Strategy</span><span>Age</span><span></span>',
      ws:'2fr '+nsColW+'110px 100px 120px 70px 38px',
      row:function(d){
        var dns=d.namespace||(S.namespace!='__all__'?S.namespace:'');
        var act='<span onclick="event.stopPropagation()">'+actMenu([
          {label:'&#x27F3; Rollout Restart', fn:'restartDep', args:[d.name,dns]},
          {label:'&#x1F5D1;&#xFE0F; Delete', fn:'deleteDeployment', args:[d.name,dns], danger:true}
        ])+'</span>';
        return '<span>'+bold(d.name)+'</span>'+nsCell(d)+'<span>'+badge(d.health)+'</span><span>'+d.ready+'/'+d.desired+'</span><span>'+esc(d.strategy)+'</span><span>'+d.age+'</span>'+act;
      }
    },
    statefulsets:{
      cols:'<span>Name</span>'+nsColH+'<span>Health</span><span>Ready</span><span>Service</span><span>Age</span><span></span>',
      ws:'2fr '+nsColW+'110px 100px 1.5fr 70px 38px',
      row:function(s){
        var sns=s.namespace||(S.namespace!='__all__'?S.namespace:'');
        var act='<span onclick="event.stopPropagation()">'+actMenu([
          {label:'&#x27F3; Rollout Restart', fn:'restartSts', args:[s.name,sns]},
          {label:'&#x1F5D1;&#xFE0F; Delete', fn:'deleteStatefulSet', args:[s.name,sns], danger:true}
        ])+'</span>';
        return '<span>'+bold(s.name)+'</span>'+nsCell(s)+'<span>'+badge(s.health)+'</span><span>'+s.ready+'/'+s.desired+'</span><span>'+esc(s.service)+'</span><span>'+s.age+'</span>'+act;
      }
    },
    services:    {cols:'<span>Name</span>'+nsColH+'<span>Type</span><span>Cluster IP</span><span>Age</span>',
                  ws:'2fr '+nsColW+'130px 160px 70px',
                  row:s=>'<span>'+bold(s.name)+'</span>'+nsCell(s)+'<span><span class="badge b-blue">'+esc(s.type)+'</span></span><span>'+esc(s.cluster_ip)+'</span><span>'+s.age+'</span>'},
    pvcs:        {cols:'<span>Name</span>'+nsColH+'<span>Status</span><span>Capacity</span><span>Class</span><span>Age</span>',
                  ws:'2fr '+nsColW+'110px 100px 160px 70px',
                  row:p=>'<span>'+bold(p.name)+'</span>'+nsCell(p)+'<span>'+badge(p.health)+'</span><span><strong>'+esc(p.capacity)+'</strong></span><span>'+esc(p.storage_class)+'</span><span>'+p.age+'</span>'},
    pvs:         {cols:'<span>Name</span><span>Status</span><span>Capacity</span><span>Claim</span><span>Age</span>',
                  ws:'2.5fr 110px 100px 2fr 70px',
                  row:p=>'<span>'+bold(p.name)+'</span><span>'+badge(p.health)+'</span><span><strong>'+esc(p.capacity)+'</strong></span><span>'+esc(p.claim)+'</span><span>'+p.age+'</span>'},
    configmaps:  {cols:'<span>Name</span>'+nsColH+'<span>Keys</span><span>Age</span>',
                  ws:'4fr '+nsColW+'80px 80px',
                  row:c=>'<span>'+bold(c.name)+'</span>'+nsCell(c)+'<span>'+c.keys.length+'</span><span>'+c.age+'</span>'},
    secrets:     {cols:'<span>Name</span>'+nsColH+'<span>Type</span><span>Keys</span><span>Age</span>',
                  ws:'2fr '+nsColW+'2fr 60px 80px',
                  row:s=>'<span>'+bold(s.name)+'</span>'+nsCell(s)+'<span style="font-size:11px;color:#64748b">'+esc(s.type)+'</span><span>'+s.keys.length+'</span><span>'+s.age+'</span>'},
    ingresses:   {cols:'<span>Name</span>'+nsColH+'<span>Class</span><span>Rules</span><span>Age</span>',
                  ws:'2fr '+nsColW+'130px 80px 80px',
                  row:i=>'<span>'+bold(i.name)+'</span>'+nsCell(i)+'<span>'+esc(i.class)+'</span><span>'+i.rules.length+'</span><span>'+i.age+'</span>'},
    events:      {cols:'<span>Type</span>'+nsColH+'<span>Age</span><span>Reason</span><span>Object</span><span>Message</span>',
                  ws:'70px '+nsColW+'60px 130px 180px 1fr',
                  row:e=>'<span><span class="badge '+(e.type==='Warning'?'b-red':'b-cyan')+'">'+esc(e.type)+'</span></span>'+nsCell(e)+
                    '<span>'+esc(e.age)+'</span><span style="color:#d97706;font-weight:600">'+esc(e.reason)+'</span>'+
                    '<span style="font-size:12px;color:#64748b">'+esc(e.involved_object)+'</span>'+
                    '<span style="font-size:12px;color:#475569">'+esc(e.message)+'</span>'},
  }
  const cfg=cfgs[type];
  if(!cfg) return;
  const arBar = type==='pods' ?
    '<div class="ar-bar"><span class="ar-dot"></span><span class="ar-badge">Live</span>'+
    '   <!-- <span type="hidden" style="color:#64748b">Auto-refreshing every '+_arInterval+'s</span>'+
    '<span style="color:#94a3b8">— next in <span id="ar-next">'+_arCountdown+'s</span></span>-->'+
    '<button class="btn btn-sm" style="margin-left:auto;font-size:11px" onclick="silentRefreshPods()">↻ Refresh </button></div>' : '';
  let html='<div class="ph"><h1>'+(RES_META[type]?.icon||'📋')+' '+(RES_META[type]?.label||type)+'</h1>'+
    '<p>'+items.length+' item'+(items.length!==1?'s':'')+' in <strong>'+(S.namespace==='__all__'?'all namespaces':S.namespace)+'</strong></p></div>'+arBar+
    '<div class="rt-wrap"><div class="rt-hdr" style="grid-template-columns:'+cfg.ws+'">'+cfg.cols+'</div>';
  items.forEach(item=>{
    html+='<div class="rt-row" style="grid-template-columns:'+cfg.ws+'" onclick="pickItem(\''+type+'\',\''+esc(item.name)+'\')">'+cfg.row(item)+'</div>';
  });
  html+='</div>';
  el.innerHTML=html;
}

/* Item detail */
function pickItem(type,name){
  const item=(S.data[type]||[]).find(x=>x.name===name);
  if(!item||type==='events') return;
  _detType=type; _detName=name;
  S.page='detail';
  PAGES.forEach(p=>document.getElementById('page-'+p).style.display=p==='detail'?'block':'none');
  document.getElementById('tb-icon').textContent=RES_META[type]?.icon||'🔍';
  document.getElementById('tb-label').textContent=(RES_META[type]?.label||type)+': '+name;
  const renders={pods:renderPod,deployments:renderDep,statefulsets:renderSts,
                 services:renderSvc,pvcs:renderPvc,pvs:renderPv,
                 configmaps:renderCm,secrets:renderSec,ingresses:renderIng};
  if(renders[type]) renders[type](item);
}
function setDet(html){document.getElementById('det-body').innerHTML=html;}

/* Renderers */
function renderPod(p){
  setDet(
    '<div class="det-card">'+
    '<div class="det-title" style="justify-content:space-between">'+
    '<div style="display:flex;align-items:center;gap:9px;flex-wrap:wrap">'+
    '🟢 '+esc(p.name)+' '+badge(p.phase.toLowerCase())+
    '<span style="font-size:12px;color:#94a3b8">'+esc(p.namespace)+' @ '+esc(S.cluster)+'</span></div>'+
    '<button class="btn btn-sm" id="pod-ref-btn" onclick="refreshPodDetail(\''+esc(p.name)+'\',\''+esc(p.namespace||'')+'\')">↻ Refresh</button> '+
    '</div>'+
    '<div class="kv">'+
    '<span class="kk">Node</span><span class="kv2">'+esc(p.node)+'</span>'+
    '<span class="kk">Pod IP</span><span class="kv2">'+esc(p.pod_ip)+'</span>'+
    '<span class="kk">Age</span><span class="kv2">'+esc(p.age)+'</span>'+
    '<span class="kk">Ready</span><span class="kv2">'+esc(p.ready)+'</span>'+
    Object.entries(p.labels).map(([k,v])=>'<span class="kk">'+esc(k)+'</span><span class="kv2" style="color:#94a3b8">'+esc(v)+'</span>').join('')+
    '</div></div>'+
    '<div class="det-card"><div class="det-sec">Containers</div>'+p.containers.map(ccHtml).join('')+'</div>'+
    '<div class="det-card"><div class="det-sec">Conditions</div><div class="kv">'+
    p.conditions.map(c=>'<span class="kk">'+esc(c.type)+'</span><span class="kv2" style="color:'+(c.status==='True'?'#059669':'#dc2626')+'">'+(c.status==='True'?'✓':'✗')+' <span style="color:#94a3b8">'+esc(c.reason)+'</span></span>').join('')+
    '</div></div>'+
    '<div class="det-card">'+
    '<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:8px">'+
    '<div class="det-sec" style="margin-bottom:0">Events</div>'+
    '<button class="btn btn-sm" id="ev-ref-btn" onclick="refreshEvents(\''+esc(p.name)+'\',\''+esc(p.namespace||'')+'\')">↻ Refresh</button></div>'+
    '<div id="ev-box"><div class="loading"><span class="spin"></span>Loading...</div></div></div>'+
    '<div class="det-card"><div class="det-sec">Logs</div>'+
    '<div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-bottom:8px">'+
    '<button class="btn btn-sm" id="log-btn" onclick="toggleLog(\''+esc(p.name)+'\',\''+esc(p.namespace||'')+'\')">📄 Show Logs</button>'+
    '<div id="log-ctrl" style="display:none;align-items:center;gap:6px;flex-wrap:wrap">'+
    '<button class="btn btn-sm" onclick="fetchLogs(\''+esc(p.name)+'\',\''+esc(p.namespace||'')+'\')">↻ Refresh</button>'+
    '<select id="log-tail" onchange="fetchLogs(\''+esc(p.name)+'\',\''+esc(p.namespace||'')+'\')" style="padding:4px 8px;border:1px solid #e2e8f0;border-radius:6px;font-family:inherit;font-size:12px;background:#f8fafc;outline:none;">'+
    '<option value="100">100 lines</option><option value="200" selected>200 lines</option><option value="500">500 lines</option><option value="1000">1000 lines</option></select>'+
    '<button class="btn btn-sm" id="log-err-btn" onclick="toggleErrOnly()">⚠ Errors only</button>'+
    '<input id="log-filter" placeholder="🔍 filter..." oninput="applyFilter()" style="padding:4px 8px;border:1px solid #e2e8f0;border-radius:6px;font-family:inherit;font-size:12px;width:130px;outline:none;">'+
    '<span id="log-stat" style="font-size:11px;color:#94a3b8"></span></div></div>'+
    '<div class="log-box" id="log-box"></div></div>'
  );
  const evNs=p.namespace||(S.namespace!=='__all__'?S.namespace:'');
  refreshEvents(p.name, evNs);
}

async function refreshPodDetail(podName,podNs){
  const btn=document.getElementById('pod-ref-btn');
  if(btn){btn.disabled=true;btn.textContent='↻...';}
  try{
    const ns=(podNs&&podNs!=='__all__')?podNs:(S.namespace!=='__all__'?S.namespace:'default');
    const pods=await GET('/api/'+enc(S.cluster)+'/'+enc(ns)+'/pods');
    const fresh=pods.find(p=>p.name===podName);
    if(fresh){
      if(S.data.pods){const i=S.data.pods.findIndex(p=>p.name===podName);if(i>=0)S.data.pods[i]=fresh;}
      renderPod(fresh);
    }
  }catch(e){}
  if(btn){btn.disabled=false;btn.textContent='↻ Refresh';}
}

function refreshEvents(podName,ns){
  const box=document.getElementById('ev-box');
  const btn=document.getElementById('ev-ref-btn');
  if(box) box.innerHTML='<div class="loading"><span class="spin"></span>Loading events...</div>';
  if(btn){btn.disabled=true;btn.textContent='Loading...';}
  const evNs=(ns&&ns!=='__all__'&&ns!=='')?ns:(S.namespace&&S.namespace!=='__all__'?S.namespace:null);
  if(!evNs){
    if(box) box.innerHTML='<span style="color:#dc2626">Namespace unknown</span>';
    if(btn){btn.disabled=false;btn.textContent='↻ Refresh';}
    return;
  }
  fetch('/api/'+enc(S.cluster)+'/'+enc(evNs)+'/pods/'+enc(podName)+'/events',{cache:'no-store'})
    .then(r=>{if(!r.ok)throw new Error(r.statusText);return r.json();})
    .then(evs=>{if(box)box.innerHTML=evHtml(evs);})
    .catch(e=>{if(box)box.innerHTML='<span style="color:#dc2626">Error: '+esc(e.message)+'</span>';})
    .finally(()=>{if(btn){btn.disabled=false;btn.textContent='↻ Refresh';}});
}

function renderDep(d){
  setDet(
    '<div class="det-card"><div class="det-title" style="justify-content:space-between">'+
    '<div style="display:flex;align-items:center;gap:9px;flex-wrap:wrap">🚀 '+esc(d.name)+' '+badge(d.health)+'</div>'+
    '<button class="btn btn-warn btn-sm" onclick="restartDep(this,\''+esc(d.name)+'\',\''+esc(d.namespace||'')+'\')">⟳ Rollout Restart</button></div><div class="kv">'+
    '<span class="kk">Namespace</span><span class="kv2">'+esc(d.namespace)+'</span>'+
    '<span class="kk">Age</span><span class="kv2">'+esc(d.age)+'</span>'+
    '<span class="kk">Replicas</span><span class="kv2">'+d.ready+'/'+d.desired+' ready · '+d.updated+' updated · '+d.available+' available</span>'+
    '<span class="kk">Strategy</span><span class="kv2">'+esc(d.strategy)+'</span>'+
    '</div></div>'+
    '<div class="det-card"><div class="det-sec">Containers</div>'+d.containers.map(ccHtml).join('')+'</div>'+
    '<div class="det-card"><div class="det-sec">Conditions</div><div class="kv">'+
    d.conditions.map(c=>'<span class="kk">'+esc(c.type)+'</span><span class="kv2" style="color:'+(c.status==='True'?'#059669':'#d97706')+'">'+(c.status==='True'?'✓':'⚠')+' <span style="color:#94a3b8">'+esc(c.message)+'</span></span>').join('')+
    '</div></div>'+
    '<div class="det-card"><div class="det-sec">Events</div>'+evHtml(d.events)+'</div>'
  );
}

function renderSts(s){
  setDet(
    '<div class="det-card"><div class="det-title" style="justify-content:space-between">'+
    '<div style="display:flex;align-items:center;gap:9px;flex-wrap:wrap">💾 '+esc(s.name)+' '+badge(s.health)+'</div>'+
    '<button class="btn btn-warn btn-sm" onclick="restartSts(this,\''+esc(s.name)+'\',\''+esc(s.namespace||'')+'\')">⟳ Rollout Restart</button></div><div class="kv">'+
    '<span class="kk">Namespace</span><span class="kv2">'+esc(s.namespace)+'</span>'+
    '<span class="kk">Age</span><span class="kv2">'+esc(s.age)+'</span>'+
    '<span class="kk">Replicas</span><span class="kv2">'+s.ready+'/'+s.desired+'</span>'+
    '<span class="kk">Service</span><span class="kv2">'+esc(s.service)+'</span>'+
    '</div></div>'+
    '<div class="det-card"><div class="det-sec">Containers</div>'+
    s.containers.map(c=>'<div class="cont-card"><div class="cont-name">'+esc(c.name)+'</div><div class="kv"><span class="kk">Image</span><span class="kv2">'+esc(c.image)+'</span></div></div>').join('')+'</div>'+
    (s.vclaims.length?'<div class="det-card"><div class="det-sec">Volume Claim Templates</div><table><tr><th>Name</th><th>Storage</th><th>Class</th></tr>'+
    s.vclaims.map(v=>'<tr><td>'+esc(v.name)+'</td><td>'+esc(v.storage)+'</td><td>'+esc(v.class)+'</td></tr>').join('')+'</table></div>':'')+
    '<div class="det-card"><div class="det-sec">Events</div>'+evHtml(s.events)+'</div>'
  );
}

function renderSvc(s){
  setDet(
    '<div class="det-card"><div class="det-title">🌐 '+esc(s.name)+' <span class="badge b-blue">'+esc(s.type)+'</span></div><div class="kv">'+
    '<span class="kk">Namespace</span><span class="kv2">'+esc(s.namespace)+'</span>'+
    '<span class="kk">Cluster IP</span><span class="kv2">'+esc(s.cluster_ip)+'</span>'+
    '<span class="kk">Age</span><span class="kv2">'+esc(s.age)+'</span>'+
    (s.ext_ips.length?'<span class="kk">External IPs</span><span class="kv2" style="color:#059669">'+s.ext_ips.join(', ')+'</span>':'')+
    '</div></div>'+
    '<div class="det-card"><div class="det-sec">Ports</div><table><tr><th>Name</th><th>Protocol</th><th>Port</th><th>Target</th></tr>'+
    s.ports.map(p=>'<tr><td>'+esc(p.name)+'</td><td>'+esc(p.protocol)+'</td><td>'+p.port+'</td><td>'+esc(p.target)+'</td></tr>').join('')+'</table></div>'+
    (Object.keys(s.selector).length?'<div class="det-card"><div class="det-sec">Selector</div><div class="kv">'+
    Object.entries(s.selector).map(([k,v])=>'<span class="kk">'+esc(k)+'</span><span class="kv2">'+esc(v)+'</span>').join('')+'</div></div>':'')
  );
}

function renderPvc(p){
  setDet('<div class="det-card"><div class="det-title">💿 '+esc(p.name)+' '+badge(p.health)+'</div><div class="kv">'+
    '<span class="kk">Namespace</span><span class="kv2">'+esc(p.namespace)+'</span>'+
    '<span class="kk">Status</span><span class="kv2">'+badge(p.status.toLowerCase())+'</span>'+
    '<span class="kk">Volume</span><span class="kv2">'+esc(p.volume)+'</span>'+
    '<span class="kk">Capacity</span><span class="kv2" style="font-size:18px;font-weight:700;color:#2563eb">'+esc(p.capacity)+'</span>'+
    '<span class="kk">Requested</span><span class="kv2">'+esc(p.request)+'</span>'+
    '<span class="kk">Storage Class</span><span class="kv2">'+esc(p.storage_class)+'</span>'+
    '<span class="kk">Access Modes</span><span class="kv2">'+p.access_modes.join(', ')+'</span>'+
    '<span class="kk">Age</span><span class="kv2">'+esc(p.age)+'</span>'+
    '</div></div>');
}

function renderPv(p){
  setDet('<div class="det-card"><div class="det-title">🗄️ '+esc(p.name)+' '+badge(p.health)+'</div><div class="kv">'+
    '<span class="kk">Status</span><span class="kv2">'+badge(p.status.toLowerCase())+'</span>'+
    '<span class="kk">Capacity</span><span class="kv2" style="font-size:18px;font-weight:700;color:#2563eb">'+esc(p.capacity)+'</span>'+
    '<span class="kk">Storage Class</span><span class="kv2">'+esc(p.storage_class)+'</span>'+
    '<span class="kk">Access Modes</span><span class="kv2">'+p.access_modes.join(', ')+'</span>'+
    '<span class="kk">Reclaim Policy</span><span class="kv2">'+esc(p.reclaim_policy)+'</span>'+
    '<span class="kk">Source Type</span><span class="kv2">'+esc(p.source_type)+'</span>'+
    '<span class="kk">Bound To</span><span class="kv2" style="color:'+(p.claim!=='—'?'#2563eb':'#94a3b8')+'">'+esc(p.claim)+'</span>'+
    '<span class="kk">Age</span><span class="kv2">'+esc(p.age)+'</span>'+
    '</div></div>');
}

function renderCm(c){
  let data_html='';
  Object.entries(c.data).forEach(([k,v])=>{
    data_html+='<div class="cm-key">🔧 '+esc(k)+'</div><div class="cm-val">'+esc(v)+'</div>';
  });
  setDet('<div class="det-card"><div class="det-title">📋 '+esc(c.name)+'</div><div class="kv">'+
    '<span class="kk">Namespace</span><span class="kv2">'+esc(c.namespace)+'</span>'+
    '<span class="kk">Age</span><span class="kv2">'+esc(c.age)+'</span>'+
    '<span class="kk">Keys</span><span class="kv2">'+c.keys.length+'</span>'+
    '</div></div>'+
    '<div class="det-card"><div class="det-sec">Data</div>'+data_html+'</div>');
}

function renderSec(s){
  setDet('<div class="det-card"><div class="det-title">🔑 '+esc(s.name)+'</div><div class="kv">'+
    '<span class="kk">Namespace</span><span class="kv2">'+esc(s.namespace)+'</span>'+
    '<span class="kk">Type</span><span class="kv2">'+esc(s.type)+'</span>'+
    '<span class="kk">Age</span><span class="kv2">'+esc(s.age)+'</span>'+
    '</div></div>'+
    '<div class="det-card"><div class="det-sec">Keys (values redacted)</div><table><tr><th>Key</th><th>Size</th></tr>'+
    s.keys.map(k=>'<tr><td>🔒 '+esc(k.name)+'</td><td>'+k.size+' bytes</td></tr>').join('')+'</table></div>');
}

function renderIng(i){
  let rules_html='';
  i.rules.forEach(r=>{
    rules_html+='<div style="margin-bottom:12px"><div style="font-size:14px;font-weight:700;color:#059669;margin-bottom:6px">'+esc(r.host)+'</div>'+
    '<table><tr><th>Path</th><th>Service</th><th>Port</th></tr>'+
    r.paths.map(p=>'<tr><td>'+esc(p.path)+'</td><td>'+esc(p.service)+'</td><td>'+p.port+'</td></tr>').join('')+'</table></div>';
  });
  setDet('<div class="det-card"><div class="det-title">🔀 '+esc(i.name)+'</div><div class="kv">'+
    '<span class="kk">Namespace</span><span class="kv2">'+esc(i.namespace)+'</span>'+
    '<span class="kk">Class</span><span class="kv2">'+esc(i.class)+'</span>'+
    '<span class="kk">Age</span><span class="kv2">'+esc(i.age)+'</span>'+
    '</div></div><div class="det-card"><div class="det-sec">Rules</div>'+rules_html+'</div>'+
    (i.tls.length?'<div class="det-card"><div class="det-sec">TLS</div>'+
    i.tls.map(t=>'<div class="kv"><span class="kk">Hosts</span><span class="kv2" style="color:#059669">🔒 '+esc(t.hosts.join(', '))+'</span>'+
    '<span class="kk">Secret</span><span class="kv2">'+esc(t.secret)+'</span></div>').join('')+'</div>':''));
}

/* Logs — manual refresh, no auto */
function toggleLog(podName,podNs){
  const box=document.getElementById('log-box');
  const btn=document.getElementById('log-btn');
  const ctrl=document.getElementById('log-ctrl');
  if(box.classList.contains('show')){
    box.classList.remove('show'); btn.textContent='📄 Show Logs';
    if(ctrl) ctrl.style.display='none'; return;
  }
  _logRaw=[]; _logPodNs=podNs||null; _logErrOnly=false;
  box.classList.add('show'); btn.textContent='📄 Hide Logs';
  if(ctrl) ctrl.style.display='flex';
  fetchLogs(podName,podNs);
}

async function fetchLogs(podName,podNs){
  const box=document.getElementById('log-box');
  const tail=document.getElementById('log-tail')?.value||200;
  if(box) box.innerHTML='<span style="color:#94a3b8"><span class="spin"></span>Fetching...</span>';
  const ns=(podNs&&podNs!==''&&podNs!=='__all__')?podNs:_logPodNs||(S.namespace!=='__all__'?S.namespace:null);
  if(!ns){if(box)box.innerHTML='<div class="le">Namespace unknown</div>';return;}
  _logPodNs=ns;
  try{
    const d=await GET('/api/'+enc(S.cluster)+'/'+enc(ns)+'/pods/'+enc(podName)+'/logs?tail='+tail);
    const ansi=/\x1b\[[0-9;]*[a-zA-Z]/g;
    _logRaw=(d.logs||'').replace(ansi,'').split('\n');
    applyFilter();
    if(box) box.scrollTop=box.scrollHeight;
  }catch(e){
    if(box) box.innerHTML='<div class="le">Error: '+esc(e.message)+'</div>';
  }
}

function applyFilter(){
  const box=document.getElementById('log-box');
  const stat=document.getElementById('log-stat');
  const fStr=(document.getElementById('log-filter')?.value||'').toLowerCase();
  if(!box) return;
  let lines=_logErrOnly?_logRaw.filter(l=>/error|err |exception|fatal|panic/i.test(l)):_logRaw;
  if(fStr) lines=lines.filter(l=>l.toLowerCase().includes(fStr));
  let errs=0,warns=0;
  box.innerHTML=lines.map(line=>{
    const ll=line.toLowerCase();
    if(/error|err |exception|fatal|panic/.test(ll)){errs++;return '<div class="le">'+esc(line)+'</div>';}
    if(/warn|warning/.test(ll)){warns++;return '<div class="lw">'+esc(line)+'</div>';}
    return '<div class="li">'+esc(line)+'</div>';
  }).join('')||'<div class="li" style="color:#475569">No lines match.</div>';
  if(stat) stat.innerHTML=lines.length+' lines &nbsp;<span style="color:#f87171">'+errs+' err</span>&nbsp;<span style="color:#fbbf24">'+warns+' warn</span>';
}

function toggleErrOnly(){
  _logErrOnly=!_logErrOnly;
  const btn=document.getElementById('log-err-btn');
  if(btn){btn.textContent=_logErrOnly?'⚠ All lines':'⚠ Errors only';
          btn.style.background=_logErrOnly?'#fef3c7':'';btn.style.color=_logErrOnly?'#d97706':'';}
  applyFilter();
}

/* Cluster management */
async function loadClusterMgmt(){
  document.getElementById('cl-mgmt-list').innerHTML=
    '<div class="loading"><span class="spin"></span>Loading...</div>';
  try{
    const cls=await GET('/api/clusters');
    renderMgmtCards(cls);
  }catch(e){
    document.getElementById('cl-mgmt-list').innerHTML='<div style="color:#dc2626">'+esc(e.message)+'</div>';
  }
}

function renderMgmtCards(cls){
  const el=document.getElementById('cl-mgmt-list');
  if(!cls.length){
    el.innerHTML='<div style="color:#94a3b8;font-size:14px;padding:10px 0">No clusters added yet.</div>';
    return;
  }
  let html='';
  cls.forEach(c=>{
    html+='<div class="cl-card" id="mc-'+esc(c.name)+'">'+
      '<div class="cl-card-head">'+
      '<div><div class="cl-card-name">'+esc(c.name)+'</div><div class="cl-card-desc">'+esc(c.description||'')+'</div></div>'+
      '<span class="pill pill-unk" id="mc-pill-'+esc(c.name)+'">'+(c.error?'✗ No Data':'⏳ Checking...')+'</span>'+
      '</div>'+
      '<div class="cl-card-meta" id="mc-meta-'+esc(c.name)+'">'+(c.error?'<span class="mk">Error</span><span class="mv" style="color:#dc2626">'+esc(c.error)+'</span>':'')+'</div>'+
      '<div class="cl-card-actions">'+
      '<button class="btn btn-primary btn-sm" onclick="openCluster(\''+esc(c.name)+'\')">Launch</button>'+
      '<button class="btn btn-success btn-sm" onclick="testMgmt(\''+esc(c.name)+'\',this)">Test</button>'+
      '<button class="btn btn-danger btn-sm" onclick="delCluster(\''+esc(c.name)+'\')">Remove</button>'+
      '</div></div>';
  });
  el.innerHTML=html;
  // async status
  cls.filter(c=>!c.error).forEach(c=>{
    GET('/api/clusters/'+enc(c.name)+'/status').then(s=>{
      const pill=document.getElementById('mc-pill-'+c.name);
      const meta=document.getElementById('mc-meta-'+c.name);
      if(pill){pill.className='pill '+(s.status==='connected'?'pill-ok':'pill-err');
               pill.textContent=s.status==='connected'?'✓ Connected':'✗ Error';}
      if(meta) meta.innerHTML=s.status==='connected'
        ?(s.cluster?'<span class="mk">Cluster</span><span class="mv">'+esc(s.cluster)+'</span>':'')+
         (s.version?'<span class="mk">Version</span><span class="mv">'+esc(s.version)+'</span>':'')+
         (s.namespaces?'<span class="mk">Namespaces</span><span class="mv">'+s.namespaces+'</span>':'')
        :'<span class="mk">Error</span><span class="mv" style="color:#dc2626">'+esc(s.error||'Failed')+'</span>';
    }).catch(()=>{});
  });
}

async function testMgmt(name,btn){
  btn.textContent='...';
  try{
    const s=await GET('/api/clusters/'+enc(name)+'/status');
    btn.textContent=s.status==='connected'?'✓ OK':'✗ Fail';
    btn.style.cssText=s.status==='connected'?'background:#d1fae5;color:#059669;border-color:#6ee7b7':'background:#fee2e2;color:#dc2626;border-color:#fca5a5';
    setTimeout(()=>{btn.textContent='Test';btn.style.cssText='';},3000);
    if(s.status==='connected') loadClusterMgmt();
  }catch(e){btn.textContent='Error';}
}

async function delCluster(name){
  if(!confirm('Remove cluster "'+name+'"?')) return;
  await fetch('/api/clusters/'+enc(name),{method:'DELETE'});
  if(S.cluster===name){S.cluster=null;S.namespace=null;}
  loadClusterMgmt(); loadDD();
}

/* Add cluster form */
function toggleAddForm(){
  const btn=document.getElementById('add-form-toggle');
  const body=document.getElementById('add-form-body');
  btn.classList.toggle('open'); body.classList.toggle('open');
  btn.querySelector('.tarr').textContent=body.classList.contains('open')?'▲':'▼';
}
function dragOver(e){e.preventDefault();document.getElementById('drop-zone').classList.add('drag');}
function dragLeave(){document.getElementById('drop-zone').classList.remove('drag');}
function onDrop(e){e.preventDefault();dragLeave();if(e.dataTransfer.files[0])uploadFile(e.dataTransfer.files[0]);}
function onFileSelect(inp){if(inp.files[0])uploadFile(inp.files[0]);}

async function uploadFile(file){
  showFMsg('info','Reading '+file.name+'...');
  const fd=new FormData();fd.append('file',file);
  try{
    const r=await fetch('/api/clusters/upload',{method:'POST',body:fd});
    const d=await r.json();
    if(!r.ok){showFMsg('err',d.detail||'Upload failed');return;}
    _kcData=d.kubeconfig_data;
    const ok=document.getElementById('dz-ok');
    ok.textContent='✓ '+file.name+' — '+d.contexts.length+' context'+(d.contexts.length!==1?'s':'');
    ok.style.display='block';
    document.getElementById('drop-zone').classList.add('drag');
    showFMsg('ok','Ready — contexts: '+(d.contexts.join(', ')||'default'));
  }catch(e){showFMsg('err','Error: '+e.message);}
}

async function addCluster(){
  const name=document.getElementById('f-name').value.trim();
  const desc=document.getElementById('f-desc').value.trim();
  if(!name){showFMsg('err','Cluster name is required');return;}
  if(!_kcData){showFMsg('err','Upload a kubeconfig file first');return;}
  showFMsg('info','Testing connection...');
  try{
    const r=await fetch('/api/clusters',{method:'POST',
      headers:{'Content-Type':'application/json'},
      body:JSON.stringify({name,kubeconfig_data:_kcData,description:desc})});
    const d=await r.json();
    if(!r.ok){showFMsg('err',d.detail||'Error');return;}
    showFMsg('ok','✓ Connected — '+d.cluster+' ('+d.version+')');
    clearForm(); loadClusterMgmt(); loadDD();
    const body=document.getElementById('add-form-body');
    if(body.classList.contains('open')) toggleAddForm();
  }catch(e){showFMsg('err',e.message);}
}

function showFMsg(type,text){
  const el=document.getElementById('form-msg');
  el.textContent=text; el.className='form-msg fm-'+type;
}
function clearForm(){
  ['f-name','f-desc'].forEach(id=>document.getElementById(id).value='');
  const el=document.getElementById('form-msg');el.textContent='';el.className='form-msg';
  document.getElementById('dz-ok').style.display='none';
  document.getElementById('drop-zone').classList.remove('drag');
  document.getElementById('file-input').value='';
  _kcData=null;
}

/* Boot */
window.addEventListener('DOMContentLoaded',()=>{
  showPage('overview');
  loadDD();
});
"""


def get_page() -> str:
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>K8s Cluster Analyzer</title>
<style>""" + _CSS + """</style>
</head>
<body>
<div id="wrap">

<div id="sb">
  <div id="sb-brand" onclick="showPage('overview')">
    <div id="sb-brand-icon">⎈</div>
    <div><div id="sb-brand-name">K8s Analyzer</div><div id="sb-brand-sub">Multi-Cluster</div></div>
  </div>
  <div class="sb-sec">Navigation</div>
  <div class="sb-item active" id="nav-overview"     onclick="showPage('overview')">     <span class="ico">🏠</span> Overview</div>
  <div class="sb-item"        id="nav-clusters"     onclick="showPage('clusters')">     <span class="ico">⚙️</span> Clusters</div>
  <div class="sb-item"        id="nav-ns-dashboard" onclick="showPage('ns-dashboard')"> <span class="ico">📊</span> Namespace</div>
  <div class="sb-divider"></div>
  <div class="sb-sec">Resources</div>
  <div class="sb-item" id="nav-pods"         onclick="goRes('pods')">        <span class="ico">🟢</span> Pods         <span class="sb-badge" id="sc-pods">—</span></div>
  <div class="sb-item" id="nav-deployments"  onclick="goRes('deployments')"> <span class="ico">🚀</span> Deployments  <span class="sb-badge" id="sc-dep">—</span></div>
  <div class="sb-item" id="nav-statefulsets" onclick="goRes('statefulsets')"><span class="ico">💾</span> StatefulSets <span class="sb-badge" id="sc-sts">—</span></div>
  <div class="sb-item" id="nav-services"     onclick="goRes('services')">    <span class="ico">🌐</span> Services     <span class="sb-badge" id="sc-svc">—</span></div>
  <div class="sb-item" id="nav-pvcs"         onclick="goRes('pvcs')">        <span class="ico">💿</span> PVCs         <span class="sb-badge" id="sc-pvc">—</span></div>
  <div class="sb-item" id="nav-pvs"          onclick="goRes('pvs')">         <span class="ico">🗄️</span> PVs          <span class="sb-badge" id="sc-pv">—</span></div>
  <div class="sb-item" id="nav-configmaps"   onclick="goRes('configmaps')">  <span class="ico">📋</span> ConfigMaps   <span class="sb-badge" id="sc-cm">—</span></div>
  <div class="sb-item" id="nav-secrets"      onclick="goRes('secrets')">     <span class="ico">🔑</span> Secrets      <span class="sb-badge" id="sc-sec">—</span></div>
  <div class="sb-item" id="nav-ingresses"    onclick="goRes('ingresses')">   <span class="ico">🔀</span> Ingresses    <span class="sb-badge" id="sc-ing">—</span></div>
  <div class="sb-item" id="nav-events"       onclick="goRes('events')">      <span class="ico">📣</span> Events       <span class="sb-badge" id="sc-evt">—</span></div>
  <div id="sb-foot"><strong id="sb-cl">No cluster</strong><span id="sb-ns">—</span></div>
</div>

<div id="main">
  <div id="topbar">
    <div id="tb-title"><span id="tb-icon">🏠</span>&nbsp;<span id="tb-label">Cluster Overview</span></div>
    <div class="cl-wrap">
      <div class="cl-pill" onclick="toggleDD('cl-dd')">
        <span class="dot dz" id="cl-dot"></span>
        <span id="cl-pill-label">Select Cluster</span>
        <span class="arr">▼</span>
      </div>
      <div class="cl-dd" id="cl-dd">
        <div id="cl-dd-body"></div>
        <div class="cl-dd-manage" onclick="showPage('clusters');document.getElementById('cl-dd').classList.remove('open')">⚙ Manage Clusters</div>
      </div>
    </div>
    <select id="ns-sel" onchange="onNsChange(this.value)">
      <option value="">— select cluster first —</option>
    </select>
    <span id="ns-pill"></span>
    <div id="tb-right">
      <button class="btn btn-primary" onclick="refreshAll()">↻ Refresh</button>
    </div>
  </div>

  <div id="content">
    <div id="page-overview"><div class="loading"><span class="spin"></span>Loading...</div></div>
    <div id="page-nodes" style="display:none"></div>
    <div id="page-clusters" style="display:none">
      <div class="ph"><h1>⚙️ Cluster Management</h1>
        <p>Upload kubeconfig files to register clusters. Content stored in clusters.json.</p></div>
      <div id="cl-mgmt-list" class="cl-grid" style="margin-bottom:20px">
        <div class="loading"><span class="spin"></span>Loading...</div>
      </div>
      <div id="add-form-toggle" onclick="toggleAddForm()">
        <span>➕</span> Add New Cluster <span class="tarr">▼</span>
      </div>
      <div id="add-form-body">
        <div class="card" style="margin-bottom:0">
          <div class="form-msg" id="form-msg"></div>
          <div class="form-row">
            <label class="form-label">Cluster Name *</label>
            <input class="form-input" id="f-name" placeholder="e.g. production, staging" />
          </div>
          <div class="form-row">
            <label class="form-label">Upload Kubeconfig *</label>
            <div class="drop-zone" id="drop-zone"
                 onclick="document.getElementById('file-input').click()"
                 ondragover="dragOver(event)" ondragleave="dragLeave()" ondrop="onDrop(event)">
              <div class="dz-icon">📁</div>
              <div class="dz-text">Click to upload or drag &amp; drop</div>
              <div class="dz-sub">kubeconfig · admin.conf · k3s.yaml</div>
              <div class="dz-ok" id="dz-ok"></div>
            </div>
            <input type="file" id="file-input" onchange="onFileSelect(this)" />
            <div class="form-hint">Content stored in clusters.json — no file paths needed.</div>
          </div>
          <div class="form-row">
            <label class="form-label">Description (optional)</label>
            <input class="form-input" id="f-desc" placeholder="e.g. Production cluster DC1" />
          </div>
          <div style="display:flex;gap:10px">
            <button class="btn btn-primary" onclick="addCluster()">Add &amp; Test Connection</button>
            <button class="btn" onclick="clearForm()">Clear</button>
          </div>
        </div>
      </div>
    </div>
    <div id="page-ns-dashboard" style="display:none">
      <div class="empty"><div class="empty-icon">📊</div><p>Select a cluster and namespace above</p></div>
    </div>
    <div id="page-resource" style="display:none"></div>
    <div id="page-detail" style="display:none">
      <button class="btn" style="margin-bottom:16px" onclick="goBack()"> Back </button>
      <div id="det-body"></div>
    </div>
  </div>
</div>
</div>
<div id="toast-wrap"></div>
<script>""" + _JS + """</script>
</body>
</html>"""