from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import sys
ROOT=Path(__file__).resolve().parents[1]/'dist'
class Scan(HTMLParser):
 def __init__(self):super().__init__();self.refs=[];self.ids=[];self.h1=0;self.lang=False;self.title=False;self.description=False
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if tag=='html':self.lang=d.get('lang')=='en'
  if tag=='h1':self.h1+=1
  if tag=='title':self.title=True
  if tag=='meta' and d.get('name')=='description':self.description=bool(d.get('content'))
  if 'id' in d:self.ids.append(d['id'])
  for key in ['href','src','poster']:
   if key in d:self.refs.append((key,d[key]))
errors=[];pages=list(ROOT.rglob('*.html'));scans={}
for p in pages:
 s=Scan();s.feed(p.read_text());scans[p]=s
 if s.h1!=1:errors.append(f'{p}: expected one h1, got {s.h1}')
 if not(s.lang and s.title and s.description):errors.append(f'{p}: missing metadata')
 if len(s.ids)!=len(set(s.ids)):errors.append(f'{p}: duplicate IDs')
 if '@ROOT@' in p.read_text() or '[cite:' in p.read_text():errors.append(f'{p}: unresolved content')
for p,s in scans.items():
 for key,url in s.refs:
  u=urlsplit(url)
  if u.scheme or u.netloc:continue
  if u.path.startswith('/'):errors.append(f'{p}: root-absolute link {url}')
  target=(p.parent/unquote(u.path)).resolve() if u.path else p
  if not target.exists():errors.append(f'{p.relative_to(ROOT)}: missing {url}')
  if u.fragment and target in scans and u.fragment not in scans[target].ids and not(target.name=='projects.html' and u.fragment in ['all','business','software','game']):errors.append(f'{p.relative_to(ROOT)}: missing anchor {url}')
print(f'Checked {len(pages)} pages, relative links, assets, downloads, IDs, heading and metadata requirements.')
for err in errors:print(err)
sys.exit(bool(errors))
