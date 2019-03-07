REPO=hw9603

for name in splitter expander ranker tiler results; do
    docker tag $name hw9603/$name
    docker push hw9603/$name
done
