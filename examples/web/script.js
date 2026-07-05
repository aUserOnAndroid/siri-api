document.addEventListener('DOMContentLoaded', function(){
  const baseEl = document.getElementById('base')
  const keyEl = document.getElementById('key')
  const sayText = document.getElementById('sayText')
  const noteText = document.getElementById('noteText')
  const result = document.getElementById('result')

  function show(obj){ result.textContent = JSON.stringify(obj, null, 2) }

  document.getElementById('sayBtn').addEventListener('click', async ()=>{
    const url = new URL('/say', baseEl.value)
    url.searchParams.set('text', sayText.value)
    try{
      const res = await fetch(url.toString(), { headers: { 'X-API-Key': keyEl.value } })
      const j = await res.json()
      show(j)
    }catch(e){ show({error: e.toString()}) }
  })

  document.getElementById('noteBtn').addEventListener('click', async ()=>{
    const url = new URL('/note', baseEl.value)
    try{
      const res = await fetch(url.toString(), {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'X-API-Key': keyEl.value },
        body: JSON.stringify({ text: noteText.value })
      })
      const j = await res.json()
      show(j)
    }catch(e){ show({error: e.toString()}) }
  })
})
