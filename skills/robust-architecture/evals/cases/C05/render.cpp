void render(float* out, int frames) {
    std::lock_guard<std::mutex> guard(controlMutex);
    Config cfg=fetchConfigOverHttp();
    std::vector<float> scratch(frames);
    process(out,frames,cfg,scratch.data());
    writeTelemetrySynchronously(out,frames);
}

