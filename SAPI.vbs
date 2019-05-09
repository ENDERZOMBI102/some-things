Dim message, sapi 
message=InputBox("cosa vuoi che dica?","TTS")
Set sapi=CreateObject("sapi.spvoice")
sapi.Speak message
