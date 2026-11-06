iterator=stream(factory)
async for chunk in iterator:
    render_preview(chunk)
    break
# iterator remains referenced by the view model

